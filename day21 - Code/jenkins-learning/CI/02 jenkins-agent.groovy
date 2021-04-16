

/*
agent构建节点
 1、 any: 运行在任一可用节点
 2、 none: 当pipeline全局指定agent为none,则根据每个stage中定义的agent运行(stage必须指定)
 3、 label: 在指定的标签的节点运行。(标签=分组)
 4、 node: 支持自定义流水线的工作目录

*/
 // 一
pipeline{
    agent any
}

// 二

pipeline{
    agent {label "label name"}
}

// 三 自定义节点

pipeline {
    agent {
        node {
            label "label name",
            customWorkspace "/opt/jenkins-agent/workspace"
        }
    }
}



