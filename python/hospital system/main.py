from enum import Enum

# Maximum number of specializations in the hospital
MAX__SPECIALIZATION = 20

# Maximum number of patients in each specialization queue
MAX_QUEUE = 10


class Status(Enum):
    """
    Represents the priority level of a patient in the hospital system.

    * NORMAL: No urgency, patients are added to the back of the queue.
    * URGENT: Requires attention but not critical, inserted before normal patients in the queue.
    * SUPER_URGENT: Critical case needing immediate attention, inserted at the front of the queue.
    """

    NORMAL = -1
    URGENT = 0
    SUPER_URGENT = 1


class Patient:
    """
    Represents a patient in the hospital system.

    Attributes:
        name (str): Name of the patient.
        age (int): Age of the patient.
        status (Status): Priority level of the patient (NORMAL, URGENT, or SUPER_URGENT).
    """

    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

    def __str__(self):
        """
        Returns a string representation of the patient object.
        """
        return f' name: {self.name}, age: {self.age}, status: {self.status.name}'

    def __eq__(self, other):
        """
        Compares two patient objects based on their name, age, and status.
        """
        return (
            True
            if self.name == other.name and self.age == other.age and self.status.value == other.status.value
            else False
        )


class Hospital:
    """
    Manages patients in different specializations within the hospital.
    """

    def __init__(self):
        # Create a list of queues, one for each specialization
        self.patients = [[] * MAX_QUEUE for specialization in range(MAX__SPECIALIZATION)]

    def is_queue_full(self, specialization):
        """
        Checks if the queue for the given specialization is full.
        """
        return len(self.patients[specialization]) == MAX_QUEUE

    def add_patient(self, patient, specialization):
        """
        Adds a patient to the queue for the specified specialization, considering their priority level.

        Preconditions:
            There is a spot available in the specialization queue.
        """
        if patient.status == Status.NORMAL:
            # Normal patients are added to the back of the queue
            self.patients[specialization].append(patient)
            return

        # Find the insertion point for urgent or super-urgent patients
        stop_status = Status.NORMAL if patient.status == Status.URGENT else Status.URGENT

        if not self.patients[specialization]:
            # If the queue is empty, add the patient directly
            self.patients[specialization].append(patient)
            return

        # Iterate through the queue to find the insertion point
        for index, _patient in enumerate(self.patients[specialization]):
            if _patient.status == stop_status:
                # Insert the patient before the first patient with lower priority
                self.patients[specialization] = (
                    self.patients[specialization][0:index] + [patient] + self.patients[specialization][index:]
                )
                return

    def get_patients_in_specialization(self, specialization):
        """
        Returns the list of patients in the queue for the given specialization.
        """
        return self.patients[specialization]

    def get_next_patient(self, specialization):
        """
        Retrieves and removes the next patient from the queue for the specified specialization.

        Preconditions:
            0 < specialization < MAX_SPECIALIZATION
        """
        patient = self.patients[specialization][0]
        self.patients[specialization].pop(0)
        return patient

    def remove_patient(self, patient, specialization):
        """
        Removes a specific patient from the queue for the given specialization.

        Preconditions:
            The patient already exists in the specialization queue.
        """
        self.patients[specialization].remove(patient)

    def is_patient_exists(self, patient, specialization):
        """
        Checks if a patient exists in the queue for the specified specialization.
        """
        return patient in self.patients[specialization]

    def is_specialization_empty(self, specialization):
        """
        Checks if the queue for the given specialization is empty.
        """
        return len(self.patients[specialization]) == 0


