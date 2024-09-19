from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models.product import Product
from models.audit import Audit
from models.store import Store
import random

# Create an engine and bind the session
engine = create_engine('sqlite:///product-management-system.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create a Faker instance
fake = Faker()

# Define the number of records you want to generate
NUM_PRODUCTS = 10
NUM_STORES = 10
NUM_AUDITS = 10

# Define a list of car brands and models
car_brands = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes', 'Audi', 'Volkswagen', 'Hyundai']
car_models = ['Camry', 'Civic', 'Mustang', 'Malibu', 'Altima', '3 Series', 'E-Class', 'A4', 'Golf', 'Elantra']

# Generate car names by combining car brands and models
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

# Generate fake stores
stores = []
for _ in range(NUM_STORES):
    store = Store(
        name=fake.company(),
        location=fake.city(),
    )
    stores.append(store)

session.add_all(stores)
session.commit()

# Track existing product names
existing_product_names = set()

# Generate fake products with unique names
products = []
for _ in range(NUM_PRODUCTS):
    product = Product(
        name=generate_car_name(existing_product_names),
        price=fake.random_number(digits=5),
        quantity=fake.random_number(digits=3),
        store_id=fake.random_int(min=1, max=NUM_STORES)
    )
    products.append(product)

session.add_all(products)
session.commit()

# Generate fake audits
audits = []
for _ in range(NUM_AUDITS):
    audit = Audit(
        product_id=fake.random_int(min=1, max=NUM_PRODUCTS),
        product_name=fake.word(),  # If you want to keep the product_name as a fake word
        audit_date=fake.date_time_this_year()
    )
    audits.append(audit)

session.add_all(audits)
session.commit()

print("Fake data has been generated and added to the database.")
