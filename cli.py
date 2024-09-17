import click
from sqlalchemy.orm import Session
from db.setup import engine
from models import Product, Store, Audit

session = Session(bind=engine)

@click.group()
def cli():
    """A simple CLI for Product Management System"""
    pass

@click.command()
@click.option('--name', prompt='Product Name', help='The name of the product.')
@click.option('--price', prompt='Product Price', help='The price of the product.')
@click.option('--store_id', prompt='Store ID', help='The ID of the store.')
def add_product(name, price, store_id):
    """Add a new product"""
    product = Product(name=name, price=price, store_id=store_id)
    session.add(product)
    session.commit()
    click.echo(f'Product {name} added successfully!')

@click.command()
def sync_audits():
    """Synchronize product names across audits"""
    products = session.query(Product).all()
    for product in products:
        if product.audits:
            for audit in product.audits:
                audit.product_name = product.name
    session.commit()
    click.echo('Product names synchronized across audits.')

cli.add_command(add_product)
cli.add_command(sync_audits)

if __name__ == '__main__':
    cli()
