products = [
    {"name": "Pen", "stock": 15},
    {"name": "Notebook", "stock": 8},
    {"name": "Pencil", "stock": 5},
    {"name": "Eraser", "stock": 12},
    {"name": "Marker", "stock": 6}
]

print("Products with stock less than 10:\n")

for product in products:
    if product["stock"] < 10:
        print("Product:", product["name"])
        print("Stock:", product["stock"])
        print()