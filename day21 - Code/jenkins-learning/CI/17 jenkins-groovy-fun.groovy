/*
def关键字 定义函数名为print_msg， 带有一个参数msg，语句块内容是打印msg参数的值，返回msg值。
将print_msg函数的执行结果返回给response变量。
打印response
*/

def print_msg(msg){
	println(msg)
	return msg
}

response = print_msg("lsunstack is ok with jenkins")
println(response)