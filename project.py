import pandas as pd

gas = pd.read_csv("GreenHouseGas.csv")
print(gas.columns)
print(gas.dtypes)
print(gas['Supply Chain Emission Factors with Margins'])



# Printing industries with most and least produced GHG
most_produced = gas['Supply Chain Emission Factors with Margins'].idxmax()
top_producer = gas.loc[most_produced]
print("Sector with Highest Gas Emission (Kg per Dollar)")
print("--------------------------------------")
print(f"NAICS Code: {top_producer['2017 NAICS Code']}")
print(f"Industry:   {top_producer['2017 NAICS Title']}")
print(f"GHG Type:   {top_producer['GHG']}")
print(f"Intensity:  {top_producer['Supply Chain Emission Factors with Margins']} kg CO₂e per 2022 USD")

least_produced = gas['Supply Chain Emission Factors with Margins'].idxmin()
lowest_producer = gas.loc[least_produced]
print("Sector with Lowest Gas Emission Kg per Dollar")
print("--------------------------------------")
print(f"NAICS Code: {lowest_producer['2017 NAICS Code']}")
print(f"Industry:   {lowest_producer['2017 NAICS Title']}")
print(f"GHG Type:   {lowest_producer['GHG']}")
print(f"Intensity:  {lowest_producer['Supply Chain Emission Factors with Margins']} kg CO₂e per 2022 USD")


#Code for finding certain industries
while True:
    user_input = input("Input a number from 1-1016 to check the name of an industry as well as the green house gasses it produces and " \
    "how much it produces per dollar spent in that industry (input quit to stop): ")
    
    if user_input == "quit":
        break
    if user_input == "":
        user_input = input("please enter a index or industry name (enter quit to stop): ")
    elif user_input.isdigit():
        user_input_1 = (int(user_input) - 1)
        if user_input != "quit":
            print(f"Sector with the index {str(user_input)}")
            print("--------------------------------------")
            print(f"NAICS Code: {gas['2017 NAICS Code'][int(user_input_1)]}")
            print(f"Industry:   {gas['2017 NAICS Title'][int(user_input_1)]}")
            print(f"GHG Type:   {gas['GHG'][int(user_input_1)]}")
            print(f"Intensity:  {gas['Supply Chain Emission Factors with Margins'][int(user_input_1)]} kg CO2e per 2022 USD")
        else: 
            print("That index is out of the range of the data set")
    elif user_input:
        industry_names = gas[gas['2017 NAICS Title'].str.contains(user_input, case=False)]
        if industry_names.empty:
            print(f"No industries found matching the industry {user_input}.")
        else:
            for each_industry, row in industry_names.iterrows():
                print("--------------------------------------")
                print(f"NAICS Code: {row['2017 NAICS Code']}")
                print(f"Industry:   {row['2017 NAICS Title']}")
                print(f"GHG Type:   {row['GHG']}")
                print(f"Intensity:  {row['Supply Chain Emission Factors with Margins']} kg CO2e per 2022 USD")


answer = input("program ended, would you like to find out which industries produce more than a certain amount of GHG per dollar spent?(yes/no)  ").lower()



# code for looking for industries that produce more than a certain amount of GHG per hour
while answer != "yes" and answer != "no":
    answer = input("Is that a yes or a no? ").lower()

if answer == "yes":
    amount = float(input(
    "Greater than what amount of kg of GHG per dollar spent do you want to check for?"
    "(input a number between 0.000 and 3.923): "))
    while True:
        user_input2 = amount
        if user_input2 != "quit":
            industries = gas[gas['Supply Chain Emission Factors with Margins'] > amount]
            if industries.empty:
                print("No industries exceed that GHG intensity.")
            else:
                print("\nIndustries emitting above your threshold:\n")
                for index, row in industries.iterrows():
                    print(f"- {row['2017 NAICS Title']} "
                          f"(NAICS {row['2017 NAICS Code']}): "
                          f"{row['Supply Chain Emission Factors with Margins']:.3f} kg CO2e/$")
        user_input2 = input("If you want to check which companies produce more than a different amount of GHG per dollar, input the \nGHG amount. If not, enter quit to stop:  ")
        if user_input2 == "quit":
            break
        else:
            amount = float(user_input2)

print("Okay, goodbye!")


