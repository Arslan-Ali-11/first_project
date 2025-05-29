product_store = {
          "apple":[200,15],
          "banana":[150,12],
          "mangoes":[100,5]
    }
def product_catalog():
  for product,(price,stock) in product_store.items():
    print(f"{product.capitalize()}  Price {price},  in stock {stock}")

def adding_value():
  product_name = input("enter the product name:").lower()
  price = int(input("enter the price:"))
  stock = int(input("enter the stock:"))

  product_store[product_name] = [
      price,stock
  ]

def user_purchase():
  user_purchase_item = input("enter the product name:").lower()

  if user_purchase_item in product_store :
    user_purchase_quantity = int(input("enter the quantity:"))
    available_stock = product_store[user_purchase_item][1]
    if user_purchase_quantity <= available_stock:
        bill = product_store[user_purchase_item][0] * user_purchase_quantity
        print(bill)
    else:
            print(f"Sorry, only {available_stock} {user_purchase_item}(s) are available in stock.\n")
  else:
        print(f"Product '{user_purchase_item.capitalize()}' not found in our catalog.\n")


while True:
 print("""
Welcome to the Smart Grocery Store Assistant
1. View Products
2. Add/Update Product
3. Purchase Items
4. Exit
""")
  user_number = int(input("Enter the number:"))
  if user_number == 1:
    product_catalog()
  elif user_number == 2:
    adding_value()
  elif user_number == 3:
    user_purchase()
  elif user_number == 4:
    print("exit")
    break
  else:
    print("invalid input")
