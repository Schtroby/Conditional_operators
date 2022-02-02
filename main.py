
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height > 120:
  print("You can ride the rollercoaster!\n")
  age = int(input("What is your age?\n"))
  if age < 12:
    print("Please pay $5.\n")
  elif age <= 18:
    print("Please pay $7.\n")
  elif age > 18:
    print("Please pay $12.\n")

else:
  print("Sorry, you have to grow taller before you can ride.")
  