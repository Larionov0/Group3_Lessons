import requests
from typing import List


class Drink:
    def __init__(self, name, category, strAlcoholic, instructions, ingredients, img_src):
        self.name = name
        self.category = category
        self.is_alcoholic = strAlcoholic
        self.instructions = instructions
        self.ingredients = ingredients
        self.img_src = img_src

    def __str__(self):
        return f"{self.name} ({self.ingredients})"


class CocktailManager:
    BASE_URL = 'https://www.thecocktaildb.com/api/json/v1/1/search.php'

    def __init__(self):
        pass

    def get_api_drinks(self, search_string) -> List[dict]:
        data = requests.get(self.BASE_URL, params={'s': search_string}).json()
        if data['drinks'] is None:
            return []
        return data['drinks']

    def convert_drink(self, drink_from_api) -> Drink:
        ingredients = []
        n = 1
        while True:
            ingr = drink_from_api[f'strIngredient{n}']
            if ingr is None:
                break
            else:
                ingredients.append(ingr)
            n += 1

        drink = Drink(
            name=drink_from_api['strDrink'],
            category=drink_from_api['strCategory'],
            instructions=drink_from_api['strInstructions'],
            strAlcoholic=drink_from_api['strAlcoholic'],
            ingredients=ingredients,
            img_src=drink_from_api['strDrinkThumb']
        )
        return drink

    def get_drinks(self, search_string) -> List[Drink]:
        api_drinks = self.get_api_drinks(search_string)
        drinks = []
        for api_drink in api_drinks:
            drink = self.convert_drink(api_drink)
            drinks.append(drink)
        return drinks


# c_m = CocktailManager()
# data = c_m.get_drinks('margar')
#
# for drink in data:
#     print(drink)
