
# Python OOP Mini-Project: Banking System

## Overview
This project demonstrates core object-oriented programming concepts using a simple banking system simulation.

### Covered Concepts
| Concept                         | Implementation                              |
|-------------------------------|----------------------------------------------|
| Class Construction & `__init__` | `BankAccount`, `SavingsAccount`, `Customer` |
| Class vs Instance Variables    | `total_accounts` in `BankAccount`           |
| Encapsulation                  | `__balance`, `@property` in BankAccount     |
| Inheritance                    | `SavingsAccount`, `CheckingAccount`         |
| Method Overriding              | `withdraw()` in `CheckingAccount`           |
| Polymorphism                   | Shared method calls in a loop               |
| Duck Typing                    | `print_account_summary()` function          |
| Operator Overloading           | `__add__` method to merge accounts          |
| Composition                    | `Customer` "has-a" accounts list            |

## Notes
- All validations are in place (deposit > 0, no negative balances).
- Used name-mangling for balance protection.
- Customer can track and transfer between accounts.

## Challenges
- Managing proper encapsulation with `@property` and name mangling.
- Demonstrating polymorphism cleanly in one loop.
