def func_salary(salary,procent):
    res = salary / 100 * procent
    return res


salary = int(input("Enter your salary>> "))
procent = float(input("Enter procent>> "))

print(func_salary(salary , procent))