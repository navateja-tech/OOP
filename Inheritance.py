class Employee:
    def __init__(self, name: str, emp_id: int, base_salary: float):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_salary(self) -> float:
        """Base salary calculation — no bonuses."""
        return self.base_salary

    def show_details(self) -> None:
        print(f"[ID:{self.emp_id}] {self.name} | Salary: {self.calculate_salary():.2f}")


class Manager(Employee):
    def __init__(self, name: str, emp_id: int, base_salary: float, team_size: int):
        super().__init__(name, emp_id, base_salary)   # reuse parent's __init__
        self.team_size = team_size
        self.bonus_per_member = 500

    def calculate_salary(self) -> float:
        # Extend parent behavior instead of rewriting base salary logic
        bonus = self.team_size * self.bonus_per_member
        return super().calculate_salary() + bonus

class SeniorManager(Manager):
    def __init__(self, name: str, emp_id: int, base_salary: float, team_size: int, leadership_bonus: float):
        super().__init__(name, emp_id, base_salary, team_size)   # reuse Manager's __init__
        self.leadership_bonus = leadership_bonus

    def calculate_salary(self) -> float:
        # Extend Manager's salary logic further
        return super().calculate_salary() + self.leadership_bonus
    
if __name__ == "__main__":
    emp = Employee("Ravi", 101, base_salary=40000)
    mgr = Manager("Anita", 102, base_salary=60000, team_size=5)
    sr_mgr = SeniorManager("Karan", 103, base_salary=80000, team_size=8, leadership_bonus=15000)

    for person in [emp, mgr, sr_mgr]:
        person.show_details()

    print("\nMRO of SeniorManager:", [cls.__name__ for cls in SeniorManager.__mro__])