import os
import sys
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        clear()
        print("Currency Converter")
        print("------------------")
        print("1. Convert Currency")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            convert_currency()
        elif choice == "2":
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def convert_currency():
    exchange_rates = {
        "CLP": {"USD": 0.0012, "ARS": 0.012, "EUR": 0.85, "TRY": 9.2, "GBP": 0.74},
        "ARS": {"USD": 0.012, "CLP": 83.33, "EUR": 0.071, "TRY": 7.66, "GBP": 0.061},
        "USD": {"CLP": 833.33, "ARS": 83.33, "EUR": 0.85, "TRY": 9.2, "GBP": 0.74},
        "EUR": {"USD": 1.18, "ARS": 14.08, "CLP": 1176.47, "TRY": 10.7, "GBP": 0.91},
        "TRY": {"USD": 0.11, "ARS": 0.13, "EUR": 0.093, "CLP": 0.11, "GBP": 0.081},
        "GBP": {"USD": 1.35, "ARS": 16.39, "EUR": 1.1, "TRY": 12.31, "CLP": 1.35},
    }

    currencies = {
        "CLP": {"min": 1000, "max": 1000000},
        "ARS": {"min": 100, "max": 10000},
        "USD": {"min": 10, "max": 1000},
        "EUR": {"min": 10, "max": 1000},
        "TRY": {"min": 100, "max": 10000},
        "GBP": {"min": 10, "max": 1000}
    }

    clear()
    print("Available Currencies:")
    print("---------------------")
    for currency in currencies:
        print(currency)

    from_currency = input("Enter your initial currency: ")
    to_currency = input("Enter the currency you want to exchange to: ")

    if from_currency not in currencies or to_currency not in currencies:
        print("Invalid currencies. Please try again.")
        return

    amount = float(input("Enter the amount to convert: "))

    if amount < currencies[from_currency]["min"] or amount > currencies[from_currency]["max"]:
        print("Invalid amount. Please try again.")
        return

    converted_amount = amount

    if from_currency != to_currency:
        conversion_rate = exchange_rates[from_currency][to_currency]
        converted_amount *= conversion_rate  # Apply conversion rate
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

        withdraw_funds = input("Do you want to withdraw your funds? (y/n): ")

        if withdraw_funds.lower() == "y":
            converted_amount *= 0.99  # Apply 1% commission for withdrawal
            print(f"Withdrawn amount: {converted_amount:.2f} {to_currency}")

    perform_another_operation = input("Do you want to perform another operation? (y/n): ")

    if perform_another_operation.lower() == "y":
        convert_currency()

menu()
