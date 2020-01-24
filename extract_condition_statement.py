products_with_discount = ['type1', 'type2']
current_day = 4
product_type = 'type1'

class Container_A:
    def calculate_discount(self):
        # ...some computation.

        if current_day == 1 or current_day == 4 and product_type in products_with_discount:
            discount = 25
        else:
            discount = 0

        return discount

class Container_B:
    def calculate_discount(self):
        # ...some computation.

        if self.has_discount():
            discount = 25
        else:
            discount = 0

        return discount

    def has_discount(self):
        if current_day == 1 or current_day == 4 and product_type in products_with_discount:
            return True
        else:
            return False
