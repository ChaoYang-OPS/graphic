package com.opsk8s
def print_core_msg(value,color){
    colors = ['red'   : "\033[1;031m ##############################${value}############################## \033",
              'green' : "[1;032m###################################${value}##############################\033",
              'blue' : "[1;034m###################################${value}##############################\033",
              'yellow' : "\033[1;033m ###################################${value}############################## \033" ]
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

    // commits_id = get_git_commit_id()
    get_git_commit_id()
    print_core_msg("check SCM commits_id=${env.git_commits_id}","green")
}


def docker_login_to_nexus_register_server(nexus_server,nexus3_server_credentials_id){

    withCredentials([usernamePassword(credentialsId: "${nexus3_server_credentials_id}", 
    passwordVariable: 'NEXUS_PASSWORD', usernameVariable: 'NEXUS_USER')]) {
    // some block
        // docker login 172.16.100.99:8089 -u admin -p admin
        def login_command = "docker login ${nexus_server} -u ${NEXUS_USER} -p ${NEXUS_PASSWORD} "
        exec_shell_command_return_status(login_command)
    }
}

def docker_login_to_register_server(register_server,register_server_credentials_id){

    withCredentials([usernamePassword(credentialsId: "${register_server_credentials_id}", 
    passwordVariable: 'REGISTER_PASSWORD', usernameVariable: 'REGISTER_USER')]) {
        def login_command = "docker login ${register_server} -u ${REGISTER_USER} -p ${REGISTER_PASSWORD} "
        exec_shell_command_return_status(login_command)
    }
}
def push_image_to_nexus(nexus_server, image_name, image_tag){

    print_core_msg("Push Images To Nexus , please wait ........", "green")
    def push_command = "docker push ${nexus_server}/${image_name}:${image_tag}"
    push_result = exec_shell_command_return_status(push_command)
    if (push_result == "0"){
        print_core_msg("push ${nexus_server}/${image_name}:${image_tag} success","green")
        exec_shell_command_return_status("docker rmi -f ${nexus_server}/${image_name}:${image_tag}")
        docker_logout_to_nexus_register_server(nexus_server)
    }else{
        print_core_msg("push ${nexus_server}/${image_name}:${image_tag} success","red")
        docker_logout_to_nexus_register_server(nexus_server)
    }
}
def push_image_to_aliyun(register_server, register_namespace, image_name, image_tag){

    print_core_msg("Push Images To Aliyun , please wait ........", "green")
    exec_shell_command_return_status("docker build -t ${register_server}/${register_namespace}/${image_name}:${image_tag} .")
    def push_command = "docker push ${register_server}/${register_namespace}/${image_name}:${image_tag}"
    push_result = exec_shell_command_return_status(push_command)
    if (push_result == "0"){
        print_core_msg("push ${register_server}/${register_namespace}/${image_name}:${image_tag} success","green")
        exec_shell_command_return_status("docker rmi -f ${register_server}/${register_namespace}/${image_name}:${image_tag}")
        docker_logout_to_nexus_register_server(register_server)
    }else{
        print_core_msg("push image to Aiyun${register_server}/${register_namespace}/${image_name}:${image_tag} faliure","red")
        docker_logout_to_nexus_register_server(register_server)
    }
}


def build_image(build_type,register_server,image_name, image_tag){
    image_version = get_create_version_time()
    env.image_tag = "${image_tag}" + "-" + "${image_version}"
    print_core_msg("Build Images, please wait ........", "green")
    if (build_type == "maven" || build_type == "nodejs"){
        build_image_command = "docker build -t ${register_server}/${image_name}:${env.image_tag} ."
        build_result = exec_shell_command_return_status(build_image_command)
        if (build_result == "0"){
            print_core_msg("build image ${register_server}/${image_name}:${env.image_tag} success","green")
        }
    }
}

