# Coffee Order Management System

This project is a Coffee Order Management System that allows customers to place orders for coffee, and track the orders, customers, and coffee details. It is built using Python and features classes to represent `Coffee`, `Customer`, and `Order` relationships.

## Table of Contents
- [Coffee Order Management System](#coffee-order-management-system)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Classes Overview](#classes-overview)
    - [Coffee Class](#coffee-class)
    - [Customer Class](#customer-class)
    - [Order Class](#order-class)
    - [Example of Creating an Order](#example-of-creating-an-order)
  - [Running Tests](#running-tests)
  - [Contributing](#contributing)

## Project Structure

```
├── Pipfile
├── Pipfile.lock
├── README.md
└── src
    └── lib
        ├── Coffee.py
        ├── Customer.py
        ├── Order.py
```

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone git@github.com:MUCHIRIJOHN1990/coffee_shop.git
   cd coffee_shop
   ```

2. **Install dependencies** using [Pipenv](https://pipenv.pypa.io/en/latest/):
   ```bash
   pipenv install --dev
   ```

3. **Activate the virtual environment**:
   ```bash
   pipenv shell
   ```

## Usage

To interact with the system, create instances of the `Customer`, `Coffee`, and `Order` classes and use their methods to manage coffee orders.

Here’s a simple example:

```python
from Coffee import Coffee
from Customer import Customer
from Order import Order

# Create Coffee and Customer objects
coffee_1 = Coffee("Esp")
customer_1 = Customer("Alice")

# Create an order for a customer
order_1 = Order(customer_1, coffee_1, 5.00)

# Get all orders for this coffee
orders = coffee_1.orders()

# Get all customers who ordered this coffee
customers = coffee_1.customers()

# Get the average price of all orders for this coffee
average_price = coffee_1.average_price()
```

## Classes Overview

### Coffee Class

- **Purpose**: The `Coffee` class manages the details of a coffee, such as its name, related orders, and customers.
- **Important Methods**:
  - `orders()`: Returns all orders associated with this coffee.
  - `customers()`: Returns all customers who ordered this coffee.
  - `num_orders()`: Returns the number of orders placed for this coffee.
  - `average_price()`: Returns the average price of all orders for this coffee.

### Customer Class

- **Purpose**: The `Customer` class handles the customer information, such as their name, their orders, and associated coffee.
- **Important Methods**:
  - `orders()`: Returns all orders placed by the customer.
  - `coffee()`: Returns all unique coffee types ordered by this customer.
  - `create_order(coffee, price)`: Creates a new order for the customer.

### Order Class

- **Purpose**: The `Order` class represents individual orders made by customers for a specific coffee at a certain price.
- **Important Attributes and Methods**:
  - `customer`: The customer who placed the order.
  - `coffee`: The coffee ordered.
  - `price`: The price of the coffee, which must be between 1.0 and 10.0.
  - `all`: A class-level list that stores all the order instances created.

### Example of Creating an Order

```python
from Coffee import Coffee
from Customer import Customer
from Order import Order

# Create instances of Customer and Coffee
customer_1 = Customer("Alice")
coffee_1 = Coffee("Latte")

# Create an order with a valid price between 1.0 and 10.0
order_1 = Order(customer_1, coffee_1, 4.50)
```

## Running Tests

Unit tests can be run using `pytest`. After setting up the project and activating the environment:

```bash
pytest
```

This will automatically discover and run all the test cases.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m "feat: description of the feature"`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
