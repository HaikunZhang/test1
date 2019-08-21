#!/usr/bin/env python
# -*- coding:utf-8 -*-


##################################################################
# 练习1. 简易计算器                                               #
# 要求： 1. 用户输入两个数，接下来程序第一行打印两个数的和，        #
#       2. 第二行打印两个数的差                                   #
#       3. 第三行打印两个数的乘积                                 #
#       4. 第四行打印两个数的商                                   #
#       5. 打印出第一个数的整数，整数的十六进制、八进制、二进制形式 #
##################################################################

num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))

print("第一个数为：%.2f"%num1,"第二个数为：%.2f"%num2)

print( num1,"+", num2,"=",(num1 + num2))
print( num1,"-", num2,"=",(num1 - num2))
print( num1,"*", num2,"=",(num1 * num2))
print( num1,"/", num2,"=",(num1 / num2)) if num2 != 0 else print("第二个数不能为0")

n1 =int(num1)
print("整数为：",n1,"十六进制为：", hex(n1),"八进制为：",oct(n1),"二进制为：",bin(n1))
print("整数为：%d"% num1,"十六进制为：%x"% n1,"八进制为：%o"% n1,"二进制不支持字符串格式化输出")


