"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
import time

class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time
        super(Consumer, self).__init__(**kwargs)

    def run(self):
        for cart in self.carts:
            self.cart_id = self.marketplace.new_cart()
            for item in cart:
                for i in range(item['quantity']):
                    if item['type'] == 'add':
                        while not self.marketplace.add_to_cart(self.cart_id, item['product']):
                            time.sleep(self.retry_wait_time)
                    elif item['type'] == 'remove':
                        self.marketplace.remove_from_cart(self.cart_id, item['product'])
            print("\n".join(self.name + " bought " + str(i) for i in self.marketplace.place_order(self.cart_id)))
