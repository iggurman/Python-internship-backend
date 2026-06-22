def max(*yo):
    tem=0
    for i in yo:
        if i>tem:
            tem=i
    return tem

print(max(10,20,30,100))