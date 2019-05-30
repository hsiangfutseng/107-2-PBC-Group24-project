def twid_check(twid):
    """check if twid validate"""
    if len(twid) != 10: # check length
        return 1

    upper = ord(twid[0])
    if upper < 65 or upper > 90: # check first letter
        return 2

    sex = int(twid[1])
    if sex < 1 or sex > 2: # check sex
        return 3

    for i in range(1,10): # check the test are numbers
        num = ord(twid[i])
        if num < 48 or num > 57:
            return 4

    tran_list = [10,11,12,13,14,15,16,17,34,18,19,20,21,22,35,23,24,25,26,27,28,29,32,30,31,33] # letters to numbers

    n_num = tran_list[upper - 65] # find corresponding number
    newid = str(n_num) + str(twid[1:]) # new id with 11 numbers

    """validate: ckecksum % = 0 """
    weight_list = [1,9,8,7,6,5,4,3,2,1,1] # weight in each number

    checksum = 0
    for i in range(0,11): # summary
        checksum += int(newid[i]) * int(weight_list[i])

    judge = checksum % 10 # judge standard

    if judge == 0:
        return 0
    else:
        return 5


"""Operation"""


name = input("What's your name:")
print("Hello", name)
print()

while True:
    twid = input("please input your ID number:")
    check = twid_check(twid)

    if check == 0:
        print("That's right! Congratulate.")
        break

    if check != 0:
        print("Sorry! You have wrong number.")
        print()
        continue
