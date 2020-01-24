# products_with_discount = ['type1', 'type2']
# product_type = 'type1'
product_discount = 34

class Container_A:
    def get_discount(self, current_day):
        # ...some computation.
        base_discount = 20
        tem_a = 10

        if current_day <= 4:
            # ... long computation
            # ...
            # ...
            # ...
            # ...
            # ...
            discount_final = base_discount +  ...

        return discount_final


class Container_A:
    def get_discount(self, current_day):
        # ...some computation.
        base_discount = 20
        tem_a = 10

        weekday_discount, temp_c, temp_b = self.get_weekday_discount(base_discount,current_day, temp_a, temp_b)

        weekend_discount, temp_d, temp_v = self.get_weekend_discount(base_discount,temp_a, temp_c, temp_b)

        discount_final = self.calculate_final_discoutn(weekday_discount, weekend_discount, temp_b, temp_v)

        return discount_final


class Container_B:

    def get_discount(self, current_day):
        # ...some computation.

        discount_final = Dicsount().get_discount(current_day)

        return discount_final


class Dicsount:
    def __init__(self):
        base_discount = 20
        weekday_discount = 0
        weekend_discount = 0
        temp_c = 0
        temp_b = 0
        temp_d = 0
        temp_v = 0

    def get_discount(self, current_day):
        # ...some computation.
        self.get_weekday_discount(current_day)
        self.get_weekend_discount()
        discount_final = self.calculate_final_discoutn()

        return discount_final




