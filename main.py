from datetime import date

from application.salary import calculate_salary
from application.db.people import get_employees

d = date.today()
print(d)


if __name__ == '__main__':
    calculate_salary()
    get_employees()