from order import Order


class Customer:

    def __init__(self, name):
        """
        Create a new Customer object.

        Args:
            name (str): The name of the customer, which must be a string
                containing between 1 and 15 characters.
        """
        self.name = name

    @property
    def name(self):
        """
        Gets the name of the customer.

        Returns:
            str: The name of the customer.
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of the customer.

        The name must contain between 1 and 15 characters. If it does not, an
        exception will be raised.

        Args:
            name (str): The new name of the customer.
        """
        if not (1 <= len(name) <= 15):
            raise Exception
        else:
            self._name = name

    def orders(self):
        """
        Gets all orders of this customer.

        Returns:
            list: A list of all orders of this customer.
        """
        return [order for order in Order if order.customer == self]

    def coffee(self):
        """
        Gets all coffee of this customer.

        Returns:
            list: A list of all coffee of this customer.
        """
        uniqe_cofee = {
            order.coffee
            for order in Order if order.customer == self
        }

        return list(uniqe_cofee)

    def create_order(self, coffee, price):
        """
        Creates a new order for this customer.

        Args:
            coffee (Coffee): The coffee ordered.
            price (float): The price of the order.
        """
        Order(self, coffee, price)
