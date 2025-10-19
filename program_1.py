# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
rainfall_data = []

for month in months:
    while True:
        try:
            rainfall = float(input(f'What was the total rainfall for {month}? '))
            rainfall_data.append((month, rainfall))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

total_rainfall = sum(r for m, r in rainfall_data)
average_rainfall = total_rainfall / len(months)

lowest_month, lowest_rainfall = min(rainfall_data, key=lambda x: x[1])
highest_month, highest_rainfall = max(rainfall_data, key=lambda x: x[1])

print(f'\nThe total rainfall for the year is {total_rainfall:.2f} inches.')
print(f'The average monthly rainfall is {average_rainfall:.2f} inches.')
print(f'The month with the lowest rainfall is {lowest_month} with {lowest_rainfall:.2f} inches.')
print(f'The month with the highest rainfall is {highest_month} with {highest_rainfall:.2f} inches.')
