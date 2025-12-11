foods = ["apple", "banana", "carrot", "dates", "eggplants", "fraises"]

while True:
    query = input("Search List: ")

    if query not in foods:
        foods.append(query)
        print("Missing from list\nAdding to list")
    else:
        print(f"Found: {query}")

