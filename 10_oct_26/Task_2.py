products=["pen","mobile","Jeans","chair"]
Categories=["Statioanry","Electronics","Garments","Furniture"]
Categories_set=set(Categories)
Categories_set.add("Appliance")
Categories_set.add("Electronics")
print(Categories_set)

print("Appliance" in Categories_set)
print("Instruments" in Categories_set)

count=len(Categories_set)
print(count)