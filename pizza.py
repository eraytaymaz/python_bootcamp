import csv
import datetime

class Pizza:
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description

class Classic(Pizza):
    cost = 5
    description = "Klasik Pizza"

class Margherita(Pizza):
    cost = 10
    description = "Margherita Pizza"

class Turkish(Pizza):
    cost = 15
    description = "Türk Pizzası"

class Dominos(Pizza):
    cost = 20
    description = "Dominos Pizzası"

class Decorator(Pizza):
    pass

class Olive(Decorator):
    cost = 1
    description = "Zeytin"

class Mushroom(Decorator):
    cost = 2
    description = "Mantar"

class Cheese(Decorator):
    cost = 3
    description = "Keçi Peyniri"

class Meat(Decorator):
    cost = 4
    description = "Et"

class Onion(Decorator):
    cost = 5
    description = "Soğan"

class Corn(Decorator):
    cost = 6
    description = "Mısır"

def get_cost(a, b):
    return Pizza.get_cost(a) + Pizza.get_cost(b)

def get_description(a, b):
    return Pizza.get_description(a) + " " + Pizza.get_description(b)

def main():
    with open ("Menü.txt", "r") as f:
        for line in f:
            print(line, end="")
    print()
    f.close()
    
    pizza_no = int(input("Pizza seçiniz:"))
    decorator_no = int(input("Sos seçiniz:"))
    name = input("Ad Soyad:")
    id = input("TC Kimlik:")
    credit_card = input("Kredi Kartı:")
    password = input("Şifre:")
    
    pizza = Pizza
    decorator = Decorator
    if pizza_no == 1:
        pizza = Classic
    elif pizza_no == 2:
        pizza = Margherita
    elif pizza_no == 3:
        pizza = Turkish
    elif pizza_no == 4:
        pizza = Dominos
    
    if decorator_no == 11:
        decorator = Olive
    elif decorator_no == 12:
        decorator = Mushroom
    elif decorator_no == 13:
        decorator = Cheese
    elif decorator_no == 14:
        decorator = Meat
    elif decorator_no == 15:
        decorator = Onion
    elif decorator_no == 16:
        decorator = Corn

    print("Ödeyeceğiniz Fiyat:" + str(get_cost(pizza, decorator)))
    print("Seçtiğiniz Pizza:" + get_description(pizza, decorator))

    data = (name, id, credit_card, password, get_description(pizza, decorator), datetime.datetime.now())
   
    with open ("Orders_Database.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter="\t")
        writer.writerow(data)
    csv_file.close()

if __name__ == "__main__":
    main()
