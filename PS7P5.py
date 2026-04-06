# tuition program

file = open("students.txt", "r")

total_tuition = 0
count = 0

print("Name   Credits   Tuition")

while True:
    name = file.readline().strip()
    if name == "":
        break

    district = file.readline().strip()
    credits = int(file.readline())

    if district == "I":
        cost = 250
    else:
        cost = 500

    tuition = credits * cost

    total_tuition = total_tuition + tuition
    count = count + 1

    print(name, credits, "$", format(tuition, ",.2f"))

file.close()

print("Total tuition: $", format(total_tuition, ",.2f"))
print("Number of students:", count)