def docker_logout_to_nexus_register_server(nexus_server){

    withCredentials([usernamePassword(credentialsId: "${nexus3_server_credentials_id}", 
    passwordVariable: 'NEXUS_PASSWORD', usernameVariable: 'NEXUS_USER')]) {
        def logout_command = "docker logout ${nexus_server}"
        exec_shell_command_return_status(logout_command)
    }
}
def input_request_approved(input_message, input_description, input_submitter, input_name){
    input message: "${input_message}", ok: 'Yes',
    parameters: [choice(choices: ['Yes', 'No'], 
    description: "${input_description}", name: "${input_name}")], 
    submitter: "${input_submitter}", 
    submitterParameter: "${input_name}"
    println(parameters)
}
def build_scm_code(build_type, build_command){
    def build_tools = ["maven": "/usr/local/maven-3.8.1/bin",
                       "gradle": "/usr/local/gradle-6.8.3/bin", 
                       "go": "/usr/local/go/bin", 
                       "sonar": "/usr/local/sonar-scanner-4.6.0.2311/bin", 
                       "nodejs": "/usr/local/node-v14.16.1/bin"]
    print_core_msg("current build_type=${build_type}", "green")
    print_core_msg("current build_command=${build_command}", "green")
    switch(build_type) {
        case "maven":
            // sh "${build_tools["maven"]}/${build_command}"
            exec_shell_command_return_status("${build_tools["maven"]}/${build_command}")
            break
        case "gradle":
            sh "${build_tools["gradle"]}/${build_command}"
            break
        case "go":
            sh "${build_tools["go"]}/${build_command}"
            break
        case "nodejs":
            print_msg("The front end takes a long time to pack, please be patient. Thank you for using, thank you", "green")
            exec_shell_command_return_status("${build_tools["nodejs"]}/${build_command}")
            break
        default:
            print_msg("unknown build_type ==> [maven|gralde|nodejs|go]", "green")
            
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

def get_current_trigger_type(trigger_type){
    if (trigger_type == "automatically"){
        currentBuild.description = "${trigger_type} Trigger by ${env.user_email}  branche_name=${env.branche_name} \n email: ${env.user_email}"
    } else if (trigger_type == "manually"){
        currentBuild.description = "${trigger_type} Trigger by ${env.user_email}  branche_name=${env.branche_name} \n email: ${env.user_email}"
    } else {
        currentBuild.description = "Unknown Trigger"
    }
}

def get_create_version_time() {
    return new Date().format('yyyyMMddHHmm') +new Date().getTime()
    // return new Date().format('yyyyMMddHHmmss') + "_${env.BUILD_ID}"
}

def get_create_version_time_and_build_id() {
    return new Date().format('yyyyMMddHHmm') +new Date().getTime()+ "-${env.BUILD_ID}"
    // return new Date().format('yyyyMMddHHmmss') + "_${env.BUILD_ID}"
}



// def set_output_font_color_to_red(message){
//     ansiColor ('xterm'){
//         sh "echo \"\\033[1;031m${message} \\033[0m\""
//     }
// }

// def set_output_font_color_to_green(message){
//     ansiColor ('xterm'){
//         sh "echo \"\\033[1;032m${message} \\033[0m\""
//     }
// }

// def set_output_font_color_to_blue(message){
//     ansiColor ('xterm'){
//         sh "echo \"\\033[1;034mm${message} \\033[0m\""
//     }
// }

// def set_output_font_color_to_yellow(message){
//     ansiColor ('xterm'){
//         sh "echo \"\\033[1;033mm${message} \\033[0m\""
//     }
// }


def print_msg(value,color){
    colors = ['red'   : "\033[1;031m ${value} \033",
              'green' : "[1;032m${value}\033",
              'blue' : "[1;034m${value}\033",
              'yellow' : "\033[1;033m ${value} \033" ]
    ansiColor('xterm') {
        println(colors[color])
    }
}

def get_git_commit_id(){
    def get_commits_id_command = "git rev-parse --short HEAD"
    commits_id = exec_shell_command_return_response(get_commits_id_command)
    env.git_commits_id = commits_id
    return commits_id
}

def nexus_artifact_plugin_upload(artifact_id, file_name, file_type,group_id, nexus_repository, app_version){
    def nexus3_server_credentials_id = "0b52bd27-d8dd-42de-b394-1cd6f384f932"
    def nexus_server_url = "172.16.100.99:8081"
    def nexus_server_protocol = "http"
    def nexus_version = "nexus3"
    nexusArtifactUploader artifacts: [[artifactId: "${artifact_id}", classifier: '', file: "${file_name}", type: "${file_type}"]], 
    credentialsId: "${nexus3_server_credentials_id}", 
    groupId: "${group_id}", nexusUrl: "${nexus_server_url}", 
    nexusVersion: "${nexus_version}", protocol: "${nexus_server_protocol}", 
    repository: "${nexus_repository}", version: "${app_version}"
}
