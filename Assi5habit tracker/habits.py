from datetime import datetime
class Habit:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__history = []
    def mark_done(self, date: str) -> None:
        if date not in self.__history:
            self.__history.append(date)
            self.__history.sort()
    def streak(self) -> int:
        from datetime import timedelta
        dates = [datetime.strptime(d, "%Y-%m-%d") for d in self.__history]
        dates.sort(reverse=True)
        streak = 0
        for i, date in enumerate(dates):
            if i == 0 or dates[i - 1] - date == timedelta(days=1):
                streak += 1
            else:
                break
        return streak
    def __str__(self):
        return f"{self.name}: {self.description}"
    def __repr__(self):
        return f"Habit({self.name!r}, {self.description!r})"
    def to_dict(self):
        return {"name": self.name, "description": self.description, "history": self.__history}
    @staticmethod
    def from_dict(d):
        h = Habit(d["name"], d["description"])
        h.__history = d["history"]
        return h
import json
class PersistenceError(Exception):
    pass
class HabitTracker:
    DATE_FORMAT = "%Y-%m-%d"
    def __init__(self):
        self.habits = {}
    def add_habit(self, name, desc):
        self.habits[name] = Habit(name, desc)
    def remove_habit(self, name):
        if name in self.habits:
            del self.habits[name]
    def mark_done(self, name, date=None):
        if not date:
            date = datetime.today().strftime(self.DATE_FORMAT)
        self.habits[name].mark_done(date)
    def list_habits(self):
        return list(self.habits.values())
    def report(self):
        return {name: habit.streak() for name, habit in self.habits.items()}
    def __add__(self, other):
        new_tracker = HabitTracker()
        new_tracker.habits = {**self.habits, **other.habits}
        return new_tracker
    def save(self, filename):
        try:
            with open(filename, "w") as f:
                json.dump({k: v.to_dict() for k, v in self.habits.items()}, f, indent=2)
        except OSError as e:
            raise PersistenceError(str(e))
    def load(self, filename):
        try:
            with open(filename, "r") as f:
                raw = json.load(f)
                self.habits = {k: Habit.from_dict(v) for k, v in raw.items()}
        except FileNotFoundError:
            self.habits = {}
        except json.JSONDecodeError as e:
            raise PersistenceError(str(e))

