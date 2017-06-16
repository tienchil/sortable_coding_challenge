import json

from pprint import pprint

def load_json(filename):
    # Loading the data into a list
    data = []
    with open(filename) as data_file:
        for line in data_file:
            data.append(json.loads(line))

    return data

# Loading the data into a list
products_data = load_json("./data/products.txt")
listings_data = load_json("./data/listings.txt")

print(len(products_data))
print(len(listings_data))
pprint(products_data[0])

# Display products info
manufacturer = {}
for product in products_data:
    manu = product["manufacturer"]
    if manu not in manufacturer:
        manufacturer[manu] = 1
    else:
        manufacturer[manu] += 1

pprint(manufacturer)

# Create Objects for Products, Listings, Results