import click
from sqlalchemy.orm import Session
from db.setup import engine
from models.product import Product
from models.store import Store
from models.audit import Audit

session = Session(bind=engine)

@click.group()
def cli():
    """Product Management System CLI"""
    pass

@click.command()
@click.option('--name', prompt='Product Name', help='The name of the product.')
@click.option('--price', prompt='Product Price', help='The price of the product.')
@click.option('--store_id', prompt='Store ID', help='The ID of the store.')
def add_product(name, price, store_id):
    """Add a new product"""
    product = Product.create(session, name, price, store_id)
    click.echo(f'Product {product.name} added successfully!')

@click.command()
def list_products():
    """List all products"""
    products = Product.get_all(session)
    for product in products:
        click.echo(f'ID: {product.id}, Name: {product.name}, Price: {product.price}')

@click.command()
@click.option('--product_id', prompt='Product ID', help='The ID of the product to delete.')
def delete_product(product_id):
    """Delete a product"""
    Product.delete(session, product_id)
    click.echo(f'Product with ID {product_id} deleted successfully!')

# Adding commands to the CLI group
cli.add_command(add_product)
cli.add_command(list_products)
cli.add_command(delete_product)

@click.command()
@click.option('--name', prompt='Store Name', help='The name of the store.')
@click.option('--location', prompt='Store Location', help='The location of the store.')
def add_store(name, location):
    """Add a new store"""
    store = Store(name=name, location=location)
    session.add(store)
    session.commit()
    click.echo(f'Store {name} added successfully!')

cli.add_command(add_store)


if __name__ == '__main__':
    cli()
