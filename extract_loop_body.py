class Container_A:
    def add_discounts(self, all_products):
        # some preparation/calculation
        # ...
        # ...
        # ...

        for product in all_products:
            product_metadata = self.get_product_metadata()
            product_discount = self.get_discount(product_metadata)
            # other long computation
            # ...
            product['discount'] =  product_discount
            # other long transformation/preparation
            # ...
            # ...
            # ...
            # ...
            # ...

        return all_products




    def get_product_metadata(self):
        return 1
    def get_discount(self, product_metadata):
        return 1


class Container_B:
    def add_discounts(self, all_products):
        # some preparation/calculation
        # ...
        # ...
        # ...

        for product in all_products:
            self.get_product_discount(product)
        return all_products

    def get_product_discount(self, product):
        product_metadata = self.get_product_metadata()
        product_discount = self.get_discount(product_metadata)
        # other long computation
        # ...
        product['discount'] = product_discount
        # other long transformation/preparation
        # ...
        # ...
        # ...
        # ...
        # ...




    def get_product_metadata(self):
        return 1
    def get_discount(self, product_metadata):
        return 1

