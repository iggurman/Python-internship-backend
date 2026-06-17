# • Create an inventory system using a dictionary. 
inventory={}
m=int(input("enter the number of keys "))
for i in range(m):
    key=input("enter keys ")
    values=input("enter values ")
    inventory[key]=values
print(inventory)
