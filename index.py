class Product:
    def __init__(self, title, calorific, cost):
        if calorific <= 0:
            raise ValueError('Калорийность должна быть больше 0')
        elif cost <= 0:
            ValueError('Себестоимость должна быть больше 0')
        else:
            self.title = title
            self.calorific = calorific
            self.cost = cost


class Ingredient():
    def __init__(self, product, weight):
        if weight <= 0:
            raise ValueError('Вес должен быть больше 0')
        else:
            self.product = Product
            self.weight = weight

    def get_calorific(self):
        return self.weight / 100 * self.calorific

    def get_cost(self):
        return self.weight / 100 * self.cost


class Pizza (Ingredient):
    def __init__(self, title, ingredients):
        if not title:
            raise ValueError('Название пиццы не может быть пустым')
        else:
            self.title = title
            self.ingredients = ingredients


# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты.
# Для каждого ингредиента указываем продукт, из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)

# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])
pizza_margarita_light = Pizza('Маргарита', [dough_ingredient, cheese_ingredient])

# Выводим экземпляр пиццы
print(pizza_margarita)
print(pizza_margarita_light)
