
# drinks = ["Water", "Coffee", "Tea", "Cola", "Pepsi", "Root Beer", "Beer", "Wine"]

food_list = []

class color:
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'


class Food_item:

  def __init__(self, name, food_type, price, calories):

    self.name = name
    self.food_type = food_type
    self.price = price 
    self.calories = calories

# for x in range (len(drinks)):

appetizers = [("cheese tray", 4.99, 1000), ("salad", 4.50, 150), ("fruit bowl", 3.99, 100), ("french fries", 3.99, 800), ("cheesy garlic bread", 6.99, 900), ("shrimp", 6.99, 800), ("stuffed mushrooms", 5.99, 700)]
for dish in appetizers:
  food_list.append(Food_item(dish[0], "Appetizer", dish[1], dish[2]))

main_courses = [("pizza", 7.99, 1000), ("hamburger", 5.99, 1200), ("pasta", 5.99, 800), ("pbj", 2.50, 300), ("naan", 3.99, 600), ("rice bowl", 3.99, 300), ("sushi", 7.99, 500)]
for dish in main_courses:
  food_list.append(Food_item(dish[0], "Main Course", dish[1], dish[2]))

drinks = [("soda", 1.99, 250), ("water", 2.50, 50), ("smoothie", 4.99, 600), ("coffee", 2.99, 200), ("tea", 1.99, 100), ("milk shake", 2.99, 400), ("beer", 4.99, 200), ("wine", 6.99, 250), ("slushie", 2.99, 600)]
for dish in drinks:
  food_list.append(Food_item(dish[0], "Drink", dish[1], dish[2]))

desserts = [("ice cream", 3.99, 600), ("pudding", 3.99, 700), ("cookies", 4.99, 1000), ("freezie box", 4.99, 700), ("cupcakes", 4.99, 1200), ("donuts", 4.99, 1200), ("cake", 9.99, 1700), ("muffin", 4.99, 1200), ("ice cream cake", 12.99, 2000)]
for dish in desserts:
  food_list.append(Food_item(dish[0], "Dessert", dish[1], dish[2]))


class Menu:

  def __init__(self, food_list):
    self.food_list = food_list

  def print_header(self, string):

    print(color.RED + color.BOLD + color.UNDERLINE + string + ":" + color.END)
    print("")

  def space(self):
    print("")
    print("")

  def food_identifier(self, food_string):
    for x in range (len(food_list)):
      food_item = food_list[x-1]
      if food_item.food_type == food_string:
        price_tag = "${:.2f}".format(food_item.price)
        num_dots = 50 - len(food_item.name) - len(price_tag)

        print(food_item.name, '.'*num_dots, price_tag)

  def display(self):

    self.print_header("Appetizers")
    self.food_identifier("Appetizer")
    self.space()

    self.print_header("Main Courses")
    self.food_identifier("Main Course")
    self.space()

    self.print_header("Drinks")
    self.food_identifier("Drink")
    self.space()

    self.print_header("Desserts")
    self.food_identifier("Dessert")
    self.space()



class Bill:

  #Constructor
  def __init__(self):

    self.bill = []
    self.bill_total = []
    self.order_amount = []

    # if food_choice in food_list:

    #   self.Food_item = Food_choice
    #   print(Food_item)

  def add_item(self, food, amount):
    #Add an item the bill
    self.order_amount.append(int(amount))
    self.bill.append(food.name)
    self.bill_total.append(amount*food.price)

  def print_bill(self):
    print("")
    print("")
    print("")
    print("BILL")
    print("")
    for i in range(len(self.bill)):
      #for food in self.bill):
      print("{} x {}.........................${:.2f}".format(self.order_amount[i], self.bill[i], self.bill_total[i]))
      print("")
      # print(self.order_amount[i], "X ", self.bill[i]," .... ", self.bill_total[i])
        
     
  
  def gets_total(self):
    total = 0.0
    for i in range (len(self.bill_total)):
      total += (self.bill_total[i])
    
    total = round(total, 2)
    print("Subtotal........................ $", total)
    tax = round((total*0.13), 2)
    total *= 1.13
    total = round(total, 2)
    print("Tax............................. $", tax)
    print("Total........................... $", total)




# Main

print("")
print(color.DARKCYAN + 'Welcome to the Extremely Healthy Reataurant!' + color.END)
print("")
print("")

user_order = []
menu = Menu(food_list)
menu.display()

the_bill = Bill()

order = input("Would you like to make an order? (Y/N): ").lower()

while order == "y":

  choice_name = input("What would you like to order?")
  for food in food_list:
    if(food.name == choice_name.lower()):
      amount = int(input("How many would you like to order?"))
      print("")
      the_bill.add_item(food, amount)
      break;
  
  order = input("Would you like to order another item? (Y/N): ").lower()

the_bill.print_bill()
the_bill.gets_total()
    

# ENTRY_SIZE = FOOD_NAME + DOTS + PRICE_SIZE

# DOTS = ENTRY_SIZE - FOOD_NAME - PRICE_SIZE
  
