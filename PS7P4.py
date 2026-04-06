# order program

file = open("items.txt", "r")

total = 0
count = 0

print("Item   Quantity   Price   Extended Price")

while True:
    item = file.readline().strip()
    if item == "":
        break

    quantity = int(file.readline())
    price = float(file.readline())

    extended = quantity * price

    total = total + extended
    count = count + 1

    print(item, quantity, "$", format(price, ",.2f"),
          "$", format(extended, ",.2f"))

file.close()

average = total / count

print("Total: $", format(total, ",.2f"))
print("Orders:", count)
print("Average order: $", format(average, ",.2f"))