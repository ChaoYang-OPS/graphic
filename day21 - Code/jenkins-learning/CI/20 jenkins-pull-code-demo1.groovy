


String branche_name = "${env.branche_name}"
String git_http_url = "${env.git_http_url}"
pipeline{
    agent {label "build"}
    parameters {
        string defaultValue: 'http://172.16.100.120/opsk8s/demo-springboot-service.git',
        description: 'The project code GIT address Example: http://172.16.100.120/opsk8s/demo-springboot-service.git',
        name: 'git_http_url', trim: true

    }

    stages{
        stage("Get SCM Code"){
            steps{
                script{
                    checkout([$class: 'GitSCM', branches: [[name: "${branche_name}"]],
                    extensions: [], userRemoteConfigs: [[credentialsId: 'ddf5f4aa-2ceb-46c0-a284-67a8945ac00f',
                    url: "${git_http_url}"]]])
                }
            }
        }
    }
}
