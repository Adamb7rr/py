def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError('Invalid amount')
            return amount
        except ValueError:
            print("Invalid amount")

def get_currency(label):
    currencies = ('EGP', 'USD', 'EUR')
    while True:
        currency = input(f"{label} currency (EGP/USD/EUR): ").upper()
        if currency not in currencies:
            print("Invalid currency")
        else:
            return currency
        
def convert(amount, source, target):
    exchange_rates = {
        'EGP': {'USD': 0.02, 'EUR': 0.01},
        'USD': {'EGP': 47.57, 'EUR': 0.84},
        'EUR': {'EGP': 56.05, 'USD': 1.17}
    }
    if source == target:
        return amount
    return amount * exchange_rates[source][target]
    
def main():
    while True:
        user = input("Do you want to convert again? (y/n): ")
        if user == 'y':
            amount = get_amount()
            source = get_currency('Source')
            target = get_currency('Target')
            exchange = convert(amount, source, target)
            print(f'${amount} {source} is equal to ${exchange:.2f} {target}')
        elif user == 'n':
            print("Exit...")
            break

if __name__==('__main__'):
    main()