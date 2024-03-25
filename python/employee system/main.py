class Employee:
    """
    Represents an employee with name, age, and salary attributes.
    """

    def __init__(self, name, age, salary):
        """
        Initializes an Employee object with the given name, age, and salary.

        Parameters:
        - name (str): The name of the employee.
        - age (int): The age of the employee.
        - salary (float): The salary of the employee.
        """
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        """
        Returns a string representation of the Employee object.

        Returns:
        - str: A string containing the name, age, and salary of the employee.
        """
        return f' Employee: {self.name}, age: {self.age}, salary: {self.salary}'


class Company:
    """
    Represents a company with a list of employees.
    """

    def __init__(self):
        """
        Initializes a Company object with an empty list of employees.
        """
        self.employees = []

    def add_employee(self, name, age, salary):
        """
        Adds a new employee to the company.

        Parameters:
        - name (str): The name of the employee.
        - age (int): The age of the employee.
        - salary (float): The salary of the employee.
        """
        self.employees.append(Employee(name, age, salary))

    def get_employees(self):
        """
        Returns the list of employees in the company.

        Returns:
        - list: A list containing all Employee objects in the company.
        """
        return self.employees

    def delete_by_age(self, age):
        """
        Deletes employees with the given age from the company.

        Parameters:
        - age (int): The age of the employees to be deleted.
        """
        for employee in self.employees:
            if employee.age == age:
                self.employees.remove(employee)

    def update_salary_by_name(self, name, new_salary):
        """
        Updates the salary of an employee with the given name.

        Parameters:
        - name (str): The name of the employee.
        - new_salary (float): The new salary of the employee.
        """
        for employee in self.employees:
            if name == employee.name:
                employee.salary = new_salary


class FrontEnd:
    """
    Provides a front-end interface for managing employees in a company.
    """

    def __init__(self):
        """
        Initializes a FrontEnd object with a Company instance, message list, and employees list.
        """
        self.company = Company()
        self.message = ['Add new Employee', 'List all Employees', 'Delete by age', 'Update salary by name', 'End']
        self.employees = []

    def display(self):
        """
        Displays the list of available actions.
        """
        print('-------------------------------')
        for index, message in enumerate(self.message):
            print(f'{index + 1}) {message}')
        print('? ', end='')

    def get_employee_info(self):
        """
        Prompts the user to enter employee information.

        Returns:
        - dict: A dictionary containing the name, age, and salary of the employee.
        """
        name = input('Enter employee name\n? ')
        age = input('Enter employee age\n? ')
        salary = input('Enter employee salary\n? ')
        return {'name': name, 'age': age, 'salary': salary}

    def display_employees(self):
        """
        Displays the list of employees.
        """
        for index, employee in enumerate(self.employees):
            print(f'{index + 1}) {employee}')

    def run(self):
        """
        Runs the front-end interface to manage employees.
        """
        self.display()
        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print('Invalid input, please try again.')
            self.run()

        if choice == 1:
            info = self.get_employee_info()
            self.company.add_employee(info['name'], info['age'], info['salary'])
        elif choice == 2:
            self.employees = self.company.get_employees()
            self.display_employees()
        elif choice == 3:
            age = input('Enter the age: ')
            self.company.delete_by_age(age)
        elif choice == 4:
            print('Please enter the updated information for the employee.')
            info = self.get_employee_info()
            self.company.update_salary_by_name(info['name'], info['salary'])
        else:
            return

        self.run()


# Create a FrontEnd instance and run the interface
frontEnd = FrontEnd()
frontEnd.run()
