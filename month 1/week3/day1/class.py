# # set, list and dict comprehension
# a=[1,2,3,4,5,6,7,8]
# list2= [item*item for item in a]
# print(list2)

# set1={1,2,3,2,5,1,6,3,4,5,6,7,8}
# set2={item*item for item in set1}
# print(set2)

# dicct={k:v for k,v in enumerate(a)}
# print(dicct)

# a = [1,2,3,2,5,1,6,3,4,5,6,7,8,0,0,0,0,0]
# freq={i:a.count(i) for i in set(a)}
# print(freq)#or

# dict1={}
# for i in a:
#     if i in dict1:
#         dict1[i]+=1
#     else:
#         dict[i]=1
# print(dict1)


# fruits=["mango","apple", "banana"]
# dict={i:len(i)for i in fruits}
# print(dict)

# dict1={"mango":80,"banana":40,"tata":50}
# dict2={k:v+10 if len(k)>4 else v-10 for k,v in dict.items() if v<=50}
# print(dict2)

# #list comp and time difference
# import time
# start=time.time()
# list1=[i*i for i in range(1000000)]
# print(time.time()-start)

# import time
# start=time.time()
# list1=[i*i for i in range(1000000)]
# print(time.time()-start)

# 55k+ then 10% incre else 5%

# emp = {
#     "paridhi": 50000,
#     "gurman": 60000,
#     "avantika": 56000,
#     "hjkdf": 32000,
#     "hjdfg": 43000
# }
# result = {k: v + (v * 10 // 100) if v >= 55000 else v + (v * 5 // 100)for k, v in emp.items()}
# print(result)

#dictionary compre
emp = {
    "paridhi": {"salary": 50000, "bonus": 0, "total": 0},
    "gurman": {"salary": 60000, "bonus": 0, "total": 0},
    "avantika": {"salary": 56000, "bonus": 0, "total": 0},
    "hjkdf": {"salary": 32000, "bonus": 0, "total": 0},
    "hjdfg": {"salary": 43000, "bonus": 0, "total": 0},
}

dict2 = {
    k: {
        "salary": v["salary"],
        "bonus": v["salary"] * 10 / 100 if v["salary"] >= 55000 else v["salary"] * 5 / 100,
        "total_salary": v["salary"] + (v["salary"] * 10 / 100 if v["salary"] >= 55000 else v["salary"] * 5 / 100)
    }
    for k, v in emp.items()
}

print(dict2)