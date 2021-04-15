pipeline{
   agent any
   
   stages{
   
       stage("Maven"){
                steps{
                    script{
                        def mvnHome = '/usr/local/maven-3.6.3'
                        sh "${mvnHome}/bin/mvn  -v"
                    }
                }
        }
    }
}
