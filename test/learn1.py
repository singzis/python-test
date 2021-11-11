# 寻找水仙花数
# 水仙花数：也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个三位数，该数字每个位上数字的立方之和正好等于它本身
# for x in range(100, 1000):
#     low = x % 10
#     mid = x // 10 % 10
#     high = x // 100
#     if x == low ** 3 + mid ** 3 + high ** 3:
#         print(x)

# 正整数的反转
# num = int(input('请输入'))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)

# 百钱百鸡

for x in range(101):
    for y in range(101):
        for z in range(0, 101, 3):
            if (x + y + z == 100 and 5*x + 3*y + z/3 == 100):
                print('公鸡%d只，母鸡%d只，小鸡%d只' % (x, y, z))

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))