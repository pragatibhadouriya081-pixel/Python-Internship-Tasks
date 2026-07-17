stocks = {
    "apple":180,
    "tesla":250,
    "google":150,
    "amazon":200
}

total = 0

print("Available Stocks")
print(stocks)

n = int(input("How many stocks do you want to enter? "))

for i in range(n):

    name = input("Enter Stock Name : ").lower()

    quantity = int(input("Enter Quantity : "))

    if name in stocks:

        value = stocks[name] * quantity

        total = total + value

    else:
        print("Stock Not Found")

print("\nTotal Investment =", total)

file = open("portfolio.txt","w")

file.write("Total Investment = " + str(total))

file.close()

print("Data Saved Successfully")