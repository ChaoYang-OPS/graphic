/*
条件语句
if语句
在Jenkinsfile中可用于条件判断。
*/
/*
定义变量参数branch_name
如果branch_name 等于DEV则打印DEV，
如果branch_name 等于UAT则打印UAT，
上面都不匹配则打印skipdeploy
*/

String  branch_name = "DEV"
if ( branch_name == "DEV" ){
    println("DEV....")

} else if (branch_name == "UAT"){
    println("UAT....")

} else {
    println("skipdeploy......")
}

// switch语句
/*
定义参数branch_name
匹配 develop  则打印develop ，跳出。
匹配 release  则打印release ，跳出。
默认匹配， 打印 error ，退出。
*/
String branch_name = "develop"
switch(branch_name) {
    case "develop":
        println("develop .....")
        break
    case "release":
        println("release.....")
        break
    default:
        println("error。。。。。。")
}

// for

// 遍历0-9，打印
for (i=1; i<10; i++ ){
	println(i)
}

// 循环5次
5.times { 
	println("hello")
}

// 遍历 0-4
5.times { i ->
   println(i)
}

// 遍历List
def server_list = ["server-1", "server-2", "server-3"]

for ( i in server_list){
	println(i)
}


// 使用each遍历map
def stus = ["lsunstack":"177", "opsk8s":"199"]
stus.each { k, v ->
	println(k+"="+v)

}

// 使用for遍历map
for (k in stus.keySet()){
	println(k+"="+stus[k])

}

// 异常处理

/*
 如果println(a,b)失败(肯定失败，因为有语法错误)
 catch捕获错误，并打印错误.
 finally 总是执行
*/

try{
    println(a, b)
}
catch(Exception e){
    println(e)
}
finally{
    println("done")
}