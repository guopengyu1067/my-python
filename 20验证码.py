import random
s="0123456789"#添加数字
for i in range(97,123):
    s+=chr(i)#添加小写字母
for j in range(65,91):
    s+=chr(j)#添加大写字母
#s等于所有字母和数字
code=""#验证码
n=int(input("请输入验证码的位数："))
for i in range(n):
    code+=random.choice(s)#随机选择一个字符
print(code)
u=input("请输入验证码：")
while True:
    if u!=code:
        print("验证码错误")
        code = ""
        for i in range(n):
            code += random.choice(s)
            print(code)
            u=input("请输入验证码：")
    if u==code:
        print("验证码正确")
        break



