/*
// 设置保存最近的记录
options { buildDiscarder(logRotator(numToKeepStr: '1')) }

// 禁止并行构建
options { disableConcurrentBuilds() }


// 跳过默认的代码检出
options { skipDefaultCheckout() }


// 设定流水线的超时时间(可用于阶段级别)
options { timeout(time: 1, unit: 'HOURS') }


// 设定流水线的重试次数(可用于阶段级别)
options { retry(3) }


// 设置日志时间输出(可用于阶段级别)
options { timestamps() }

*/

// 参考,需要安装插件Timestamper，如果没有生效需要重启Jenkins服务

pipeline{
    agent {label "build"}
    options{
        disableConcurrentBuilds()
        skipDefaultCheckout()
        timeout(time: 1, unit: 'HOURS')
    }

    stages{
        stage("build"){
            options{
                timeout(time: 5, unit: 'MINUTES')
                retry(3)
                timestamps()
                
            }
            steps{
                echo "Build"
            }
        }
    }
}
