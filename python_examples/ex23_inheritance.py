from ex22_encapsulation import Employee


class SalesPerson(Employee):
    def __init__(self, **kwargs):
        kwargs['dept'] = 'sales'  # do this before calling super class constructor
        super().__init__(**kwargs)
        # use the setter property, which can do validation
        self.comm_pct = kwargs.get('comm_pct', 0.0)
        self.sales_target = kwargs.get('sales_target', 200000)

    @property
    def comm_pct(self):
        return self.__comm_pct

    @comm_pct.setter
    def comm_pct(self, value):
        # do validation here
        self.__comm_pct = value

    @property
    def sales_target(self):
        return self.__sales_target

    @sales_target.setter
    def sales_target(self, value):
        # do some validation here
        self.__sales_target = value

    def print(self):
        print('SalesPerson details:')
        super().print()
        print(f"""    Commission %: {self.__comm_pct}
    Sales target: {self.__sales_target}""")


if __name__ == '__main__':
    sp1 = SalesPerson(name='Ravi', salary=57000, comm_pct=2.5, dept='ADMIN')
    print(f'{sp1.name} earns {sp1.salary} and a commission of {sp1.comm_pct}% on sales amount')
