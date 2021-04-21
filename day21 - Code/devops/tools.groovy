package org.devops

//格式化输出
def PrintMes(value,color){
    colors = ['red'   : "\033[40;31m >>>>>>>>>>>${value}<<<<<<<<<<< \033[0m",
              'blue'  : "\033[47;34m ${value} \033[0m",
              'green' : "[1;32m>>>>>>>>>>${value}>>>>>>>>>>[m",
              'green1' : "\033[40;32m >>>>>>>>>>>${value}<<<<<<<<<<< \033[0m" ]
    ansiColor('xterm') {
        println(colors[color])
    }
}


def exec_shell_command_return_status(shell_command){
    def shell_command_return_status = "-1"

    def shell_command_return_status = sh encoding: "UTF-8", returnStatus: true, returnStdout: true, script: "${shell_command}"

    if (shell_command.length() != 0 && shell_command_return_status == 0){
        def shell_command_return_response = sh returnStdout: true, script: "${shell_command}"
        // println("${shell_command_return_response}")
        // println("[success] execution [${shell_command}] with return : [${shell_command_return_status}]")
    }else{
        println("[error] execution [${shell_command}] with return : [${command_return_status}]")
    }
    return shell_command_return_status
}