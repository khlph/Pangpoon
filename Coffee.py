class Coffee:
  no_coffee = 0
  def __init__(self,name):
    self.name = name
    # Count the variable that take in 'class'
    Coffee.no_coffee += 1

# Declared Variable
a = []
c = []

# Open 'Menu.txt'
with open('Menu.txt', 'r') as file:

# Spilt From 'Menu.txt'
  for i in file:
    a.append(i.split())

file.close()

# Seperate from list 'a' to list 'c'
for i in range(len(a)):
  if a[i][0] == 'C':
    c.append(a[i])
    #print(c)
# Assign 'c' to the class
lolc = []

for i in range(len(c)):
  c[i] = Coffee(c[i][1])
  lolc.append(c[i].name)
#print(Coffee.no_coffee) # Test
lol = len(c)%20

for i in range(0,(20-lol)):
  lolc.append(' ')
#print(lolc)
