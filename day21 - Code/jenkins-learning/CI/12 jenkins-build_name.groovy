// 设置构建名称

pipeline{
    agent {label "build"}

    stages{
        stage("cront_build"){
          
            steps{
                wrap([$class: 'BuildUser']){
                    buildName "[${BUILD_USER}-${BUILD_NUMBER}]"
                }
                echo "Hello cront_build"
                sh "printenv"
                
            }
        }
    }
}