class HospitalSystem:
    """
    Provides the user interface for interacting with the hospital system.
    """

    def __init__(self):
        self.hospital = Hospital()

        # Message constants
        self.EMPTY_SPECIALIZATION_MESSAGE = 'There are no patients in this specialization'
        self.FULL_QUEUE_MESSAGE = 'Sorry, there are no available spots right now, please wait'
        self.INVALID_PATIENT_INFO_MESSAGE = 'Wrong patient info, please try again'

        # Menu options
        self.menu = [
            'Add new patient',
            'Print all patients',
            'Get next patient',
            'Remove a leaving patient',
            'End the program',
        ]

    def print_menu(self):
        """
        Displays the menu of options to the user.
        """
        print('-' * 45)
        for index, choice in enumerate(self.menu):
            print(f'{index + 1}) {choice.capitalize()}')
        print('-' * 45)

    def get_choice(self):
        """
        Gets the user's choice from the menu.
        """
        self.print_menu()
        while True:
            try:
                choice = int(input(f'Enter your choice [1-{len(self.menu)}]: '))
                if 1 <= choice <= len(self.menu):
                    return choice
                else:
                    print('Invalid choice, please try again.')
            except ValueError:
                print('Invalid input, please enter a number.')

    def get_specialization(self):
        """
        Prompts the user to enter a specialization and returns its index.
        """
        while True:
            try:
                specialization = int(input(f'Enter the specialization [1-{MAX__SPECIALIZATION}]: '))
                if 1 <= specialization <= MAX__SPECIALIZATION:
                    return specialization - 1
                else:
                    print('Invalid specialization, please try again.')
            except ValueError:
                print('Invalid input, please enter a number.')

    def run(self):
        """
        Runs the main loop of the program, handling user input and calling appropriate methods.
        """
        while True:
            choice = self.get_choice()

            if choice == 1:
                self.add_patient(self.get_patient_info(), self.get_specialization())
            elif choice == 2:
                self.print_all_patient()
            elif choice == 3:
                self.get_next_patient()
            elif choice == 4:
                self.remove_patient()
            elif choice == 5:
                break
            else:
                print('Invalid choice.')

    def add_patient(self, patient, specialization):
        """
        Adds a patient to the hospital system.
        """
        if not self.hospital.is_queue_full(specialization):
            self.hospital.add_patient(patient, specialization)
        else:
            print(self.FULL_QUEUE_MESSAGE)

    def print_all_patient(self):
        """
        Prints all patients in the hospital system.
        """
        for specialization in range(MAX__SPECIALIZATION):
            print(f'{("Specialization: " + str(specialization + 1)).center(45, "-")}')
            patients = self.hospital.get_patients_in_specialization(specialization)
            for patient in patients:
                print(patient)
            if not patients:
                print('Empty'.center(45))
            print('-' * 45)

    def remove_patient(self):
        """
        Removes a patient from the hospital system.
        """
        patient = self.get_patient_info()
        specialization = self.get_specialization()

        if self.hospital.is_patient_exists(patient, specialization):
            self.hospital.remove_patient(patient, specialization)
            print('-' * 45)
            print(f'{patient} is removed')
            print('-' * 45)
        else:
            print(self.INVALID_PATIENT_INFO_MESSAGE)

    def get_next_patient(self):
        """
        Retrieves and displays the next patient for a specific specialization.
        """
        specialization = self.get_specialization()
        print('-' * 45)
        if not self.hospital.is_specialization_empty(specialization):
            next_patient = self.hospital.get_next_patient(specialization)
            print(f'{next_patient} Please go to the doctor'.upper())
        else:
            print(self.EMPTY_SPECIALIZATION_MESSAGE)
        print('-' * 45)

    def get_patient_info(self):
        """
        Prompts the user to enter patient information and returns a Patient object.
        """
        name = input('Enter the patient name: ').upper()
        age = int(input('Enter the patient age: '))

        while True:
            status_str = input('Enter the patient status (urgent, super_urgent, normal): ').strip().upper()
            if status_str in (status.name for status in Status):
                status = Status[status_str]
                break
            else:
                print('Invalid status, please try again.')

        return Patient(name, age, status)


class DummyData:
    """
    Generates dummy patient data for testing purposes.
    """

    def __init__(self, system):
        self.system = system

    def generate_data(self):
        """
        Creates and adds dummy patients to the hospital system.
        """
        for i in range(1, 18):
            name = 'Patient' + str(i)
            age = i + 20
            for status in Status:
                self.system.add_patient(Patient(name, age, status), i)


if __name__ == "__main__":
    system = HospitalSystem()
    dummy = DummyData(system)
    dummy.generate_data()
    system.run()
