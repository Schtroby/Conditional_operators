
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

bill = 0;

if height > 120:
  print("You can ride the rollercoaster!\n")
  age = int(input("What is your age?\n"))
  if age < 12:
    bill = 5
    print("Child tickets are $5.\n")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.\n")
  else:
    bill = 12
    print("Adult tickets are $12.\n")

  wants_photo = input("Do you want a photo taken? Y or N\n")
  if wants_photo == "Y":
    #Add 3$ to their bill
    bill += 3

  print(f"Youre finale bill is {bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")
  