# name  = "Aakash Kandel"
# age = 24
# bio = "I am oddo developer"


# print("Hi i am "+name+" " +str(age));

# print(f"Hi i am {name} and i am {age} years and {bio}")


# # list 

# colors = ["blue","green","pink","yellow","red","black","orange","violet","brown","indigo"]

# # print(colors)

# # for color in colors:
# #     print(color)

# for i in range(3):
#     print(colors[i])


# def findListLength(itmes):
#     count = 0
#     for item in itmes:
#         count +=1
#     return count

# count = findListLength(colors);
# print(f"The length of colors is {count}")


numbers = [1,2,3,4,5,6]
def countEvenNumbers(num):
    count = 0
    for n in num:
        if n % 2 == 0:
            count +=1
    return count

print(f"{countEvenNumbers(numbers)}")
