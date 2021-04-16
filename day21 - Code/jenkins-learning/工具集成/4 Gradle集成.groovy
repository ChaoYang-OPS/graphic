pipeline{
   agent any
   
   stages{
   
       stage("mavenbuild"){
                steps{
                    script{
                        def mvnHome = '/usr/local/maven-3.6.3'
                        sh "${mvnHome}/bin/mvn  -v"
                    }
                }
        }

       stage("antbuild"){
                steps{
                    script{
                        def antHome = '/usr/local/ant-1.10.9'
                        sh "${antHome}/bin/ant  -version"
                    }
                }
        }
       stage("Gradlebuild"){
                steps{
                    script{
                        def antHome = '/usr/local/gradle-6.8.3'
                        sh "${antHome}/bin/gradle  -v"
                    }
                }
        }
    }
}