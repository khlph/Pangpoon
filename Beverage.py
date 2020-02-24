class Beverage:
  no_beverage = 0
  def __init__(self,name,price):
    self.name = name
    self.price = price
    # Count the variable that take in 'class'
    Beverage.no_beverage += 1

# Declared Variable
a = []
b = []

# Open 'Menu.txt'
with open('Menu.txt', 'r') as file:

# Spilt From 'Menu.txt'
  for i in file:
    a.append(i.split())

file.close()

# Seperate from list 'a' to list 'b'
for i in range(len(a)):
  if a[i][0] == 'B':
    b.append(a[i])

lolb = []
# Assign 'b' to the class
for i in range(len(b)):
  b[i] = Beverage(b[i][1],b[i][2])
  lolb.append(b[i].name)
  #print(b[i].price)

lol = len(b)%20

for i in range(0,(20-lol)):
  lolb.append(' ')
#print(lolb)





