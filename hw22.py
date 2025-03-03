#Name: CJ Nickson
#Class: 6th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class StoreItem:
    def __init__(self, stock, cost, weight):
        # Initializing attributes
        self.stock = stock
        self.cost = cost
        self.weight = weight

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
item1 = StoreItem(50, 10.99, 1.2)
item2 = StoreItem(30, 5.49, 0.8)
item3 = StoreItem(100, 15.99, 2.5)

#3. Print the stock of all three objects and the cost of the second store item.
print("Stock of item1:", item1.stock)
print("Stock of item2:", item2.stock)
print("Stock of item3:", item3.stock)

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
def double_cost(self):
    # Doubling the cost of the item
    self.cost *= 2
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
print("\nCost of item2:", item2.cost)
print("\nNew cost of item2 after doubling:", item2.cost)
item3.stock = int(item3.stock / 4)
print("\nNew stock of item3:", item3.stock)

#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del item1
try:
    print("\nWeight of item1:", item1.weight)
except NameError:
    print("\nError: item1 has been deleted and no longer exists.")
