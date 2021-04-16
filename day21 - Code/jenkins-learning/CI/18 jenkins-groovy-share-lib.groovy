/*在Jenkinsfile中使用@Library('demo-jenkins-lib') _ 来加载共享库，注意后面符号_用于加载。 
类的实例化def my_tools = new com.opsk8s.tools(),使用类中的方法 `mytools.print_msg(msg)`  。
*/


@Library('demo-jenkins-lib') _

def my_tools = new com.opsk8s.tools()


pipeline{
    agent {label "build"}
    stages{
        stage("build"){
            steps{
                script{
                    message = "Jenkins share lib ....."
                    my_tools.print_msg(message)
                }
            }
        }
    }
}


/*
共享库扩展
共享库加载
*/
// 加载demo-jenkins-lib共享库
@Library('demo-jenkins-lib') _
// 加载demo-jenkins-lib共享库的1.0版本
@Library('demo-jenkins-lib@1.0') _
// 加载多个共享库， demo-jenkins-lib共享库的默认版本， yourlib共享库的2.0版本（分支）
@Library(['demo-jenkins-lib', 'yourlib@2.0']) _