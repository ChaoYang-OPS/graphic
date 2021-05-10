

def print_core_msg(value,color){
    colors = ['red'   : "\033[1;031m ##############################${value}############################## \033",
              'green' : "[1;032m###################################${value}##############################\033",
              'blue' : "[1;034m###################################${value}##############################\033",
              'yellow' : "\033[1;033m ###################################${value}############################## \033" ]
    ansiColor('xterm') {
        println(colors[color])
    }
}


def print_msg(value,color){
    colors = ['red'   : "\033[1;031m ${value} \033",
              'green' : "[1;032m${value}\033",
              'blue' : "[1;034m${value}\033",
              'yellow' : "\033[1;033m ${value} \033" ]
    ansiColor('xterm') {
        println(colors[color])
    }
}


def get_scm_code(git_http_url, branche_name, git_http_credentials_id){
    print_core_msg("check SCM git_http_url=${git_http_url} ","green")
    print_core_msg("check SCM branche_name=${branche_name}","green")
    checkout([$class: 'GitSCM', branches: [[name: "${branche_name}"]],
    extensions: [], userRemoteConfigs: [[credentialsId: "${git_http_credentials_id}",
    url: "${git_http_url}"]]])
}


def docker_login_to_register_server(register_server,register_server_credentials_id){

    withCredentials([usernamePassword(credentialsId: "${register_server_credentials_id}",
    passwordVariable: 'REGISTER_PASSWORD', usernameVariable: 'REGISTER_USER')]) {
        def login_command = "docker login ${register_server} -u ${REGISTER_USER} -p ${REGISTER_PASSWORD} "
        exec_shell_command_return_status(login_command)
    }
}

def exec_shell_command_return_status(shell_command){
    def shell_command_return_status = "-1"
    def shell_command_return_status_error_msg = "./shell_command_return_status_error.log"

    if (shell_command.length() != 0){
        // sh(returnStdout: true, scrip:cmd)
        // sh(returnStdout: true, scrip:cmd).toString().trim()
        // sh(returnStdout: true, scrip:cmd > stdout 2> stderr).toString().trim()
        // def shell_command_return_status= sh returnStdout: true, script: "${shell_command}"
        shell_command_return_status = sh (encoding: "UTF-8", returnStatus: true, returnStdout: true, script: "${shell_command} 2> ${shell_command_return_status_error_msg}").toString().trim()
        if (shell_command_return_status == "0"){
            print_msg("[success] execution [${shell_command}] with return : [${shell_command_return_status}]","green")
            return shell_command_return_status
        }else{
             error_msg = readFile encoding: 'UTF-8', file: "${shell_command_return_status_error_msg}"
             print_msg("[error] execution [${shell_command}] with return : [${error_msg}]","red")
             print_msg("clear the temporary error log file ${shell_command_return_status_error_msg}","blue")
             delete_command = "rm -f ${shell_command_return_status_error_msg} &>/dev/null"
             exec_shell_command_return_status(delete_command)
        }

    }
    return shell_command_return_status
}

def exec_shell_command_return_response(shell_command){

    def shell_command_response = "-1"
    if(shell_command.length() !=0){
        // sh returnStdout: true, script: ''
        shell_command_response = sh  returnStdout: true, script: "${shell_command}"
        shell_command_response = shell_command_response - "\n"
        print_msg("[success] execution [${shell_command}] with return : [${shell_command_response}]","green")
    }else{
        print_msg("[error] execution [${shell_command}] with return : [${shell_command_response}]","red")
        return shell_command_response
    }
    return shell_command_response
}

def get_create_version_time() {
    return new Date().format('yyyyMMddHHmm') +new Date().getTime()
    // return new Date().format('yyyyMMddHHmmss') + "_${env.BUILD_ID}"
}

def get_create_version_time_and_build_id() {
    return new Date().format('yyyyMMddHHmm') +new Date().getTime()+ "-${env.BUILD_ID}"
    // return new Date().format('yyyyMMddHHmmss') + "_${env.BUILD_ID}"
}

