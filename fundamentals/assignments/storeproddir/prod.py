class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
        self.id = None
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price * percent_change/100
        else:
            self.price -= self.price * percent_change/100
        return self
    def print_info(self):
        print("Prod name:"+self.name+" category:"+self.category+" price"+str(self.price)+"id :"+str(self.id))
        return self