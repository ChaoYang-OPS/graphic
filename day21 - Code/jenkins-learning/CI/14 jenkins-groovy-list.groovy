

// 列表
//定义一个列表  [1, 2, 3, 4, 5, lsunstack]
def my_list = [1, 2, 3, 4, 5, "lsunstack"]
println(my_list)
// 列表的元素增删
// [1, 2, 3, 4, 5, lsunstack, jenkins]
println(my_list + "jenkins")
// [1, 2, 3, 4, 5]
println(my_list - "lsunstack")
//[1, 2, 3, 4, 5, lsunstack, opsk8s]
println(my_list << "opsk8s")

// true
def new_list = my_list.add("gitlab")
println(new_list)
// 判断元素是否为空
// false
println(my_list.isEmpty())

// 列表去重
// [1, 2, 3, 4, 5, lsunstack, opsk8s, gitlab]
println(my_list.unique())

// 列表反转
// [gitlab, opsk8s, lsunstack, 5, 4, 3, 2, 1]
println(my_list.reverse())

// 列表排序
// [gitlab, 1, 2, 3, 4, 5, lsunstack, opsk8s]
println(my_list.sort())

// 判断列表是否包含指定的元素
// true
println(my_list.contains("lsunstack"))

// 列表的长度
// 8
println(my_list.size())


// 扩展列表定义方式  下面执行需要在Jenkins 里面授权
/*
Scripts not permitted to use staticMethod org.codehaus.groovy.runtime.DefaultGroovyMethods count int[] java.lang.Object. 
Administrators can decide whether to approve or reject this signature.
*/
String[] stus = ["zhangsan", "lisi","wangwu"]
def num_list = [1,2,3,4,4,4] as int[]

// 通过索引获取列表元素
println(num_list[2])

// 计算列表中元素出现的次数
println(num_list.count(4))
