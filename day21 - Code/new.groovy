

// import share lib
@Library('demo-jenkins-lib') _

def tools = new com.opsk8s.tools()
def mail = new com.opsk8s.mails()
def sonar = new com.opsk8s.sonar()

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
  tools.print_core_msg("The build is triggered automatically", "green")
  def data = readJSON text: "${generic_webhook_data}"
  env.branche_name = data["ref"] - "refs/heads/"
  env.git_http_url = data["project"]["git_http_url"]
  env.user_email = data["user_email"]
  env.user_username = data["user_username"]
  env.trigger_type = "automatically"
}
catch(Exception e) {
  println(e)
  tools.print_core_msg("The build is triggered manually","green")
  env.trigger_type = "manually"
}

String branche_name = "${env.branche_name}"
String git_http_url = "${env.git_http_url}"
String build_type = "${env.build_type}"
String build_command = "${env.build_command}"
String skip_code_scan = "${env.skip_code_scan}"
String git_http_credentials_id = "${env.git_http_credentials_id}"
String sonar_server_credentials_id = "${env.sonar_server_credentials_id}"
String sonar_http_server_url = "${env.sonar_http_server_url}"
String build_run_jenkins_agent_node = "${env.build_run_jenkins_agent_node}"
String scan_scm_code_dir = "src"
String nexus3_submitter_approve = "admin,dev"
String aliyun_submitter_approve = "admin,dev"
String nexus3_server_credentials_id = "${nexus3_server_credentials_id}"
String nexus3_http_server_url = "${nexus3_http_server_url}"
String aliyun_server_server_url = "${aliyun_server_server_url}"
String aliyun_server_credentials_id = "${aliyun_server_credentials_id}"
String aliyun_register_server_namespace = "${aliyun_register_server_namespace}"

pipeline{
    agent {label "${build_run_jenkins_agent_node}"}
    parameters {
        string defaultValue: 'http://172.16.100.120/opsk8s/demo-springboot-service.git',
        description: 'The project code GIT address Example: http://172.16.100.120/opsk8s/demo-springboot-service.git',
        name: 'git_http_url', trim: true

        string defaultValue: 'master', description: 'branche_name , eg: master', name: 'branche_name', trim: true

        choice choices: ['maven', 'gradle', 'nodejs'], description: 'build type', name: 'build_type'

        string defaultValue: 'mvn clean package -Dmaven.test.skip=true', description: 'build command , eg: mvn clean package', name: 'build_command', trim: true

        choice choices: ['true', 'false'], description: 'Whether to skip the code scan ，false apply  code scan', name: 'skip_code_scan'

        string defaultValue: 'ddf5f4aa-2ceb-46c0-a284-67a8945ac00f', description: 'git_http_credentials_id， eg: ddf5f4aa-2ceb-46c0-a284-67a8945ac00f', name: 'git_http_credentials_id', trim: true

        string defaultValue: '67846d02-451c-43cb-b532-4327dec32972', description: 'sonar_server_credentials_id eg: ddf5f4aa-2ceb-46c0-a284-67a8945ac00f', name: 'sonar_server_credentials_id', trim: true

        string defaultValue: 'http://172.16.100.120:9000', description: 'sonar_server_credentials_id eg: http://sonar.opsk8s.com:80', name: 'sonar_http_server_url', trim: true

        string defaultValue: 'build01', description: 'run jenkins build job host', name: 'build_run_jenkins_agent_node', trim: true
        password defaultValue: '123', description: '123', name: 'test_pwd'
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
                    tools.get_current_trigger_type("${env.trigger_type}")
                    tools.get_scm_code("${git_http_url}","${branche_name}","${git_http_credentials_id}")
                }
            }
            post {
                success {
                    script{
                        tools.print_core_msg("check SCM Code successful!!!","green")
                    }
                }
                failure {
                    script{
                        tools.print_core_msg("check SCM Code failure!!!","red")
                        // error "check SCM Code failure!!!, Exit....."
                    }
                }
            }
        }
        stage("Build SCM Code"){
            steps{
                script{
                    tools.build_scm_code("${build_type}", "${build_command}")
                }
            }
        }
        stage("Scan SCM Code"){
            when{
                environment name: 'skip_code_scan', value: 'false'
            }
            steps{
                script{
                    project_version = tools.get_create_version_time()
                    // println("${project_version}")
                    withCredentials([string(credentialsId: "${sonar_server_credentials_id}", variable: "SONAR_ADMIN_TOKEN")]) {
                        sonar.sonar_scm_code("${build_type}", "${scan_scm_code_dir}","${sonar_http_server_url}", "${SONAR_ADMIN_TOKEN}", "${project_version}")
                    }
                }
            }
        }
        stage("Build Images"){
            steps{
                script{

                    tools.docker_login_to_nexus_register_server("${nexus3_http_server_url}","${nexus3_server_credentials_id}")
                    tools.build_image("${build_type}","${nexus3_http_server_url}","${JOB_NAME.toLowerCase()}", "${branche_name}")
                }
            }
        }
        stage("Push Images to Nexus"){
            options{
                timeout(time: 5, unit: 'MINUTES')
                timestamps()
            }
            input {
                message "upload_image_to_nexus"
                ok "Yes"
                submitter "${nexus3_submitter_approve}"
                parameters {
                    choice(choices: ['Yes', 'No'], description: '', name: 'upload_image_to_nexus')
                }
            }
            when {
                environment name: 'upload_image_to_nexus', value: 'Yes'
            }
            steps{
                script{
                    tools.docker_login_to_nexus_register_server("${nexus3_http_server_url}", "${nexus3_server_credentials_id}")
                    tools.push_image_to_nexus("${nexus3_http_server_url}", "${JOB_NAME.toLowerCase()}", "${env.image_tag}")
                }
            }
        }
        stage("Push Images to Aliyun"){
            options{
                timeout(time: 5, unit: 'MINUTES')
                timestamps()
            }
            input {
                message "upload_image_to_Aliyun"
                ok "Yes"
                submitter "${aliyun_submitter_approve}"
                parameters {
                    choice(choices: ['Yes', 'No'], description: '', name: 'upload_image_to_aliyun')
                }
            }
            when{
                environment name: 'upload_image_to_aliyun', value: 'Yes'
            }
            steps{
                script{
                    tools.docker_login_to_register_server("${aliyun_server_server_url}","${aliyun_server_credentials_id}")
                    tools.push_image_to_aliyun("${aliyun_server_server_url}", "${aliyun_register_server_namespace}", "${JOB_NAME.toLowerCase()}", "${env.image_tag}")
                }
            }
        }
        stage("Get Image Scan result for Aliyun"){
            steps{
                script{
                    tools.print_core_msg("Get Image Scan result for Aliyun, please wait ........", "green")
                }
            }
        }
    }
    post{
        always{
            script{
                mail.mail_send_build_info("${env.user_email}", "${currentBuild.currentResult}")
                cleanWs()
            }
        }
    }
}
