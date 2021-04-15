/*env 构建时变量
• 定义： 通过键值对（k-v）格式定义流水线在运行时的环境变量， 分为流水线级别和阶段级别。
*/

//流水线级别环境变量参考

pipeline {
    agent {label "build"}
    environment{
        name = 'lsunstack'
        release_version = '6.6.6'
        env_name = 'UAT'
    }

    stages{
        stage("get_env"){
            steps{
                echo "name=${name} release_version=${release_version} env_name=${env_name}"
            }
        }
    }
}


// 阶段级别环境变量参考

pipeline {
    agent {label "build"}

    stages{
        stage("get_env"){
            environment {
                release_version = '8.8.8'
            }
            steps{
                script{
                    echo "${release_version}"
                }
            }
        }
    }
}