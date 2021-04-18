

// import share lib
@Library('demo-jenkins-lib') _

def tools = new com.opsk8s.tools()

/*
def print_msg(value,color){
    colors = ['red'   : "\033[40;31m >>>>>>>>>>>${value}<<<<<<<<<<< \033[0m",
              'green' : "[1;32m>>>>>>>>>>${value}>>>>>>>>>>[m",
              'green1' : "\033[40;32m >>>>>>>>>>>${value}<<<<<<<<<<< \033[0m" ]
    ansiColor('xterm') {
        println(colors[color])
    }
}
*/


try {
  // Gitlab提交触发
  // generic-webhook
  println("${generic_webhook_data}")
  tools.print_msg("The build is triggered automatically", "green")
  def data = readJSON text: "${generic_webhook_data}"
  env.branche_name = data["ref"] - "refs/heads/"
  env.git_http_url = data["project"]["git_http_url"]
}
catch(Exception e) {
  println(e)
  tools.print_msg("The build is triggered manually","green")
}

String branche_name = "${env.branche_name}"
String git_http_url = "${env.git_http_url}"
pipeline{
    agent {label "build"}
    parameters {
        string defaultValue: 'http://172.16.100.120/opsk8s/demo-springboot-service.git',
        description: 'The project code GIT address Example: http://172.16.100.120/opsk8s/demo-springboot-service.git',
        name: 'git_http_url', trim: true

        string defaultValue: 'master', description: 'branche_name , eg: master', name: 'branche_name', trim: true

    }

    options{
        disableConcurrentBuilds()
        skipDefaultCheckout()
        timeout(time: 1, unit: 'HOURS')
    }

    stages{
        stage("Get SCM Code"){
            options{
                timeout(time: 5, unit: 'MINUTES')
                retry(3)
                timestamps()
            }
            steps{
                script{
                    tools.print_msg("check SCM git_http_url=${git_http_url}","green")
                    tools.print_msg("check SCM branche_name=${branche_name}","green")
                    checkout([$class: 'GitSCM', branches: [[name: "${branche_name}"]],
                    extensions: [], userRemoteConfigs: [[credentialsId: 'ddf5f4aa-2ceb-46c0-a284-67a8945ac00f',
                    url: "${git_http_url}"]]])
                }
            }
            post {
                success {
                    script{
                        tools.print_msg("check SCM Code successful!!!","green")
                    }
                }
                failure {
                    script{
                        tools.print_msg("check SCM Code failure!!!","red")
                    }
                }
            }
        }
    }
}

/*

def EmailUser(userEmail,status){
  emailext body: """
            <!DOCTYPE html>
            <html>
            <head>
            <meta charset="UTF-8">
            </head>
            <body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4" offset="0">
                <img src="http://172.16.100.99:8080/static/0eef74bf/images/headshot.png">
                <table width="95%" cellpadding="0" cellspacing="0" style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">
                    <tr>
                        <td><br />
                            <b><font color="#0B610B">构建信息</font></b>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <ul>
                                <li>项目名称：${JOB_NAME}</li>
                                <li>构建编号：${BUILD_ID}</li>
                                <li>构建状态: ${status} </li>
                                <li>项目地址：<a href="${BUILD_URL}">${BUILD_URL}</a></li>
                                <li>构建日志：<a href="${BUILD_URL}console">${BUILD_URL}console</a></li>
                            </ul>
                        </td>
                    </tr>
                    <tr>
                </table>
            </body>
            </html>  """,
            subject: "Jenkins-${JOB_NAME}项目构建信息 ",
            to: userEmail

}

*/





// import share lib
@Library('demo-jenkins-lib') _

def tools = new com.opsk8s.tools()
def mail = new com.opsk8s.mails()

/*
def print_msg(value,color){
    colors = ['red'   : "\033[40;31m >>>>>>>>>>>${value}<<<<<<<<<<< \033[0m",
              'green' : "[1;32m>>>>>>>>>>${value}>>>>>>>>>>[m",
              'green1' : "\033[40;32m >>>>>>>>>>>${value}<<<<<<<<<<< \033[0m" ]
    ansiColor('xterm') {
        println(colors[color])
    }
}
*/


try {
  // Gitlab提交触发
  // generic-webhook
  println("${generic_webhook_data}")
  tools.print_msg("The build is triggered automatically", "green")
  def data = readJSON text: "${generic_webhook_data}"
  env.branche_name = data["ref"] - "refs/heads/"
  env.git_http_url = data["project"]["git_http_url"]
  env.user_email = data["user_email"]
  env.user_username = data["user_username"]
  env.trigger_type = "automatically"
}
catch(Exception e) {
  println(e)
  tools.print_msg("The build is triggered manually","green")
  env.trigger_type = "manually"
}

