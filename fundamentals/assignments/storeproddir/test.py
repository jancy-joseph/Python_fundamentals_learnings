from store import Store
from prod import Product
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