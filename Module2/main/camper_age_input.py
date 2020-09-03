""" Author: Elijah Morishita
    elmorishita@dmacc.edu
    9/2/2020
    The camper_age_input programs converts user's input from years to months
    and prints the results at the end of the program
    """

# gathering user input
age_in_years = int(input("Please enter your child's age (1-5 years): "))

def convert_to_months(years):
    """calculating years to months"""
    months = years * 12
    return months


if __name__ == '__main__':
    # returning the "months" to the age_in_months variable
    age_in_months = convert_to_months(age_in_years)

    # outputing the data to the user
    print(age_in_years, "years is", age_in_months, "months")

#  The end of the camper_age_input program