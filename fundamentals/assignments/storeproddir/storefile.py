class Store:
    def __init__(self,name):
        self.name = name
        self.product = []
    def add_product(self, new_product):
        self.product.append(new_product)
        new_product.id =len(self.product)-1
    #    self.print_listof_products()
        return self 
    def print_listof_products(self):
        for i in range(len(self.product)):
            self.product[i].print_info()
        return self
    def sell_product(self, idx):
        #self.print_listof_products()
        #print(type(idx),idx)
        for i in range(len(self.product)):
            if(self.product[i].id == idx):
                self.product.pop(idx)
                #because we popped an element the length of array has changed so we need to break out of loop
                #after updating the ids of the rest of elements.Hence we are iterating from the current index to 
                # one less than the previosu length
                start = idx
                end = len(self.product) -1
                for i in range(start,end):
                    self.product[i].id-=1
                break#as index will go out of range as length now got reduced
        return self
    def inflation(self, percent_increase):
        for i in range(len(self.product)):
            self.product[i].update_price(percent_increase,True)
        return self
    def set_clearance(self, category, percent_discount):
        for i in range(len(self.product)):
            if self.product[i].category == category:
                self.product[i].update_price(percent_discount,False)
        return self 
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
storeobj =Store("Mystore")
prodobj = Product("prod1",20,"A")
#print(prodobj.name,prodobj.price,prodobj.category)
prodobj1 = Product("prod2",34,"B")
storeobj.add_product(prodobj).add_product(prodobj1)
storeobj.print_listof_products()
storeobj.sell_product(1).print_listof_products()
""" storeobj.inflation(20)
print("after inflation")
storeobj.print_listof_products().set_clearance("B",20)
print("after clearance")
storeobj.print_listof_products() """