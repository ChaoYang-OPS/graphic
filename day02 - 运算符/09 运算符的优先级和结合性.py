"""运算符的优先级和结合性"""

"""
一、 什么是运算符的优先级
        每个运算符都有固定的优先级
        当表达式中包含优先级不同的运算符时，高优先级的运算符先参与运算
        比如: 运算符*和/的优先级就比运算符+和-的优先级高，正所谓"先乘除，后加减"
"""
# * 比+的优先级高，*先参与运算
print(2 + 3 * 4)  # 14

"""
二、什么是运算符的结合性
     每个运算符都有固定的结合性
     当表达式中包含优先级相同的运算符时，结合性定义了哪个运算符先参与运算。
     
     如果运算符的结合性为左，那么左边的运算符先参与运算，
     比如： 2 + 3 - 4, 2 + 3 会先参与运算
     如果运算符的结合性为右，那么右边的运算符先参与运算
     比如： a = b = 18， b = 18 会先参与运算
"""

"""
三、 正确使用运算符的优先级和结合性
      没有必要记忆所有运算符的优先级和结合性
      
      对于包含多个运算符的复杂表达式，其可读性是较低的，为了提高可读性，建议的做法有两种:
        (1) 在复杂表达式中使用小括号来指定运算顺序
        (2) 将复杂表达式拆分几步来完成 
"""

is_has_key = False
is_entered_door = False
is_passed_scan = False
is_know_password = True

# and比or的优先级高，or的结合性是左
print(is_has_key or is_entered_door and is_passed_scan or is_know_password)  # True
# 在复杂表达式使用小括号指定运算顺序
print((is_has_key or (is_entered_door and is_passed_scan)) or is_know_password)  # True
# 将复杂表达式拆分几步来完成
step1 = is_entered_door and is_passed_scan
step2 = is_has_key or step1
step3 = step2 or is_know_password
print(step3)  # True
