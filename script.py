# Len's Slice: I work at Len’s Slice, a new pizza joint in the neighborhood. I am going to use my knowledge of Python lists to organize some of the sales data.
print("Sales Data")
# To keep track of the kinds of pizzas sold, a list is created called toppings that holds different toppings.
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
# A list called "prices" is created to track how much each pizza costs.
prices = [2, 6, 1, 3, 2, 7, 2]
len(toppings)
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizzas = list(zip(prices, toppings))
print(pizzas)

