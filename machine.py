class Money:

    def __init__(self, money=0):
        self._money = money

    def get_money(self):
        return self._money

    def add_money(self, cost):
        self._money += cost


class Menu:

    def __init__(self, water=0, milk=0, coffee=0, cost=0):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost
