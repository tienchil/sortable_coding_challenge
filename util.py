class Product:
    # Definition of a product object
    def __init__(self, product_dict):
        self.product_name = product_dict["product_name"]
        self.manufacturer = product_dict["manufacturer"]
        self.family = product_dict.get("family")
        self.model = product_dict["model"]
        self.announced_date = product_dict["announced-date"]

    def __str__(self):
        return self.product_name

    def display(self):
        """Display detailed information about the product"""
        name = "Product Name: {}\n".format(self.product_name)
        man = "Manufacturer: {}\n".format(self.manufacturer)
        fam = "Family: {}\n".format(self.family)
        model = "Model: {}\n".format(self.model)
        date = "Announced Date: {}\n".format(self.announced_date)

        print(name+man+fam+model+date)


class Listing:
    # Definition of a listing object
    def __init__(self, listing_dict):
        self.title = listing_dict["title"]
        self.manufacturer = listing_dict["manufacturer"]
        self.currency = listing_dict["currency"]
        self.price = listing_dict["price"]

    def __str__(self):
        return self.title

    def display(self):
        """Display detailed information about the listing"""
        title = "Title: {}\n".format(self.title)
        man = "Manufacturer: {}\n".format(self.manufacturer)
        currency = "Currency: {}\n".format(self.currency)
        price = "Price: {}$ {}\n".format(self.currency, self.price)

        print(title+man+currency+price)

class Result:
    # Definition of a Result object
    def __init__(self, product_name, listings=[]):
        self.product_name = product_name
        self.listings = listings # A list of Listing objects

    def __str__(self):
        return "{} with {} listings".format(self.product_name, 
                                             len(self.listings))

    def add_listing(self, listing):
        """Add a Listing item into listings"""
        self.listings.append(listing)

    def display(self):
        print("Product Name: {}\n".format(self.product_name))
        for i, li in enumerate(self.listings):
            print(i+1)
            li.display()




def print_objects(obj_list):
    for obj in obj_list:
        print(obj)
        obj.display()


if __name__ == "__main__":
    # Mini test

    prod_list = [{"product_name":"Sony_Cyber-shot_DSC-W310",
                  "manufacturer":"Sony",
                  "model":"DSC-W310",
                  "family":"Cyber-shot",
                  "announced-date":"2010-01-06T19:00:00.000-05:00"},
                  {"product_name":"Canon_EOS_60D",
                  "manufacturer":"Canon","model":"60D",
                  "family":"EOS",
                  "announced-date":"2010-08-25T20:00:00.000-04:00"}, 
                  {"product_name":"Epson_PhotoPC_700",
                  "manufacturer":"Epson","model":"700",
                  "family":"PhotoPC",
                  "announced-date":"1998-07-04T20:00:00.000-04:00"}]


    listings = [{"title":"Olympus PEN E-PL1 12.3MP Live MOS Micro Four Thirds Interchangeable Lens Digital Camera with 14-42mm f/3.5-5.6 Zuiko Digital Zoom Lens (Black)",
                 "manufacturer":"Olympus Canada",
                 "currency":"CAD",
                 "price":"429.98"},
                 {"title":"Canon PowerShot A1200 (Silver)",
                 "manufacturer":"Canon Canada",
                 "currency":"CAD",
                 "price":"124.99"}]




    prod_obj = [Product(prod) for prod in prod_list]
    print_objects(prod_obj)

    print("-------------------")

    listing_obj = [Listing(li) for li in listings]
    print_objects(listing_obj)

    print("-------------------")

    result = Result(prod_obj[0])
    print(result)

    result.add_listing(listing_obj[0])
    result.add_listing(listing_obj[1])
    print_objects([result])