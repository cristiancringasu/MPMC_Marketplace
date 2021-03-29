"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""


class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """
    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.queue_size_per_producer = queue_size_per_producer
        self.producer_id = 0
        self.producer_queue = {}
        self.cart_id = 0
        self.consumer_cart = {}


    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        producer_id_temp = self.producer_id
        self.producer_id += 1
        self.producer_queue[str(producer_id_temp)] = []
        return str(producer_id_temp)

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        if len(self.producer_queue[producer_id]) == self.queue_size_per_producer:
            return False
        self.producer_queue[producer_id].append((product, None))
        return True

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        cart_id_temp = self.cart_id
        self.cart_id += 1
        self.consumer_cart[cart_id_temp] = []
        return cart_id_temp

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        for producer_id, products in self.producer_queue.items():
            for idx in range(len(products)):
                (product_base, booker) = products[idx]
                if product == product_base and booker == None:
                    products[idx] = (product_base, cart_id)
                    return True
        return False



    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        for producer_id, products in self.producer_queue.items():
            for idx in range(len(products)):
                (product_base, booker) = products[idx]
                if product == product_base and booker == cart_id:
                    products[idx] = (product_base, None)
                    return

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        order_list = []
        for producer_id, products in self.producer_queue.items():
            for elem in list(products):
                (product, booker) = elem
                if booker == cart_id:
                    order_list.append(product)
                    products.remove(elem)
        return order_list
