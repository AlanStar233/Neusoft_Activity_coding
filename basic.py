# # Ctrl+'/'
#
# print('Hello Alan!')
#
# #int
# age = 19
#
# #string
# name = "张三"
#
# #print with var & var_type
# print(age)
# print(type(age))
#
# print(name)
# print(type(name))

# if
name = input("Please type your name:")
age = input("Please type your age:")

if int(age) >= 18:
    print('{} Your age {} >= 18 !'.format(name, age))
else:
    print('{} Your age {} < 18 !'.format(name, age))
