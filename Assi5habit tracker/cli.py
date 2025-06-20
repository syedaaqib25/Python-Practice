from habits import HabitTracker, PersistenceError
from datetime import datetime

tracker = HabitTracker()
FILENAME = "habits.json"

try:
    tracker.load(FILENAME)
except PersistenceError:
    print("Warning: Could not load previous data.")

def get_date_input():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        return datetime.today().strftime("%Y-%m-%d")
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return date
    except ValueError:
        print("Invalid date format.")
        return None

while True:
    print("\n1. Add Habit\n2. Remove Habit\n3. Mark Done\n4. List Habits\n5. Streak Report\n6. Save & Exit")
    try:
        choice = int(input("Choose option: "))
    except ValueError:
        print("Invalid input.")
        continue

    if choice == 1:
        name = input("Habit name: ")
        desc = input("Description: ")
        tracker.add_habit(name, desc)

    elif choice == 2:
        name = input("Habit name to remove: ")
        tracker.remove_habit(name)

    elif choice == 3:
        name = input("Habit name: ")
        date = get_date_input()
        if date:
            tracker.mark_done(name, date)

    elif choice == 4:
        for habit in tracker.list_habits():
            print(habit)

    elif choice == 5:
        for name, streak in tracker.report().items():
            print(f"{name}: {streak} day streak")

    elif choice == 6:
        try:
            tracker.save(FILENAME)
            print("Saved. Goodbye!")
        except PersistenceError:
            print("Error saving file.")
        break

    else:
        print("Choose 1–6.")
