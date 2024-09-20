from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models.product import Product
from models.audit import Audit
from models.store import Store
import random

engine = create_engine('sqlite:///product-management-system.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker() 

#this describes the number of records to be generated for each model
NUM_PRODUCTS = 10
NUM_STORES = 10
NUM_AUDITS = 10


#These are the brands of cars to be populated
car_brands = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes', 'Audi', 'Volkswagen', 'Hyundai']
car_models = ['Camry', 'Civic', 'Mustang', 'Malibu', 'Altima', '3 Series', 'E-Class', 'A4', 'Golf', 'Elantra']

def generate_car_name(existing_names):
    while True:
        brand = random.choice(car_brands)
        model = random.choice(car_models)
        name = f"{brand} {model}"
        if name not in existing_names:
            existing_names.add(name)
            return name

# Clear existing data
session.query(Product).delete()
session.query(Store).delete()
session.query(Audit).delete()
session.commit()

stores = []
for _ in range(NUM_STORES):
    store = Store(
        name=fake.company(),
        location=fake.city(),
    )
    stores.append(store)

session.add_all(stores)
session.commit()

existing_product_names = set() # Track existing product names

products = []
for _ in range(NUM_PRODUCTS):
    product = Product(
        name=generate_car_name(existing_product_names),
        price=fake.random_number(digits=5),
        quantity=fake.random_number(digits=1),
        store_id=fake.random_int(min=1, max=NUM_STORES)
    )
    products.append(product)

session.add_all(products)
session.commit()

audits = []
for _ in range(NUM_AUDITS):
    audit = Audit(
        product_id=fake.random_int(min=1, max=NUM_PRODUCTS),
        product_name=fake.word(),  
        audit_date=fake.date_time_this_year()
    )
    audits.append(audit)

session.add_all(audits)
session.commit()

print("Successfully created.")
