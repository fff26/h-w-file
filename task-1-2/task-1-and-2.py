from pprint import pprint

class Menu:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_menu(self):
        with open(self.filepath, 'rt', encoding='utf-8') as file:
            dishes = {}
            while True:
                dish_name = file.readline().strip()
                if not dish_name:
                    break
                num_ingredients = int(file.readline())
                ingredients = []
                for i in range(num_ingredients):
                    ingredient_line = file.readline().strip()
                    ingredient_name, quantity, measure = ingredient_line.split(' | ')
                    ingredients.append({
                        'ingredient_name': ingredient_name,
                        'quantity': int(quantity),
                        'measure': measure
                    })
                dishes[dish_name] = ingredients
                # Пропускаем пустую строку после блюда
                file.readline()
        return dishes
menu = Menu('data.txt')
dishes = menu.read_menu()
pprint(dishes)

def get_shop_list_by_dishes(dishes, person_count):
    menu = Menu('data.txt')
    all_ingredients = {}
    for dish_name in dishes:
        ingredients = menu.read_menu()[dish_name]
        for ingredient in ingredients:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            if ingredient_name in all_ingredients:
                all_ingredients[ingredient_name]['quantity'] += quantity
            else:
                all_ingredients[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return all_ingredients
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
result = get_shop_list_by_dishes(dishes, person_count)
print(result)