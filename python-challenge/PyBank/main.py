import csv

#define the file path
file_path = "/Users/nikolm/Desktop/budget_data.csv"

# define profit/loss
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
max_profit_increase = 0
max_profit_date = ""
max_profit_decrease = float("inf")
min_profit_date = ""

# read the CSV file into a list
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    data = list(csvreader)

    # calculate total months
    row_count = len(data)

    # initialize max_profit_date to the date of the first row
    max_profit_date = data[0][0]
    min_profit_date = data[0][0]

    # iterate over the remaining rows
    for row in data:
        date = row[0]
        profit_loss = float(row[1])
        total_profit_loss += profit_loss

        # calculate profit/loss change
        if previous_profit_loss != 0:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)

            # update max profit increase and date 
            if profit_loss_change > max_profit_increase:
                max_profit_increase = profit_loss_change
                max_profit_date = date

            # update max profit decrease and date
            if profit_loss_change < max_profit_decrease:
                max_profit_decrease = profit_loss_change
                min_profit_date = date

        previous_profit_loss = profit_loss

# calculate average change if profit_loss_changes is not empty
if profit_loss_changes:
    average_change = sum(profit_loss_changes) / len(profit_loss_changes)
else:
    average_change = 0

print("``` text")
print("Financial Analysis")
print("Total months:", row_count)
print(f"Total: ${total_profit_loss:.0f}")
print(f"Average change: ${average_change:.0f}")
print(f"Greatest increase in profits: Date: {max_profit_date}, Amount: (${max_profit_increase:.0f})")
print(f"Greatest decrease in profits: Date: {min_profit_date}, Amount: (${max_profit_decrease:.0f})")

# export text file with results
with open("Results.txt", "w") as file: 
    file.write("``` text\n")
    file.write("Financial Analysis\n")
    file.write("Total months: " + str(row_count) + "\n")
    file.write("Total: $" + str(int(total_profit_loss)) + "\n")
    file.write("Average change: $" + str(round(average_change, 2)) + "\n")
    file.write("Greatest increase in profits: Date: " + max_profit_date + ", Amount: $(" + str(int(max_profit_increase)) + ")\n")
    file.write("Greatest decrease in profits: Date: " + min_profit_date + ", Amount: $(" + str(int(max_profit_decrease)) + ")\n")
    file.write("```")
    print("Results in text file complete.txt")