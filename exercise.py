#How to make a simple payroll calculator
print("=== PAYROLL CALCULATOR ===")
name = input("enter employee name:- ")
hours = float(input("enter hours worked: "))
rate = float(input("enter hourly pay rate: $"))
if hours > 40:
    print("overtime = hours-40")
else:
    print("overtime = hours+40")

print("=== PAYROLL SUMMARY ===")
print(f"Employee: {name}")
print(f"Hours: {hours}")
print(f"Rate: {rate}")

