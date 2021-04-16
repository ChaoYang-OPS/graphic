/*
triggers 触发器
• 流水线的触发方式
• cron 定时触发: triggers { cron('H */7 * * 1-5') } 
• pollSCM: triggers { pollSCM('H */7 * * 1-5') }

(五颗星，中间用空格隔开）
第一颗表示分钟，取值0~59
第二颗表示小时，取值0~23
第三颗表示一个月的第几天，取值1~31
第四颗表示第几月，取值1~12
第五颗*表示一周中的第几天，取值0~7，其中0和7代表的都是周日
1.每30分钟构建一次：

H/30 * * * *

2.每2个小时构建一次

H H/2 * * *

3.每天早上8点构建一次

0 8 * * *

4.每天的8点，12点，22点，一天构建3次

0 8,12,22 * * *

*/

/*
 根据上游项目的状态触发
triggers { 
    upstream(upstreamProjects: 'job1,job2', 
             threshold: hudson.model.Result.SUCCESS) 
}

*/


// 每三分钟构建一次

pipeline{
    agent {label "build"}
    triggers {
        cron('H/3 * * * *')
    }

    stages{
        stage("cront_build"){
            steps{
                echo "Hello cront_build"
            }
        }
    }
}

// 这里面就是指定上游的项目，这个项目如果成功了，才会去触发当前的项目。
pipeline{
    agent {label "build"}
    triggers {
        upstream(upstreamProjects: 'demo-pipeline', threshold: hudson.model.Result.SUCCESS) 
    }

    stages{
        stage("cront_build"){
            steps{
                echo "Hello cront_build"
            }
        }
    }
}
