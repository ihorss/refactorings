# products_with_discount = ['type1', 'type2']
# product_type = 'type1'
product_discount = 34

class Container_A:
    def get_discount(self, current_day):
        a_discount = 0
        b_discount = 0
        c_discount = 0

        # ... long computation for weekday discount.
        # ... long result preparation.
        # ...
        # ...
        # ...
        # ...


class Container_B:
    def get_discount(self, current_day):
        return Discount().get_discount()

    class Discount:
        def __init__(self):
            self.a_discount = 0
            self.b_discount = 0
            self.c_discount = 0

        def get_discount(self):
            discount = self.calculate_discount()
            prepared_discount = self.prepare_output()
            return prepared_discount

        def calculate_discount(self):
            pass

        def prepare_output(self):
            pass