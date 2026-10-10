products=["pen","book","mobile","pencil","eraser"]
sample_products=("pen",10,"Stationary")
print(products[1])
print(products[-1])
products.append("chair")
print(products)

S_product=list(sample_products)
S_product[1]=20
sample_products_1=tuple(S_product)
print(sample_products_1)