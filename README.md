# foodapi

>navigate to healthynom folder
>enter venv (python 3.6)


to start the server run "python manage.py runserver"

supplier resource is available at /supplier,
example create call:
POST {
        "name": "SuperValu"
    }


ingredient resource is available at /inventory,

example create call:
POST {
        "name": "Milk, Whole",
        "inventory": {
            "costPerGram": 0.003,
            "remainingQuantity": 0,
            "ndbid": 45282044,
            "supplied_by": {
                "name": "Walmart"
            }
        }
    }
example update, supply an ID
POST
{
    "id": 40,
    "name": "Milk, 2%",
    "inventory": {
        "costPerGram": 0.003,
        "remainingQuantity": 0,
        "ndbid": 45226447,
        "supplied_by": {
            "name": "Walmart"
        }
    }
}



Recipe resource is available at /recipe,
example create 
POST {
        "name": "test333",
        "steps": "Preheat oven to 400 F. Season chicken cubes with salt, pepper and 1 teaspoon herbes de Provence. /n Heat Olive oil in a larg pan over high heat. Working in batches, brown chicken for 2 minutes per side or until lightly browned and almost cooked through. Remove to an ovenproof baking dish and reserve/n Add ham, onions, zucchini garlic and remaining herbes de provence into the pan and saute until vegetables are browned and tender. Add wine and bring to a boil, then add tomatoes, stock, olives, and bay leaf and bring to a boil. Simmer for about 2 minutes, then pour over chicken, Season with salt and pepper to taste/n Bake for 15 minutes or until chicken is cooked through."
    }
    
for now ingredients need to be added to a recipe after the recipe is created
to add an ingredient simply format this request to take in the correct values
    
    POST /recipe
    {
                "ingredient": 36,
                "recipe": 3,
                "quantityInGrams": 800
            }
