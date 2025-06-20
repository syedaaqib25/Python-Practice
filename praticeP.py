# con = {}
# while True:
#     print("\n1. Add\n2. Search\n3. Delete\n4. Exit")
#     choice = input("Enter choice: ")
#     if choice == '1':
#         name = input("Enter name: ")
#         number = input("Enter number: ")
#         con[name] = number
#         print("Contact saved.")
#     elif choice == '2':
#         name = input("Enter name: ")
#         if name in con:
#             print(f"{name}: {con[name]}")
#         else:
#             print("Contact not found.")
#     elif choice == '3':
#         na = input("Enter name to delete: ")
#         if na == name:
#             del con[name]
#             print(na, "deleted")
#         else:
#             print("Nothing Deleted")
#     elif choice == '4':
#         break
#     else:
#         print("Invalid choice.")
#


# def user_profile():
#     print("\n--- User Profile Setup ---")
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     hobbies = input("Enter your hobbies (comma-separated): ").split(',')
#     profile = {
#         "Name": name,
#         "Age": age,
#         "Hobbies": [hobby.strip() for hobby in hobbies]
#     }
#     print("Profile created successfully!\n")
#     return profile
# def expense_tracker():
#     print("\n--- Expense Tracker ---")
#     expenses = []
#     for i in range(5):
#         amount = float(input(f"Enter expense {i+1} amount: "))
#         category = input("Enter category: ").strip()
#         expenses.append({"amount": amount, "category": category})
#     total = sum(e["amount"] for e in expenses)
#     unique_categories = {e["category"] for e in expenses}
#     print(f"\nTotal Expense: ₹{total}")
#     print(f"Unique Categories: {', '.join(unique_categories)}\n")
# def contact_book():
#     print("\n--- Contact Book ---")
#     contacts = {}
#     for i in range(3):
#         name = input(f"Enter name for contact {i+1}: ")
#         age = int(input("Enter age: "))
#         contacts[name] = age
#     avg_age = sum(contacts.values()) / len(contacts)
#     over_25 = [name for name, age in contacts.items() if age > 25]
#     print(f"\nAverage age of contacts: {avg_age:.2f}")
#     print(f"Contacts over age 25: {', '.join(over_25) if over_25 else 'None'}\n")
# def string_fun():
#     print("\n--- String Fun ---")
#     sentence = input("How was your day? ")
#     vowels = 'aeiouAEIOU'
#     vowel_count = sum(1 for char in sentence if char in vowels)
#     reversed_words = ' '.join(sentence.split()[::-1])
#     print(f"Uppercase: {sentence.upper()}")
#     print(f"Vowel Count: {vowel_count}")
#     print(f"Reversed Word Order: {reversed_words}\n")
# def comprehensions():
#     print("\n--- Comprehensions ---")
#     squares = [x**2 for x in range(1, 11)]
#     cubes_dict = {x: x**3 for x in range(1, 6)}
#     print(f"Squares (1–10): {squares}")
#     print(f"Cubes Dict (1–5): {cubes_dict}\n")
# def main():
#     print("=== Personal Python Dashboard ===")
#     profile = user_profile()
#     expense_tracker()
#     contact_book()
#     string_fun()
#     comprehensions()
#     print("\nThanks for using the dashboard!")
# if __name__ == "__main__":
#     main()

# class person:
#     name = None
#     age = None

#     def __init__(self):
#         print("object has been created")
#     def greet(self):
#         print("welcome")
# io=person()
# io.greet()

# class person:
#     def __init__(self, name, age):
#         self._name = name
#         self.age = age

# import os
# os.getcwd()
# print(os.getcwd())
# f=open('C:/emp.txt','r+',-1)
# print(f.read())
# f.close()

# with open("C:/emp.txt", "r") as file:
#     content = file.read()
#     print(content)



import csv, json, os

csv_file = "data.csv"
json_file = "data.json"
data = []

# Load existing data if present
if os.path.exists(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)

def save_data():
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name"])
        writer.writeheader()
        writer.writerows(data)
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)

while True:
    print("\nChoose an option:")
    print("1. Add Entry")
    print("2. Remove Entry by ID")
    print("3. Show Data")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        try:
            id_ = int(input("Enter ID: "))
            name = input("Enter Name: ")
            data.append({"id": id_, "name": name})
            save_data()
            print("Entry added.")
        except:
            print("Invalid input.")

    elif choice == "2":
        try:
            id_ = int(input("Enter ID to remove: "))
            original_len = len(data)
            data = [d for d in data if d["id"] != id_]
            if len(data) < original_len:
                save_data()
                print("Entry removed.")
            else:
                print("ID not found.")
        except:
            print("Invalid input.")

    elif choice == "3":
        print("\nCurrent Data:")
        for d in data:
            print(d)

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
