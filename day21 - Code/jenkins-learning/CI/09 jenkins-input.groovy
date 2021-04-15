/*
input 流水线交互
参数解析
• message: 提示信息
• ok: 表单中确认按钮的文本
• submitter: 提交人，默认所有人可以
• parameters： 交互时用户选择的参数
*/

pipeline{
    agent { label "build" }
    stages{
        stage("deploy"){
            input {
                message "是否继续发布"
                ok "Yes"
                submitter "admin,dev"
                parameters {
                    string(defaultValue: 'DEV', description: '选择发布的环境', name: 'env_name', trim: true)
                }


            }
            steps{
                echo "deploy to ${env_name} ......."
            }
        }
    }
}