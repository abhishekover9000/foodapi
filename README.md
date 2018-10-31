# foodapi

1 navigate to healthynom folder
2 Make a fresh virtualenv
3 pip install -r requirements.txt
4 to start the server run "python manage.py runserver"

```
POST /recipes/
{
    "recipeName": "test recipe",
    "recipeInstructions": "you gotta, do stuff, then do, other stuff",
    "ingredients": [
        {
            "ingredient_name": "Gravy, chicken, canned or bottled, ready-to-serve",
            "ndbid": 6119,
            "amount": 12,
            "measurement": "oz"
        },
        {
            "ingredient_name": "Spinach, raw",
            "ndbid": 11457,
            "amount": 2,
            "measurement": "lbs"
        }
    ]
}
```
```
DELETE/recipes/1/
http 200 OK
```
```
DELETE /recipes/1/ingredients/1/
http 200 OK
```

