import click
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.setup import engine
from models.product import Product
from models.store import Store
from models.audit import Audit
from tabulate import tabulate
import sqlite3


session = Session(bind=engine)

def display_menu(): #Displays the  menu of commands
    menu = [
        "1. Add a product",
        "2. List all products",
        "3. Delete a product",
        "4. Update a product",
        "5. Add a store",
        "6. Delete a store",
        "7. Add an audit",
        "8. List all audits",
        "9. Synchronize audit product names",
        "0. Exit"
    ]
    print("\n".join(menu))


def get_user_choice(): #Gets the user's choice and ensure it's a valid number.
    try:
        choice = int(input("Enter the number of the command you want to run: "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

def add_product():
    """Add a new product or update quantity if it already exists"""
    try:
        name = input("Enter Product Name: ")
        price = int(input("Enter Product Price: "))
        store_id = int(input("Enter Store ID: "))
        quantity = int(input("Enter Quantity: "))

        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        product = Product.create(session, name, price, store_id, quantity)
        print(f'Product "{product.name}" added or updated successfully with quantity {product.quantity}!')
    except ValueError as e:
        print(f'Error: {e}')
    except IntegrityError:
        session.rollback()
        print('Error: Store ID does not exist.')

def list_products(): #"""Lists all products in tabular form
    products = Product.get_all(session)
    if products:
        product_data = [
            [product.id, product.name, product.quantity, product.price]
            for product in products
        ]
        headers = ["ID", "Name", "Quantity", "Price"]
        print(tabulate(product_data, headers=headers, tablefmt='grid'))
    else:
        print("No products found.")

def delete_product():
    """Delete a product by ID"""
    product_id = int(input("Enter the Product ID to delete: "))
    product = Product.find_by_id(session, product_id)
    if product:
        Product.delete(session, product_id)
        print(f'Product with ID {product_id} deleted successfully!')
    else:
        print(f'Product with ID {product_id} not found.')

def update_product():
    try:
        product_id = int(input("Enter Product ID to update: "))
        name = input("Enter New Product Name: ")
        price = int(input("Enter New Product Price: "))
        
        product = Product.find_by_id(session, product_id)
        if product:
            product.name = name
            product.price = price
            session.commit()
            print(f'Product "{name}" updated successfully!')
        else:
            print(f'Product with ID {product_id} not found.')
    except ValueError as e:
        print(f'Error: {e}')

def add_store():
    name = input("Enter Store Name: ")
    location = input("Enter Store Location: ")
    store = Store(name=name, location=location)
    session.add(store)
    session.commit()
    print(f'Store "{name}" added successfully!')

def delete_store(): #Deletes a store by id along with all its  related products
    store_id = int(input("Enter Store ID to delete: "))
    store = Store.find_by_id(session, store_id)
    if store:
        session.delete(store)
        session.commit()
        print(f'Store "{store.name}" and its associated products deleted successfully!')
    else:
        print(f'Store with ID {store_id} not found.')

def add_audit():
    product_id = int(input("Enter Product ID for audit: "))
    audit_date = input("Enter Audit Date (e.g., 2024-09-18): ")
    product = Product.find_by_id(session, product_id)
    if product:
        audit = Audit.create(session, product_id=product.id, product_name=product.name, audit_date=audit_date)
        print(f'Audit for product "{product.name}" added successfully!')
    else:
        print(f'Product with ID {product_id} not found.')

def list_audits():
    audits = Audit.get_all(session)
    
    if audits:
        audit_data = [
            [audit.id, audit.product_name, audit.audit_date]
            for audit in audits
        ]
        headers = ["Audit ID", "Product Name", "Audit Date"]
        print(tabulate(audit_data, headers=headers, tablefmt='grid'))
    else:
        print("No audits found.")

def sync_audits(): #Synchronize product names for  all audits"""
    products = Product.get_all(session)
    for product in products:
        audits = session.query(Audit).filter_by(product_id=product.id).all()
        for audit in audits:
            audit.product_name = product.name
        session.commit()
    print("Product names synchronized across all audits successfully!")

def main():
    """Main function to run the menu and handle user input"""
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            add_product()
        elif choice == 2:
            list_products()
        elif choice == 3:
            delete_product()
        elif choice == 4:
            update_product()
        elif choice == 5:
            add_store()
        elif choice == 6:
            delete_store()
        elif choice == 7:
            add_audit()
        elif choice == 8:
            list_audits()
        elif choice == 9:
            sync_audits()
        elif choice == 0:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
