# • Create a contact book using a dictionary. 
contact={}
n=int(input("Number of key value pairs"))

for i in range(n):
    key=input("enter name of the person ")
    
    contact[key]={}
    m=int(input("how many sub directories does this person have"))
    for j in range(m):
        sub=input("enter key details like contact, address etc ")
        values=input("enter values to the respective keys")
        
        contact[key][sub]=values
print(contact)