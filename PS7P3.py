# bonus program

file = open("employees.txt", "r")

total_bonus = 0

print("Name   Salary   Bonus")

while True:
    name = file.readline().strip()
    if name == "":
        break

    salary = float(file.readline())

    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    bonus = salary * rate
    total_bonus = total_bonus + bonus

    print(name, "$", format(salary, ",.2f"), "$", format(bonus, ",.2f"))

file.close()

print("Total bonuses paid: $", format(total_bonus, ",.2f"))