from customer import Customer
from coffee import Coffee


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        """
        Creates a new Order object.

        Args:
            customer (Customer): The customer who made the order.
            coffee (Coffee): The coffee ordered.
            price (float): The price of the order.

        """
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def customer(self):
        """
        Gets the customer who made the order.

        Returns:
            Customer: The customer who made the order.
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer who made the order.

        Args:
            customer (Customer): The customer who made the order.

        Raises:
            Exception: If the given customer is not an instance of
                Customer.
        """
        if not isinstance(customer, Customer):
            raise Exception
        else:
            self._customer = customer

    @property
    def coffee(self):
        """
        Gets the coffee ordered.

        Returns:
            Coffee: The coffee ordered.
        """
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        """
        Sets the coffee ordered.

        Args:
            coffee (Coffee): The coffee ordered.

        Raises:
            Exception: If the given coffee is not an instance of
                Coffee.
        """
        if not isinstance(coffee, Coffee):
            raise Exception
        else:
            self._coffee = coffee

    @property
    def price(self):
        """
        Gets the price of the order.

        Returns:
            float: The price of the order.
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of the order.

        Args:
            price (float): The price of the order. Must be between 1.0 and 10.0.

        Raises:
            Exception: If the given price is not between 1.0 and 10.0.
        """
        if not (1.0 <= price <= 10.0):
            raise Exception
        else:
            self._price = price
