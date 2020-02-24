# This is PangPoon point of sale system
# For work assignment purpose only***
#
# Programming Fundamentals
# 010123103
#
# This Program coding by
# Kajornphat  Ngamsom, 22 Nov 2016
# 5901012620029
#
# Program include file module name
# - Coffee.py
# - Beverage.py
# - Food.py
#

import Coffee # Class Coffee
import Beverage # Class Beverage
import Food # Class Food

l = 0
n = 0
order = [[[]]]
def createorder():
  global n
  global l
  n += 1
  order.append([])
  order[n].append([])
  l = 0
def createlist():
  global n
  global l
  l += 1
  order[n].append([])


# Main User Interface
def OpenUI():
  '''This function open program interface'''
  subtotal = 0
  print('#'*29,' Pang Pone POS SYS ','#'*30)
  print('#'+(' '*78)+'#')
  print('#',' Welcome',' '*68+'#')
  print('# 1.Coffee 2.Beverage 3.Food',' '*50+'#')
  print('# Please Select the section above to continue',' '*33+'#')
  #print(order[n][l])
  print('#'+' '*78+'#')
  print('# '+'Order No.{}'.format(n)+' '*(79-11-len(str(n)))+'#')
  if order[n] != [[]]:

    for i in range(0,14):
      try:
        print('# '+'{}.'.format(i+1) + order[n][i][0] + ' '*(40-len(order[n][i][0])) + str(order[n][i][1])+
              ' '*(36-len(str(order[n][i][1]))-len(str(i)))+'#')
        subtotal = order[n][i][1] + subtotal

      except IndexError :
        print('#' + (' ' * 78) + '#')

      if  i == 13 :
          print('# Subtotal' + ' '*34 + str(subtotal) + ' '*(80-45-len(str(subtotal))) + '#')

  else :
    for i in range(15):
      print('#' + (' ' * 78) + '#')
  print('# Press "N,n" to create the new order.',' '*40+'#','\n# Press "q" to terminate the program.',' '*41+'#')
  print('#'*80)
  key = input('')

  # If user select to enter Coffee
  if key == '1':
    CoffeeUI()
    return OpenUI()

  if key == '2':
    BeverageUI()
    return OpenUI()

  if key == '3':
    FoodUI()
    return OpenUI()

  if key == 'n' or key =='N':
    createorder()
    return OpenUI()
# Coffee Section
def CoffeeUI():
  global n
  print(n)
  print(l)
  while True: # Loop in CoffeeUI
    #print(order)
    print('#'*29,' Pang Pone POS SYS ','#'*30) # Header
    print('# Menu Coffee'+(' '*26) + '|' + ' Order'+(' '*33+'#'))

    # Loop for display order and menu
    for i in range(len(Coffee.lolc)):
      try:
        x = 39
        print('# '+'{}.'.format(i+1) + Coffee.lolc[i] + ' '*(x - len(Coffee.lolc[i])-3-len(str(i+1)))+'| '+
              '{}.'.format(i+1)+ order[n][i][0] + ' '*(x - len(order[n][i][0])-len(str(i+1))-2) + '#')
      except IndexError:
        print('# '+'{}.'.format(i+1) + Coffee.lolc[i] + ' '*(x - len(Coffee.lolc[i])-3-len(str(i+1)))+'|' +
              ' '*39+'#')

  # Interface input
    print('# "E,e":go to mainmenu "C,c":to begin order "D,d":to del the order',' '*12+'#')
    print('# What would you like to do?',' '*50+'#')
    print('#'*80)

    decision = input()

    if decision == 'E' or decision == 'e':
      break

    if decision == 'D' or decision == 'd':
      deleteorder()

    if decision == 'C' or decision == 'c':

      listcoffee = []
      # Loop for order
      while True:

        print('#'*29,' Pang Pone POS SYS ','#'*30) # Header
        print("# Everything 25 Baht",' '*58+'#')
        print('# Choose the number you want.',' '*49+'#')

        # Loop for display selectionable
        for i in range(Coffee.Coffee.no_coffee):
          x = 80
          # Print the order with Text-base durable
          print('# {}.'.format(i+1) + Coffee.c[i].name + ' '*(x - len(Coffee.c[i].name) - len(str(i+1)) - 4) + '#')

        print('#'+' '*78 +'#')

        if listcoffee!= []:
          print('# You have selected.',' '*58+'#')

          for i in range(len(listcoffee)):
            print('# {}.'.format(i+1),listcoffee[i],' '*(74-len(listcoffee[i])-len(str(i+1)))+'#')

        for i in range(18-Coffee.Coffee.no_coffee-len(listcoffee)):
          print('#'+' '*78 +'#')

        # Interface Input
        print('# Press "0" to exit.',' '*58+'#')
        print('# What would you like?',' '*56+'#')
        print('#'*80)
        choice = int(input())

        if choice == 0:
          break

        # Add the selection to current order
        order[n][l].append(Coffee.c[choice-1].name)
        order[n][l].append(25)
        listcoffee.append(Coffee.c[choice-1].name)
        # print(l)
        createlist()
        #print(order)

