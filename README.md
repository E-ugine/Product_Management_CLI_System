
# Product Management CLI Application

#### This Python CLI application allows users to efficiently manage a database of products, stores, and audits through a simple, intuitive command-line interface. Users can perform CRUD operations on products and stores, track product audits, and synchronize product names across audit records.


---

## Description

The **Product Management CLI Application** is designed to simplify product inventory and audit management by providing a straightforward command-line tool for adding, updating, listing, and deleting products and stores. This system is particularly useful for retail businesses or individuals who need to manage their product catalog, store data, and audit records efficiently.

With its user-friendly interface, the application allows the user to view information in table form, making it easy to understand the product and store data at a glance. It ensures data consistency by synchronizing product names across related audits whenever product details are updated.

### Key Features

- **Product Management**:
  - Add new products or update existing product quantities.
  - View all products in a well-formatted table.
  - Update product details like name and price.
  - Delete products by ID.
  
- **Store Management**:
  - Add new stores with a name and location.
  - Delete stores along with their associated products.

- **Audit Management**:
  - Record audits for products to track stock and performance over time.
  - Synchronize product names across all audits when products are updated.
  - View all audits in tabular form.

### Functionality Overview:
The system uses a **SQLite3** database with tables for products, stores, and audits. It provides commands for the following:

- **Products**: Add, view, update, and delete products.
- **Stores**: Add and delete stores.
- **Audits**: Record and synchronize audits, ensuring consistency between product and audit records.

### Future Enhancements:
- Sales management to track product sales and stock levels.
- Reporting and analytics for product performance and sales trends.
- Improved user interface for larger datasets and data visualization.

---

## Demo

To explore or contribute to the project, follow the setup instructions below.

---

## Setup/Installation Requirements

To get started, you need the following:

- **Python 3.12** installed on your system.
- A **SQLite3** database for managing product, store, and audit data.
- A terminal (Linux, macOS, or Windows with WSL) for running the CLI commands.

### Setup Steps:

1. **Clone the Repository**:
   - Go to the repository URL: `https://github.com/E-ugine/product-management-cli-app`.
   - Copy the SSH URL.
   - In your terminal, navigate to your preferred directory and run:
     ```bash
     git clone <SSH URL>
     ```

2. **Install Dependencies**:
   - Open the cloned repository:
     ```bash
     cd product-management-cli-app
     ```
   - Install required Python libraries using pip:
     ```bash
     pip install -r requirements.txt

     Install dependencies using:
    pipenv install and pipenv shell to install all dependencies
     ```

3. **Set Up the Database**:
   - Run the database setup script to initialize the SQLite database:
     ```bash
     python db/setup.py
     ```

4. **Seed Data**:
   - If needed, you can seed the database with initial data for products, stores, and audits.

5. **Run the Application**:
   - Execute the CLI application:
     ```bash
     python cli.py
     ```

6. **Use the CLI Commands**:
   - Follow the on-screen prompts to manage products, stores, and audits. Each command will guide you through the required inputs (e.g., product name, store ID, etc.).


## Technologies Used

- **Python 3.12**: Core language used to build the CLI.
- **Click Library**: Used for building CLI commands and handling user inputs.
- **SQLite3**: database for storing product, store, and audit information.
- **SQLAlchemy**: ORM used for database interactions and ensuring data integrity.
- **Tabulate Library**: Used for displaying data in a table format in the terminal.

---


