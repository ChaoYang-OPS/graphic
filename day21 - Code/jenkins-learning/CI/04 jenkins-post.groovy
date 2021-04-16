/*
post 构建后操作
• 定义： 根据流水线的最终状态匹配后做一些操作。
• 状态：
• always：  不管什么状态总是执行
• success： 仅流水线成功后执行
• failure：   仅流水线失败后执行
• aborted： 仅流水线被取消后执行
• unstable：不稳定状态，单侧失败等等
*/


pipeline{
    .......
    post{
        always{
            script{
                println("流水线结束后，经常做的事情")
            }
        }
        success{
            script{
                println("流水线成功后，要做的事情")
            }
        }

        failure{
            script{
                println("流水线失败后，要做的事情")
            }
        }

        aborted{
            script{
                println("流水线取消后，要做的事情")
            }
        }
    }
}