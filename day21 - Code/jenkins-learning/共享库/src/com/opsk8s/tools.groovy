//格式化输出
def print_msg(value,color){
    colors = ['red'   : "\033[40;31m #####################${${value}#####################${ \033[0m",
              'green' : "\033[40;32m #####################${${value}#####################${ \033[0m" ]
    ansiColor('xterm') {
        println(colors[color])
    }
}