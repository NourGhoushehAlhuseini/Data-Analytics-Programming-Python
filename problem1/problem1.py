problem = "problem1"
student_name = "nour"
student_number = "t0326796"

#  Part A
def months_to_DP(total_cost_of_house, annual_salary, proportion_saved):
    total_cost_of_house = float(total_cost_of_house)
    annual_salary = float(annual_salary)
    proportion_saved = float(proportion_saved)

    down_payment = 0.25 * total_cost_of_house # 25% down payment
    monthly_salary = annual_salary / 12
    current_savings = 0.0
    months = 0
    monthly_return = 0.05 / 12  # investment return rate per month
 
    while current_savings < down_payment:
        current_savings += (monthly_salary * proportion_saved) + (current_savings * monthly_return)
        months += 1

    return months

#  Part B
def months_with_biannual_raise(total_cost_of_house, annual_salary, proportion_saved, biannual_raise): # calculates the months needed to save for the down payment
    total_cost_of_house = float(total_cost_of_house)
    annual_salary = float(annual_salary)
    proportion_saved = float(proportion_saved)
    biannual_raise = float(biannual_raise)

    down_payment = 0.25 * total_cost_of_house
    monthly_salary = annual_salary / 12
    current_savings = 0.0
    months = 0
    monthly_return = 0.05 / 12

    while current_savings < down_payment:
        current_savings += (monthly_salary * proportion_saved) + (current_savings * monthly_return)
        months += 1

        if months % 6 == 0: # apply raise every 6 months
            monthly_salary *= (1 + biannual_raise)

    return months

#  Part C
def bisection_search():
    cube = 27
    epsilon = 0.01
    num_guesses = 0
    low = 0
    high = cube
    guess = (high + low) / 2.0

    while abs(guess**3 - cube) >= epsilon:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0
        num_guesses += 1

    print("num_guesses =", num_guesses)
    print(guess, "is close to the cube root of", cube)

# Inputs for users
if __name__ == "__main__":
    total_cost = float(input("Enter the total cost of the house: "))
    annual_salary = float(input("Enter your annual salary: "))
    proportion_saved = float(input("Enter the percentage of salary to save (as a decimal): "))

    use_raise = input("Do you receive a biannual raise? (yes/no): ").strip().lower() # asks user if biannual raise applies
    if use_raise == "yes":
        biannual_raise = float(input("Enter the raise percentage (as a decimal): "))
        months = months_with_biannual_raise(total_cost, annual_salary, proportion_saved, biannual_raise)
    else:
        months = months_to_DP(total_cost, annual_salary, proportion_saved)

    print(f"\nMonths needed to save for the down payment: {months}")

    play_game = input("\nDo you want to play the cube root guessing game? (yes/no): ").strip().lower()
    if play_game == "yes":
        bisection_search()
