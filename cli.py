import click
from models.store import Store
from db.setup import SessionLocal

@click.command()
@click.option('--name', prompt="Store name", help="The store's name")
@click.option('--location', prompt="Store location", help="The store's location")
def add_store(name, location):
    db = SessionLocal()
    new_store = Store(name=name, location=location)
    db.add(new_store)
    db.commit()
    click.echo(f"Store '{name}' added!")

if __name__ == '__main__':
    add_store()
