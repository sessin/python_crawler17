# dict
name = "matthew"
user = "matthew 33 100000 010-0000-0000"
user2 = "mark 30 1000000 010-1000-0000"

print(user[18:]) # 여기에서 전화번호만 출력 해보세요
print(user2[16:]) # user2에서 전화번호만 출력 해보세요

# field명 key
user3 = {"name":"luke", "age":33, "salary":20000, "phone":"010-2000-0000"}
user4 = {"name":"john", "salary":30000, "phone":"010-4000-0000", "age":28}

print("u3=>", user3["phone"])
print("u4=>", user4["phone"])
