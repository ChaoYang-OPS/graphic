/*
stages构建阶段
• 关系： stages > stage > steps > script
• 定义：
• stages：包含多个stage阶段
• stage：包含多个steps步骤
• steps: 包含一组特定的脚本（加上script后就可以实现在声明式脚本中嵌入脚本式语法了）
*/


pipeline {
    agent { label "build"}

    stages{
        stage("build"){
            steps{
                echo "Hello Yang"
            }
        }
    }
}

// 扩展: 在阶段中定义agent

pipeline{
    agent none

    stages{
        stage("build"){
            agent { label "build"}
            steps{
                echo "loading build........"
            }
        }
    }
}