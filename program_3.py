# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
data = []
while True:
    year = input("Enter the year (or type 'exit' to finish): ")
    if year.lower() == 'exit':
        break
    state = input("Enter the name of the state: ")
    population = int(input("Enter the population of the state: "))
    data.append([int(year), state, population])


year_to_check = int(input("Enter a year to sum populations: "))
total_population = sum(pop[2] for pop in data if pop[0] == year_to_check)

print(f"Total population for the year {year_to_check}: {total_population}")
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []

    # Now have the user enter a year. 
    
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.

    # print the totalled population


# Call the main function.
if __name__ == '__main__':
    main()
