
// 注释  单行注释 //, 多行注释 /**/


// 数据类型

// 字符串string 字符串表示的方式: 单引号、双引号、三单双引号

// 定义一个字符串类型变量name 

String name = 'lsunstack'

println(name)

//定义一个变量包含多行内容

String msg = """
code = 0
data = 1
message = successful
"""

println(msg)

// 字符串切分操作

String branch_name = "release-6.6.6"
println(branch_name.split("-")[0])
println(branch_name.split("-")[-1])
println("${env.JOB_NAME}".split("-")[0])

//是否包含release字符串

println(branch_name.contains("release"))

//字符串的长度

println(branch_name.size())

println(branch_name.length())

//使用变量作为值
def message = "hello ${name}"
println(message)
println(message.toString())

//获取元素索引值
println(branchName.indexOf("-"))

//判断字符串以UAT结尾
String jobName = "demo-pipeline-001-UAT"
println(jobName.endsWith("UAT"))

//字符串增添操作
String log = "error: xxxxxx aa"
println(log.minus("a"))
println(log - "a")
println(log.plus("aa"))
println(log + "aa")

//字符串反转
String nums = "1234567"
println(nums.reverse())