# You should create classes to represent each of the following parts of our model:
#
# 1. Bicycle
# Have a model name
# Have a weight
# Have a cost to produce
# 2. Bike Shops
# Have a name
# Have an inventory of different bicycles
# Sell bicycles with a margin over their cost
# Can see how much profit they have made from selling bikes
# 3. Customers
# Have a name
# Have a fund of money to buy a bike
# Can buy and own a new bicycle

# The code should:
#
# Create a bicycle shop that has 6 different bicycle models in stock.
# The shop should charge its customers 20% over the cost of the bikes.
# Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
# Print the name of each customer, and a list of the bikes offered by the bike shop
# that they can afford given their budget. Make sure you price the bikes
# in such a way that each customer can afford at least one.

# Print the initial inventory of the bike shop for each bike it carries.
# Have each of the three customers purchase a bike
# then print the name of the bike the customer purchased, the cost, and
# how much money they have left over in their bicycle fund.
# After each customer has purchased their bike, the script should print out
# the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.

class Bicycle(object):
    def __init__(self, id, model_name, weight, production_cost):
        self.id = id
        self.model_name = model_name
        self.weight = weight
        self.production_cost = production_cost

    # Accessor Methods (Getters)
    def get_id(self):
        return self.id

    def get_model_name(self):
        return self.model_name

    def get_weight(self):
        return self.weight

    def get_production_cost(self):
        return self.production_cost

bicycle_1 = Bicycle(1, 'Avon', 15, 200)
bicycle_2 = Bicycle(2, 'Hercules', 14, 250)
bicycle_3 = Bicycle(3, 'Atlas', 12, 300)
bicycle_4 = Bicycle(4, 'Barbie', 13, 150)
bicycle_5 = Bicycle(5, 'Hero', 10, 520)
bicycle_6 = Bicycle(6, 'Pacific', 12, 750)

bikes_lst = [bicycle_1, bicycle_2, bicycle_3, bicycle_4, bicycle_5, bicycle_6]
bike_id_lst = [1, 2, 3, 4, 5, 6]

bicycle_dict = {}
for key, value in zip(bike_id_lst, bikes_lst):
    bicycle_dict[key] = value

class Bike_shop(object):
    def __init__(self, shop_name, bicycle_dict):
        self.shop_name = shop_name
        self.bicycle_dict = bicycle_dict

    def sell(self, bike_id_num):
        cost_price = bicycle_dict[bike_id_num].production_cost
        profit = 0.20 * cost_price
        selling_price = cost_price + profit
        return selling_price

bike_shop = Bike_shop('Bicycle_vendors', bicycle_dict)

class Customer(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund

    def buy(self, expenditure):
        self.fund = self.fund - expenditure
        return self.fund

    def can_afford(self, bike):
        return self.fund >= bike.get_production_cost()

customer_1 = Customer('Arnab', 200)
customer_2 = Customer('Pran', 500)
customer_3 = Customer('Shrey', 1000)

customer_lst = [customer_1, customer_2, customer_3]

def main():
    """
    Print the name of each customer, and a list of the bikes offered by the bike shop
    that they can afford given their budget.
    """
    import random
    purchase_bike_id = [] # Randomly choses one bicycle that a customer decides to purchase
    for i in customer_lst:
        affordable_bikes = [] # Each customer can afford bicycles contained in this list
        for j in bikes_lst:
            if i.can_afford(j): # Fund >= Bike's cost
                affordable_bikes.append(j.id)

        print ('Customer {} can afford {} bicycle'.format(i.name, affordable_bikes))
        purchase_bike_id.append(random.choice(affordable_bikes))

    print bike_shop.bicycle_dict # Print the initial inventory of the bike shop for each bike it carries.
    print purchase_bike_id # Bicycle id that 3 customers want to purchase

    # Have each of the three customers purchase a bike
    # then print the name of the bike the customer purchased, the cost, and
    # how much money they have left over in their bicycle fund.

    for i in range(3):
        print ("{} has purchased {} bike costing him {} "
               "and the now he/she has {} money left in the bicycle fund"
               . format(customer_lst[i], # ith customer
                        bicycle_dict[purchase_bike_id[i]].model_name, # Model Name of purchased bicycle
                        bike_shop.sell(purchase_bike_id[i]), # Selling price of the bicycle
                        customer_lst[i].buy(bike_shop.sell(purchase_bike_id[i])) # Balance = Fund - Selling price
        ))

main()



