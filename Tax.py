def calculate_tax(income):
    # Initialize tax to 0
    tax = 0
    
    # Calculate tax on the income below 38,000 SEK
    if income <= 38000:
        tax = income * 0.30
    else:
        # Tax for the first 38,000 SEK at 30%
        tax = 38000 * 0.30
        
        # Additional 5% tax for income between 38,000 and 50,000 SEK
        if income <= 50000:
            tax += (income - 38000) * 0.05
        else:
            # Tax for income between 38,000 and 50,000 SEK
            tax += (50000 - 38000) * 0.05
            
            # Additional 5% tax for income above 50,000 SEK
            tax += (income - 50000) * 0.05
    
    return tax

# Main program
if __name__ == "__main__":
    # Read the monthly income from the user
    income = float(input("Please provide monthly income: "))
    
    # Calculate the tax based on the income
    tax = calculate_tax(income)
    
    # Output the corresponding income tax
    print(f"Corresponding income tax: {tax:.0f} SEK")


