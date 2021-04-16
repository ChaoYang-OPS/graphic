/*
when 阶段运行控制
判断条件
• 根据环境变量判断
• 根据表达式判断
• 根据条件判断（not/allOf/anyOf）
*/

// 根据环境变量判断
pipeline{
    agent {label "build"}

    stages{
        stage("build"){
            steps{
                echo "build .........."
            }
        }
        stage("deploy"){
            when {
                environment name: 'env_name', value: 'UAT'
            }
            steps{
                echo "deploy ${env_name}......... "
            }
        }
    }
}

// 根据条件判断 allOf 条件全部成立

pipeline{
    agent {label "build"}

    stages{
        stage("build"){
            steps{
                echo "build ........."
            }
        }
        stage("deploy"){
            when {
                allOf {
                    environment name: 'env_name', value: 'UAT'
                    environment name: 'release_version', value: '6.6.6'
                }
            }
            steps{
                echo "deploy ${env_name}----->${release_version}.........."
            }
        }
    }
}


// 根据条件判断 anyOf 条件其中一个成立

pipeline{
    agent {label "build"}

    stages{
        stage("build"){
            steps{
                echo "build ........."
            }
        }
        stage("deploy"){
            when {
                anyOf {
                    environment name: 'env_name', value: 'UAT'
                    environment name: 'release_version', value: '6.6.6'
                }
            }
            steps{
                echo "deploy ${env_name}----->${release_version}.........."
            }
        }
    }
}






