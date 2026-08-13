
# ----------------------------MINI PROJECT NO.4-------------------

# ------------------------Create a restaurent biling system---------------------------------


class RestaurentOeder:
    def __init__(self):
        self.items = []

    def add_items(self,name,quantity,price):
        self.items.append({
            "name" : name,
            "quantity": quantity,
            "price" : price
        })

    def calculate_bill(self):
        total = 0
        for item in self.items:
            total += item["quantity"]  *  item["price"]   

        return total 

    def display_bill(self):
            print("Restaurant Bill")
            for item in self.items:
                 items_total =item["quantity"] * item["price"]
                 print(item["name"], item["quantity"],
                 item["price"], item_total )
            print("Final Bill:", self.calculate_bill() )     