

print("======================================")
print("     Personal Income Tax Calculator")
print("======================================")

income = float(input("Enter net income: "))

total_tax = 0

print("\nTax Details")
print("--------------------------------------")

if income <= 150000:
    tax = 0
    total_tax += tax
    print(f"0 - 150,000 : {tax:,.2f} Baht")

if income > 150000:
    tax = min(income, 300000) - 150000
    tax = max(tax, 0) * 0.05
    total_tax += tax
    print(f"150,001 - 300,000 : {tax:,.2f} Baht")

if income > 300000:
    tax = min(income, 500000) - 300000
    tax = max(tax, 0) * 0.10
    total_tax += tax
    print(f"300,001 - 500,000 : {tax:,.2f} Baht")

if income > 500000:
    tax = min(income, 750000) - 500000
    tax = max(tax, 0) * 0.15
    total_tax += tax
    print(f"500,001 - 750,000 : {tax:,.2f} Baht")

if income > 750000:
    tax = min(income, 1000000) - 750000
    tax = max(tax, 0) * 0.20
    total_tax += tax
    print(f"750,001 - 1,000,000 : {tax:,.2f} Baht")

if income > 1000000:
    tax = min(income, 2000000) - 1000000
    tax = max(tax, 0) * 0.25
    total_tax += tax
    print(f"1,000,001 - 2,000,000 : {tax:,.2f} Baht")

if income > 2000000:
    tax = min(income, 5000000) - 2000000
    tax = max(tax, 0) * 0.30
    total_tax += tax
    print(f"2,000,001 - 5,000,000 : {tax:,.2f} Baht")

if income > 5000000:
    tax = income - 5000000
    tax = max(tax, 0) * 0.35
    total_tax += tax
    print(f"Over 5,000,000 : {tax:,.2f} Baht")

remaining_income = income - total_tax

if income > 0:
    effective_tax_rate = (total_tax / income) * 100
else:
    effective_tax_rate = 0

print("--------------------------------------")
print(f"Total Tax            {total_tax:,.2f} Baht")
print(f"Income After Tax     {remaining_income:,.2f} Baht")
print(f"Effective Tax Rate = {effective_tax_rate:.2f}%")
print("======================================")

