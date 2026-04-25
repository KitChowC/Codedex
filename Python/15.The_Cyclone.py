# Write code below 💖

height = int(input("How tall are you (in cm): "))
credits = int(input("How many credits do you have: "))

if (height >= 137 and credits >= 10):
  print("Enjoy the ride!")
elif (height < 137 and credits >= 10):
  print("You are not tall enough to ride.")
elif (height < 137 and credits < 10):
  print("You don't have enough credits.")
else:
  print("Sorry, you don't have enough height or enough credit for the ride.")
