class Food:
  no_food = 0
  def __init__(self,name,price):
    self.name = name
    self.price = price
    # Count the variable that take in 'class'
    Food.no_food += 1

# Declared Variable
a = []
f = []

# Open 'Menu.txt'
with open('Menu.txt', 'r') as file:

# Spilt From 'Menu.txt'
  for i in file:
    a.append(i.split())

file.close()

# Seperate from list 'a' to list 'c'
for i in range(len(a)):
  if a[i][0] == 'F':
    f.append(a[i])
  #print(f)

lolf = []
# Assign 'c' to the class
for i in range(len(f)):
  f[i] = Food(f[i][1],f[i][2])
  lolf.append(f[i].name)
  #print(f[i].price)

lol = len(f)%20

for i in range(0,(20-lol)):
  lolf.append(' ')
#print(lolf)
