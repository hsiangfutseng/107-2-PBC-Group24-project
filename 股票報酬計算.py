num1 = float(input("請輸入成交價") )
num2 = int(input("請輸入成交股數") )
num3 = float(input("請輸入欲成交價") )

a = num1*num2 #成交價金
b = num2*num3 #股票現值
c = a*0.00064+b*(0.001425*0.45+0.003) #交易成本

print("淨損益"+str(b-a-c))
print("報酬率" + str(((b-a-c)/(a+c))*100) + "%")
print("交易成本" + str(c) )

# it's for gibhub fetching testing
# Hi, I'm 祥富.