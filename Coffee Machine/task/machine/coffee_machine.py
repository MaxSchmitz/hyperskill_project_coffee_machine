# Write your code here
def get_action():
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    return action


class CoffeeMachine:
    def __init__(self, money, water, milk, beans, cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.coffee = {"espresso": {"w": 250, "m": 0, "b": 16, "price": 4},
                       "latte": {"w": 350, "m": 75, "b": 20, "price": 7},
                       "cappuccino": {"w": 200, "m": 100, "b": 12, "price": 6}}

    def __str__(self):
        return f"""The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.beans} of coffee beans
        {self.cups} of disposable cups
        {self.money} of money
        """

    def get_coffee(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        user_input = input()
        try:
            selection = int(user_input) - 1
        except ValueError:
            selection = None
            # print('u suk')
        coffee_type = ["espresso", "latte", "cappuccino"]
        if user_input == 'back':
            pass
        elif self.enough_resources(coffee_type[selection]) is True:
            print("I have enough resources, making you a coffee!")
            # print(coffee[coffee_type[selection-1]]["w"])
            self.water -= self.coffee[coffee_type[selection]]["w"]
            self.milk -= self.coffee[coffee_type[selection]]["m"]
            self.beans -= self.coffee[coffee_type[selection]]["b"]
            self.money += self.coffee[coffee_type[selection]]["price"]
            self.cups -= 1
        else:
            print(f"Sorry, not enough {self.enough_resources(coffee_type[selection])}!")
        pass

    def fill(self):
        print('Write how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.beans += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(input())
        pass

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def enough_resources(self, coffee_type):
        if self.water < self.coffee[coffee_type]['w']:
            return "water"
        elif self.milk < self.coffee[coffee_type]['m']:
            return "milk"
        elif self.beans < self.coffee[coffee_type]['b']:
            return "beans"
        elif self.cups == 0:
            return "cups"
        else:
            return True

    def main_menu(self):
        choice = get_action()
        if choice == "buy":
            self.get_coffee()
        elif choice == "fill":
            self.fill()
        elif choice == "take":
            self.take()
        elif choice == "remaining":
            print(self)
        elif choice == "exit":
            exit()


cafe = CoffeeMachine(550, 400, 540, 120, 9)
while True:
    cafe.main_menu()


