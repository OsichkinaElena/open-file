import os
def prepare_dict(file_name):
    cook_book = {}
    with open(file_name,"r", encoding="utf-8" ) as file:
        for line in file:
            dish = line.strip()
            quantity_ingre = int(file.readline())
            dish_list = []
            for ingre in range(quantity_ingre):
                ingredient_name, quantity, measure = file.readline().split("|")
                dish_list.append({"ingredient_name": ingredient_name, "quantity":int(quantity) , "measure": measure.strip()})
            cook_book[dish] = dish_list
            file.readline()
    return cook_book
cook_book = prepare_dict("cook_book")
print(cook_book)