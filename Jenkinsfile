pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git clone 'https://github.com/drunkmoses/python_project_1.git'
            }
        }
    }
}
