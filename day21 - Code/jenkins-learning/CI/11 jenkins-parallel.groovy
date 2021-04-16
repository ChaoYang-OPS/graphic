/*
parallel 阶段并行
场景： 自动化测试，多主机并行发布。

*/

pipeline{
    agent { label "build" }

    stages{
        stage("parallel_stage"){
            failFast true
            parallel {
                stage("UAT"){
                    agent {
                        label "build"
                    }
                    steps {
                        echo "UAT......"
                    }
                }
                stage("PROD"){
                    agent {
                        label "build"
                    }
                    steps{
                        echo "PROD......"
                    }
                }
            }
        }
    }
}