String branche_name = "${env.branche_name}"
String git_http_url = "${env.git_http_url}"
String build_type = "${env.build_type}"
String build_command = "${env.build_command}"
String skip_code_scan = "${env.skip_code_scan}"

pipeline{
    agent {label "build"}
    parameters {
        string defaultValue: 'http://172.16.100.120/opsk8s/demo-springboot-service.git',
        description: 'The project code GIT address Example: http://172.16.100.120/opsk8s/demo-springboot-service.git',
        name: 'git_http_url', trim: true

        string defaultValue: 'master', description: 'branche_name , eg: master', name: 'branche_name', trim: true

        choice choices: ['maven', 'gradle', 'nodejs'], description: 'build type', name: 'build_type'

        string defaultValue: 'mvn clean package', description: 'build command , eg: mvn clean package', name: 'build_command', trim: true

        choice choices: ['true', 'false'], description: 'Whether to skip the code scan ，false apply  code scan', name: 'skip_code_scan'

    }

    options{
        disableConcurrentBuilds()
        skipDefaultCheckout()
        timeout(time: 1, unit: 'HOURS')
    }

    stages{
        stage("Get SCM Code"){
            options{
                timeout(time: 5, unit: 'MINUTES')
                retry(3)
                timestamps()
            }
            steps{
                script{
                    tools.print_msg("check SCM git_http_url=${git_http_url} ","green")
                    tools.print_msg("check SCM branche_name=${branche_name}","green")
                    checkout([$class: 'GitSCM', branches: [[name: "${branche_name}"]],
                    extensions: [], userRemoteConfigs: [[credentialsId: 'ddf5f4aa-2ceb-46c0-a284-67a8945ac00f',
                    url: "${git_http_url}"]]])
                }
            }
            post {
                success {
                    script{
                        tools.print_msg("check SCM Code successful!!!","green")
                    }
                }
                failure {
                    script{
                        tools.print_msg("check SCM Code failure!!!","red")
                        // error "check SCM Code failure!!!, Exit....."
                    }
                }
            }
        }
        stage("Build SCM Code"){
            steps{
                script{
                    tools.print_msg("current build_type=${build_type}", "green")
                    tools.print_msg("current build_command=${build_command}", "green")
                    tools.build_scm_code("${build_type}", "${build_command}")
                }
            }
            post{
                always{
                    script{
                        tools.get_current_trigger_type("${env.trigger_type}")
                    }
                }
            }
        }
        stage("Scan SCM Code"){
            when{
                environment name: 'skip_code_scan', value: 'false'
            }
            steps{
                script{
                    tools.print_msg("Scan SCM Code, please wait ........", "green")
                }
            }
        }
        stage("Build Images"){
            steps{
                script{
                    tools.print_msg("Build Images, please wait ........", "green")
                }
            }
        }
        stage("Push Images"){
            steps{
                script{
                    tools.print_msg("Push Images, please wait ........", "green")
                }
            }
        }
    }
    post{
        always{
            script{
                mail.mail_send_build_info("${env.user_email}", "${currentBuild.currentResult}")
            }
        }
    }
}




//


package com.opsk8s
def print_msg(value,color){
    colors = ['red'   : "\033[40;31m ##############################${value}############################## \033[0m",
              'green' : "[1;32m###################################${value}##############################[m",
              'green1' : "\033[40;32m ###################################${value}############################## \033[0m" ]
    ansiColor('xterm') {
        println(colors[color])
    }
}


def build_scm_code(build_type, build_command){
    def build_tools = ["maven": "/usr/local/maven-3.8.1/bin",
                       "gradle": "/usr/local/gradle-6.8.3/bin",
                       "go": "/usr/local/go/bin",
                       "nodejs": "/usr/local/node-v14.16.1/bin"]
    switch(build_type) {
        case "maven":
            sh "${build_tools["maven"]}/${build_command}"
            break
        case "gradle":
            sh "${build_tools["gradle"]}/${build_command}"
            break
        case "go":
            sh "${build_tools["go"]}/${build_command}"
            break
        case "nodejs":
            print_msg("The front end takes a long time to pack, please be patient. Thank you for using, thank you", "green")
            sh "${build_tools["nodejs"]}/${build_command}"
            break
        default:
            print_msg("unknown build_type ==> [maven|gralde|nodejs|go]", "green")

    }
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
    return new Date().format('yyyyMMddHHmm') +new Date().getTime()+ "-${env.BUILD_ID}"
    // return new Date().format('yyyyMMddHHmmss') + "_${env.BUILD_ID}"
}