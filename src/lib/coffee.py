from order import Order


class Coffee:

    def __init__(self, name):
        """
        Create a new Coffee object.

        Args:
            name (str): The name of the coffee, which must be a string
                containing between 1 and 3 characters.
        """
        self.name = name

    @property
    def name(self):
        """
        Gets the name of the coffee.

        Returns:
            str: The name of the coffee.
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of the coffee.

        The name must contain between 1 and 3 characters. If it does not, an
        exception will be raised.

        Args:
            name (str): The new name of the coffee.
        """
        if not (1 <= len(name) <= 3):
            raise Exception
        else:
            self._name = name

    def orders(self):
        """
        Gets all orders of this coffee.

        Returns:
            list: A list of all orders of this coffee.
        """
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        """
        Gets all customers of this coffee.

        Returns:
            list: A list of all customers of this coffee.
        """
        unique_customers = {
            order.customer
            for order in Order.all if order.coffee == self
        }
        return list(unique_customers)

    def num_orders(self):
        """
        Gets the number of orders of this coffee.

        Returns:
            int: The number of orders of this coffee.
        """

        return len(order for order in Order.all if order.coffee == self)

    def average_price(self):
        """
        Gets the average price of all orders of this coffee.

        Returns:
            float: The average price of all orders of this coffee.
        """
        total_price = sum(order.price for order in Order.all
                          if order.coffee == self)
        return total_price / self.num_orders()
