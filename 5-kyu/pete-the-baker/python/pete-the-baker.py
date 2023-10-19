def cakes(recipe, available):
    div_ingredients = {}
    for recipe_ingredient in recipe.keys():
        if recipe_ingredient not in available.keys():
            return 0
        
        if available[recipe_ingredient] < recipe[recipe_ingredient]:
            return 0
        
        div_ingredients[recipe_ingredient] = available[recipe_ingredient] / recipe[recipe_ingredient]
    return int(min(div_ingredients.values()))