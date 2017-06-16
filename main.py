"""

Sortable Coding Challenge

Please refer to https://sortable.com/challenge/ for more details


"""


from util import Product, Listing, Result, print_objects
from parse import load_json

if __name__ == "__main__":

    # Load the JSON file into a list of dictionary
    products_data = load_json("./data/products.txt")
    listings_data = load_json("./data/listings.txt")

    # Create objects for each listing and product
    products = [Product(p) for p in products_data]
    listings = [Listing(li) for li in listings_data]

    print_objects(listings[:10])
    print("------------")
    print_objects(products[:10])


