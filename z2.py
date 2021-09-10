from pprint import pprint
def prepare_dict(file_name):
    cook_book = {}
    with open(file_name,"r", encoding="utf-8") as file:
        for line in file:
            dish = line.strip()
            quantity_ingre = int(file.readline())
            dish_list = []
            for ingre in range(quantity_ingre):
                ingredient_name, quantity, measure = file.readline().split("|")
                dish_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
            cook_book[dish] = dish_list
            file.readline()
    return cook_book
# file_path = os.path.join(os.getcwd(), "cook_book.txt")
# print(prepare_dict(file_path))
cook_book = prepare_dict("cook_book")
# print(cook_book)
def get_shop_list_by_dishes(dishes, person_count):
    ingre_list = {}
    for dish in dishes:
        list_ = {}
        for ingre in cook_book[dish]:
            list_ = {"measure": ingre["measure"].strip(), "quantity": int(ingre["quantity"])*person_count}
            ingre_list[ingre["ingredient_name"]] = list_
    return ingre_list
pprint(get_shop_list_by_dishes(["Омлет", "Запеченный картофель"], 2))

