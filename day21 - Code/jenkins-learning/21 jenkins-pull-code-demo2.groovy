

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