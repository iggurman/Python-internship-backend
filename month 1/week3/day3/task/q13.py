def uni(x):
    st=set()
    for i in x:
        if i not in st:
            st.add(i)
    yield st
        
lst=[1,2,3,4,5,6,7,3,2,1,12,4,5,67,674,3,2,1,14,5,6,7,534,2,]
x=uni(lst)
for i in x:
    print(i)