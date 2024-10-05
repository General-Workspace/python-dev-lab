from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('--------------------')

    def pay_employees(self):
        print('Paying employees:')
        for i in self.employees:
            print(f"Paycheck for {i.fname} {i.lname}")
            print(f"Amount: ${i.calculate_paycheck():,.2f}")
            print("---------------------------------")


def main():
    my_company = Company()

    employee_1 = Employee('Aniebiet', 'Afia', 75000)
    my_company.add_employee(employee_1)

    employee_2 = Employee('John', 'Doe', 58470)
    my_company.add_employee(employee_2)

    employee_3 = Employee('Jane', 'Carter', 44000)
    my_company.add_employee(employee_3)

    my_company.display_employees()
    my_company.pay_employees()

main()
