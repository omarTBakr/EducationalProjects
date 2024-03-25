# Hospital Management System (Educational Project)

This project provides a basic implementation of a hospital management system that prioritizes patients based on their urgency. It is designed for educational purposes to demonstrate concepts like object-oriented programming, data structures, and user interaction.

#  Features

- Add new patients with varying priority levels (normal, urgent, super-urgent).
    
- View all patients in the system, categorized by specialization.
    
- Retrieve the next patient in line for a specific specialization, considering their priority.
    
- Remove patients from the system.
    

### Requirements

- Python 3.7 or later
    

### Getting Started

1. Clone or download this repository.
    
2. Open a terminal in the project directory.
    
3. Run the program using the command: python main.py
    
4. Follow the prompts to interact with the system and manage patients.
    

# Tackling the Problem

_This is my approach, feel free to design the system any way you want, but consider checking this design and understand how it's implemented as it focuses on some OOP principles_
The code is structured into classes representing different entities in the system:

- Status: An Enum defining patient priority levels.
    
- Patient: Represents a patient with name, age, and status.
    
- Hospital: Manages patient queues for different specializations.
    
- HospitalSystem: Provides the user interface and interacts with the Hospital class.
    

To understand the system, start by examining these classes and their methods. The HospitalSystem class drives the main program loop, handling user input and calling appropriate methods from other classes.
