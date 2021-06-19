import numpy as np
from collections import namedtuple


def makeDishList(theList, customer):
    return [x[1] for x in theList if x[0] == customer]


def quantityByDish(theList, customer):
    Orders = namedtuple('Orders', ['food', 'quantity'])
    dishList = [order[1] for order in theList]
    if customer:
        dishList = makeDishList(theList, customer)
    dishes = np.unique(dishList)
    orders = [Orders(dish, dishList.count(dish)) for dish in dishes]
    return orders


def makeDaysList(theList, customer):
    return [x[2] for x in theList if x[0] == customer]


class TrackOrders:
    theList = []

    def __len__(self):
        return len(self.theList)

    def add_new_order(self, customer, order, day):
        self.theList = [*self.theList, [customer, order, day]]
        return self.theList

    def get_most_ordered_dish_per_costumer(self, customer):
        orders = quantityByDish(self.theList, customer)
        maxQty = max([order.quantity for order in orders])
        return [order.food for order in orders if order.quantity == maxQty][0]

    def get_order_frequency_per_costumer(self, customer, order):
        orders = quantityByDish(self.theList, customer)
        return [ord.quantity for ord in orders if ord.food == order][0]

    def get_never_ordered_per_costumer(self, customer):
        dishes = np.unique([x[1] for x in self.theList])
        dishesConsumed = np.unique(makeDishList(self.theList, customer))
        neverAsked = set(x for x in dishes if x not in dishesConsumed)
        return neverAsked

    def get_days_never_visited_per_costumer(self, customer):
        days = np.unique([x[2] for x in self.theList])
        daysVisited = makeDaysList(self.theList, customer)
        daysVisited = np.unique(daysVisited)
        return set(day for day in days if day not in daysVisited)

    def get_busiest_day(self):
        Visit = namedtuple('Visit', ['day', 'quantity'])
        days = [x[2] for x in self.theList]
        visits = [Visit(day, days.count(day)) for day in np.unique(days)]
        most = max(visit.quantity for visit in visits)
        return [visit.day for visit in visits if visit.quantity == most][0]

    def get_least_busy_day(self):
        Visit = namedtuple('Visit', ['day', 'quantity'])
        days = [x[2] for x in self.theList]
        visits = [Visit(day, days.count(day)) for day in np.unique(days)]
        less = min(visit.quantity for visit in visits)
        return [visit.day for visit in visits if visit.quantity == less][0]

    def totalOrderedOfEachDish(self):
        totalOrders = quantityByDish(self.theList, None)
        return totalOrders
