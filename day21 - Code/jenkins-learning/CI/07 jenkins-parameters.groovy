/*parameters 流水线参数
• 定义： 流水线在运行时设置的参数，UI页面的参数。所有的参数都存储在params对象中。
• 将web ui页面中定义的参数，以代码的方式定义。
*/
pipeline { 
    agent {label "build"}

    parameters {
       string defaultValue: '9.9.9', description: '发布可用版本', name: 'release_version', trim: true
    }

    stages{
        stage("Build"){
            steps{
                echo "release_version=${params.release_version}"
                //echo "release_version ------- ${release_version}"
            }
        }
    }
}