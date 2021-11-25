
age = input("what's your age?")

age_as_int = int(age)

year_remaining = 90 - age_as_int

day_remaining = year_remaining*365

week_remaining = year_remaining*52

months_remaining = year_remaining*12

print(months_remaining)
message = f"you have {day_remaining} days, {week_remaining} weeks and {months_remaining} months"
print(message)