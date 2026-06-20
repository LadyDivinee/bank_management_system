# Banking Management System (OOP Demonstration)

This project is a Python-based Banking Management System designed to demonstrate the four primary pillars of Object-Oriented Programming (OOP) for my Final Project submission.

### Project Origin
* **Original Project Reference:** https://github.com/Hamed-Hasan/Python-Bank-Management 
* *Note: The original project was structurally enhanced to fully implement and demonstrate Inheritance and Polymorphism directly within the execution workflow.*

### OOP Implementation Breakdown

1. **Encapsulation:** Class variables like `balance` and `loan_limit` are protected from direct external modification. They can only be altered via validation-checked methods like `deposit()` and `withdraw()`.
2. **Abstraction:** Complex multi-step operations, such as account-to-account `transfer()` workflows and loan allocations, are hidden behind clean, single-method interfaces.
3. **Inheritance:** A master parent class `BankAccount` passes down foundational banking logic to specialized derived child classes: `SavingsAccount` and `CurrentAccount`.
4. **Polymorphism:** The `apply_yearly_update()` method is overridden by both child subclasses. Running a single maintenance loop dynamically credits interest to savings accounts while applying maintenance fees to checking accounts.

### How to Run
Run the test harness in your terminal:
```bash
python main.py
