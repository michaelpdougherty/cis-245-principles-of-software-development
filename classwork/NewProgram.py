#!/usr/bin/env python3
# Michael Dougherty & Rasaki Solebo
# In your groups, download the steps1.txt file from the Resources submodule.
# Write a program that reads the files, then displays the average number of steps taken each month.
# The year is not a leap year so February has 28 days.
# open the file
filename = "steps1.txt"
file = open(filename)


MONTHS = [
  ('January', 31),
  ('February', 28),
  ('March', 31),
  ('April', 30),
  ('May', 31),
  ('June', 30),
  ('July', 31),
  ('August', 31),
  ('September', 30),
  ('October', 31),
  ('November', 30),
  ('December', 31)
]

monthlyTotals = []

# read the file
currentDay = 0
currentMonth = 0
currentMonthlyTotal = 0

# Each iteration of this loop is a day
print("Getting monthly totals...")
for line in file:
    # Add to the monthly total
    dailySteps = int(line)
    currentMonthlyTotal += dailySteps

    daysInMonth = MONTHS[currentMonth][1]
    if currentDay + 1 == daysInMonth:
        currentMonth += 1
        currentDay = 0
        monthlyTotals.append(currentMonthlyTotal)
    else:
        currentDay += 1

# print the averages
monthlyAverages = []
print("Getting monthly averages...")
for i in range(0, 12):
    daysInMonth = MONTHS[i][1]
    monthlyTotal = monthlyTotals[i]
    monthlyAverage = monthlyTotal / daysInMonth
    monthlyAverages.append(monthlyAverage)
    monthName = MONTHS[i][0]
    print(f"{monthName:10}:\t{monthlyTotal:10}\t/\t{daysInMonth}\t=\t{monthlyAverage:10.2f}")

print("\nThank you!")
