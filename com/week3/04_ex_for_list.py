# user에게 hello라고 인사하는 프로그램을 만들어 보세요
# ex) hello matthew?, hello mark?
users = ["matthew","mark","luke","john"]

# for each를 이용해서 만들어 보세요
def getGreet(user):
    return "hello {}".format(user)

for user in users:
    greet = getGreet(user)
    print(greet)