def BeverageUI():
  while True: # Loop in BeverageUI
    print('#'*29,' Pang Pone POS SYS ','#'*30) # Header
    print('# Menu Beverage'+(' '*24) + '|' + ' Order'+(' '*33+'#'))

    # Loop for display order and menu
    for i in range(len(Beverage.lolb)):
      try:
        x = 39
        print('# '+'{}.'.format(i+1) + Beverage.lolb[i] + ' '*(x - len(Beverage.lolb[i])-3-len(str(i+1)))+'| '+
              '{}.'.format(i+1)+order[n][i][0] + ' '*(x - len(order[n][i][0])-len(str(i+1))-2) + '#')
      except IndexError:
        print('# '+'{}.'.format(i+1) + Beverage.lolb[i] + ' '*(x - len(Beverage.lolb[i])-3-len(str(i+1)))+'|' +
              ' '*39+'#')

    # Interface input
    print('# "E,e":go to mainmenu "C,c":to begin order "D,d":to del the order',' '*12+'#')
    print('# What would you like to do?',' '*50+'#')
    print('#'*80)

    decision = input()

    if decision == 'E' or decision == 'e':
      break

    if decision == 'D' or decision == 'd':
      deleteorder()

    if decision == 'C' or decision == 'c':

      listbeverage = []
      # Loop for order
      while True:

        print('#'*29,' Pang Pone POS SYS ','#'*30) # Header
        print("# All of the prices are in THB",' '*48+'#')
        print('# Choose the number you want.',' '*49+'#')

        # Loop for display selectionable
        for i in range(Beverage.Beverage.no_beverage):
          x = 80
          # Print the order with Text-base durable
          print('# {}.'.format(i+1) + Beverage.b[i].name + ' '*(x - len(Beverage.b[i].name) - len(str(i+1)) - 4) + '#')

        print('#'+' '*78 +'#')

        if listbeverage!= []:
          print('# You have selected.',' '*58+'#')

          for i in range(len(listbeverage)):
            print('# {}.'.format(i+1),listbeverage[i],' '*(74-len(listbeverage[i])-len(str(i+1)))+'#')

        for i in range(18-Beverage.Beverage.no_beverage-len(listbeverage)):
          print('#'+' '*78 +'#')

        # Interface input
        print('# Press "0" to exit.',' '*58+'#')
        print('# What would you like?',' '*56+'#')
        print('#'*80)
        choice = int(input())

        if choice == 0:
          break

        # Add the selection to current order
        order[n][l].append(Beverage.b[choice-1].name)
        order[n][l].append(int(Beverage.b[choice-1].price))
        listbeverage.append(Beverage.b[choice-1].name)
        #print(l)
        createlist()
        #print(order[n])

def FoodUI():
  while True: # Loop in FoodUI
    print('#'*29,' Pang Pone POS SYS ','#'*30)
    print('# Menu Food'+(' '*28) + '|' + ' Order'+(' '*33+'#'))

    # Loop to display order and menu
    for i in range(len(Food.lolf)):
      try:
        x = 39
        print('# '+'{}.'.format(i+1) + Food.lolf[i] + ' '*(x - len(Food.lolf[i])-3-len(str(i+1)))+'| '+
              '{}.'.format(i+1)+order[n][i][0] + ' '*(x - len(order[n][i][0])-len(str(i+1))-2) + '#')
      except IndexError:
        print('# '+'{}.'.format(i+1) + Food.lolf[i] + ' '*(x - len(Food.lolf[i])-3-len(str(i+1)))+'|' +
              ' '*39+'#')

    # Interface the input
    print('# "E,e:go to mainmenu "C,c":to begin order "D,d":to del the order',' '*12+'#')
    print('# What would you like to do?',' '*50+'#')
    print('#'*80)

    decision = input()

    if decision == 'E' or decision == 'e':
      break

    if decision == 'D' or decision == 'd':
      deleteorder()

    if decision == 'C' or decision == 'c':

      listfood = []
      # Loop for order
      while True:
        print('#'*29,' Pang Pone POS SYS ','#'*30)
        print("# All of the prices are in THB",' '*48+'#')
        print('# Choose the number you want.',' '*49+'#')

        # Loop for display selectionable
        for i in range(Food.Food.no_food):
          x = 80
          # Print the order with Text-base durable
          print('# {}.'.format(i+1) + Food.f[i].name + ' '*(x - len(Food.f[i].name) - len(str(i+1)) - 4) + '#')

        print('#'+' '*78 +'#')

        if listfood!= []:
          print('# You have selected.',' '*58+'#')

          for i in range(len(listfood)):
            print('# {}.'.format(i+1),listfood[i],' '*(74-len(listfood[i])-len(str(i+1)))+'#')

        for i in range(18-Food.Food.no_food-len(listfood)):
          print('#'+' '*78 +'#')

        # Interface Input
        print('# Press "0" to exit.',' '*58+'#')
        print('# What would you like?',' '*56+'#')
        print('#'*80)
        choice = int(input())

        if choice == 0:
          break

        # Add the selection to current order
        order[n][l].append(Food.f[choice-1].name)
        order[n][l].append(int(Food.f[choice-1].price))
        listfood.append(Food.f[choice-1].name)
        #print(l)
        createlist()
        #print(order[n])
      # print(order[n])

def deleteorder():
  global l
  # Funtion to delete the current order
  del order[n][l-1]
  l -= 1
  #print(order)

OpenUI()

