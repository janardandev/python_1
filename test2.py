def fun(list1):
    length = (len(list1))
    if len(list1) % 2 == 0:
        middle_index = length // 2
        first_half = list1[:middle_index]
        second_half = list1[middle_index:]
        first_part = sum(first_half)
        second_part = sum(second_half)
        if first_part == second_part:
            print("you are lucky")
        else:
            print(" you are unlucky")
    else:
        print("type your number again")


fun([2,3, 5, 2, 3, 3, 2, 1])

#     # first_half = list11[:middle_index]
#     # print(first_half)
#     # second_half = list11[middle_index:]
#     # print(second_half)
#     total = 0
#     total2 = 0
#     for i in range(0, len(first_half)):
#         total = total + first_half[i]
#
#     print(total)
#     for i in range(0, len(second_half)):
#         total2 = total2 + second_half[i]
#     print(total2)
#     if total == total2:
#         print("you are lucky")
#     else:
#         print("unlucky")
# fun([1,2,3,3,2,1])
#     # first = sum(first_half)
#     # print(first)
#     # second = sum(second_half)
#     # print(second)
#     # if first == second:
#     #     print("you are lucky")
#     # else:
#     #     print(" you are unlucky")
#     #
