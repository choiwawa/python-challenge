import os
import csv

budget_path = os.path.join("Resources", "budget_data.csv")

previous = 0
current = 0
running = 0
greatest_in = 0
greatest_de = 9999999999
total_sum = 0
avg_month = 0
rowcount = 0
i = 0


with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        if int(row[1]) >= greatest_in:
            greatest_in = int(row[1])
            greatest_in_name = str(row[0])

        if int(row[1])	 <= greatest_de:
            greatest_de = int(row[1])
            greatest_de_name = str(row[0])
            total_sum = int(total_sum) + int(row[1])
        
        total_sum = int(total_sum) + int(row[1])
        rowcount = rowcount + 1

        while i <= rowcount-2:
            previous = current
            current = int(row[1])
            running = running + (current - previous)
            i = i + 1

        avg_month = running / rowcount

print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(rowcount))
print("Total: $" + str(total_sum))
print("Average Change: $" + str(round(avg_month,2)))
print("Greatest Increase in Profits: $" + greatest_in_name + " $" + str(greatest_in))
print("Greatest Decreased in Profits: $" + greatest_de_name + " $" + str(greatest_de))

with open("Output.txt", "w") as output:
    output.write("Financial Analysis\n")
    output.write("------------------------\n")
    output.write("Total Months: " + str(rowcount) + "\n")
    output.write("Total: $" + str(total_sum) + "\n")
    output.write("Average Change: $" + str(round(avg_month,2))+ "\n")
    output.write("Greatest Increase in Profits: $" + greatest_in_name + " $" + str(greatest_in)+ "\n")
    output.write("Greatest Decreased in Profits: $" + greatest_de_name + " $" + str(greatest_de)+ "\n")