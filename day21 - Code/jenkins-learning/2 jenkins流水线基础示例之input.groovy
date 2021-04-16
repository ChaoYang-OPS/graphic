pipeline {
    agent any 
    stages {
        stage('Example') {
            input {
                message "Should we continue?"
                ok "Yes, we shoud"
                submitter "alice,bob"
                parameters {
                    string(name: 'PERSON', defaultValue: "Mr jenkins", description: 'Who should I say he')

                }
            }
            steps {
                echo "Hello, ${PERSON}, nice to meet you."
            }
        }
    }
}