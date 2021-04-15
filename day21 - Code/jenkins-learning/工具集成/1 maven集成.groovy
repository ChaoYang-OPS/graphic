pipeline {
    agent any 
    stages {
        stage("mavenBuild"){
            steps{
                script{
                    def mvnHome = tool 'MAVEN'
                    sh "${mvnHome}/bin/mvn  -v "
                }
            }
        }
    }
}