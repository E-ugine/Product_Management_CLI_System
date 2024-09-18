import click
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.setup import engine
from models.product import Product
from models.store import Store
from models.audit import Audit

# Create a session with the database
session = Session(bind=engine)

@click.group()
def cli():
    """Product Management System CLI"""
    pass

# Command to add a product
@click.command()
@click.option('--name', prompt='Product Name', help='The name of the product.')
@click.option('--price', prompt='Product Price', type=int, help='The price of the product.')
@click.option('--store_id', prompt='Store ID', type=int, help='The ID of the store.')
@click.option('--product_quantity', prompt='product quantity', type=int, help='The quantity of the product.')
def add_product(name, price, store_id,product_quantity):
    """Add a new product"""
    try:
        if price < 0:
            raise ValueError("Price cannot be negative.")
        product = Product.create(session, name, price, store_id,product_quantity)
        click.echo(f'Product "{product.name}" added successfully!')
    except ValueError as e:
        click.echo(f'Error: {e}')
    except IntegrityError:
        session.rollback()
        click.echo('Error: Store ID does not exist.')

# Command to list all products
@click.command()
def list_products():
    """List all products"""
    products = Product.get_all(session)
    if products:
        for product in products:
            click.echo(f'ID: {product.id}, Name: {product.name}, Quantity: {product.quantity} Price: {product.price}')
    else:
        click.echo("No products found.")

# Command to delete a product by ID
@click.command()
@click.option('--product_id', prompt='Product ID', type=int, help='The ID of the product to delete.')
def delete_product(product_id):
    """Delete a product by ID"""
    product = Product.find_by_id(session, product_id)
    if product:
        Product.delete(session, product_id)
        click.echo(f'Product with ID {product_id} deleted successfully!')
    else:
        click.echo(f'Product with ID {product_id} not found.')

# Command to update an existing product
@click.command()
@click.option('--product_id', prompt='Product ID', type=int, help='The ID of the product to update.')
@click.option('--name', prompt='New Product Name', help='The new name of the product.')
@click.option('--price', prompt='New Product Price', type=int, help='The new price of the product.')
def update_product(product_id, name, price):
    """Update an existing product"""
    try:
        product = Product.find_by_id(session, product_id)
        if product:
            product.name = name
            product.price = price
            session.commit()
            click.echo(f'Product "{name}" updated successfully!')
        else:
            click.echo(f'Product with ID {product_id} not found.')
    except ValueError as e:
        click.echo(f'Error: {e}')

# Command to add a store
@click.command()
@click.option('--name', prompt='Store Name', help='The name of the store.')
@click.option('--location', prompt='Store Location', help='The location of the store.')
def add_store(name, location):
    """Add a new store"""
    store = Store(name=name, location=location)
    session.add(store)
    session.commit()
    click.echo(f'Store "{name}" added successfully!')

# Command to delete a store by ID
@click.command()
@click.option('--store_id', prompt='Store ID', type=int, help='The ID of the store to delete.')
def delete_store(store_id):
    """Delete a store by ID along with all related products"""
    store = Store.find_by_id(session, store_id)
    if store:
        session.delete(store)
        session.commit()
        click.echo(f'Store "{store.name}" and its associated products deleted successfully!')
    else:
        click.echo(f'Store with ID {store_id} not found.')

# Command to add an audit for a product
@click.command()
@click.option('--product_id', prompt='Product ID', type=int, help='The ID of the product being audited.')
@click.option('--audit_date', prompt='Audit Date', help='The date of the audit (e.g., 2024-09-18).')
def add_audit(product_id, audit_date):
    """Add a new audit for a product"""
    product = Product.find_by_id(session, product_id)
    if product:
        audit = Audit.create(session, product_id=product.id, product_name=product.name, audit_date=audit_date)
        click.echo(f'Audit for product "{product.name}" added successfully!')
    else:
        click.echo(f'Product with ID {product_id} not found.')

# Command to list all audits
@click.command()
def list_audits():
    """List all audits"""
    audits = Audit.get_all(session)
    if audits:
        for audit in audits:
            click.echo(f'Product: {audit.product_name}, Audit Date: {audit.audit_date}')
    else:
        click.echo("No audits found.")

# Command to synchronize product names across audits
@click.command()
def sync_audits():
    """Synchronize product names across all audits"""
    products = Product.get_all(session)
    for product in products:
        audits = session.query(Audit).filter_by(product_id=product.id).all()
        for audit in audits:
            audit.product_name = product.name
        session.commit()
    click.echo("Product names synchronized across all audits successfully!")

# Register all commands to the CLI group
cli.add_command(add_product)
cli.add_command(list_products)
cli.add_command(delete_product)
cli.add_command(update_product)
cli.add_command(add_store)
cli.add_command(delete_store)
cli.add_command(add_audit)
cli.add_command(list_audits)
cli.add_command(sync_audits)

if __name__ == '__main__':
    cli()
