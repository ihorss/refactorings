class Container:
    def process_request(self):

        # Calculate data.
        data_1 = 1 + 1
        data_2 = 2 + 2
        # ...
        calculated_data = data_1 + data_2

        # Transform data for printing.
        transformed_data = list()
        # ...
        transformed_data.append(calculated_data)

        # Printing result.
        print('*' * 80)
        print('Result data:')
        print(transformed_data)
        print('*' * 80)


class Container2:
    def process_request(self):
        calculated_data = self.calculate_data()
        transformed_data = self.transform_data(calculated_data)
        self.print_results(transformed_data)

    def calculate_data(self):
        data_1 = 1 + 1
        data_2 = 2 + 2
        # ...
        calculated_data = data_1 + data_2
        return calculated_data

    def transform_data(self, calculated_data):
        transformed_data = list()
        # ...
        transformed_data.append(calculated_data)
        return transformed_data

    def print_results(self, results):
        print('*' * 80)
        print('Result data:')
        print(results)
        print('*' * 80)








