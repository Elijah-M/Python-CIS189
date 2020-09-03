
age_in_years = int(input("Please enter your child's age (1-5 years): "))

# calculating years to months
def convert_to_months(years):
    months = years * 12
    return months


if __name__ == '__main__':
    # returning the "months" to the age_in_months variable
    age_in_months = convert_to_months(age_in_years)

    # outputing the data to the user
    print(age_in_years, "years is", age_in_months, "months")
