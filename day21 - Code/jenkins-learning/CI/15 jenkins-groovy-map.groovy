

// 映射 map
// types = ["maven": "mvn"] [:]

def my_tools = ["mvn": "/usr/local/maven",
                "gradle": "/usr/local/gradle"]

// 根据key获取value
// /usr/local/maven
println(my_tools["mvn"])
// /usr/local/gradle
println(my_tools["gradle"])

// 根据key重新赋值

my_tools["mvn"] = "/data/maven"
// {mvn=/data/maven, gradle=/usr/local/gradle}
println(my_tools)

// 判断map是否包含某个key或者value
println(my_tools.containsKey("gradle"))  // true
println(my_tools.containsValue("/data/maven"))  // true

// 返回map的key 列表

// [mvn, gradle]
println(my_tools.keySet())

//  根据key删除元素
// /data/maven

println(my_tools.remove("mvn"))

// {gradle=/usr/local/gradle}
println(my_tools)