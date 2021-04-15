pipeline {
    agent any 
    stages {
        stage('Example') {
            steps {
                echo "Hello, nice to meet you."

                script {
                    def browers = ['chrome', 'firefox']
                    for (int i = 0; i < browers.size(); i++) {
                        echo "Test the ${browers[i]} browser"
                    }
                }
            }
        }
    }
}