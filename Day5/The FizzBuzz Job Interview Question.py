# This program will print those numbers as Fizz and Buzz which gets divided by 3 and 5 respectively:
# a number divided by both 3 and 5 prints a "Fizzbuzz":

for number in range(1, 101):
   if number % 3 == 0 and number % 5 == 0:
      print("FizzBuzz")
   elif number % 3 == 0:
      print("Fizz")
   elif number % 5 == 0:
      print("buzz")
   else:
      print(number)

# The end
# thank you very much