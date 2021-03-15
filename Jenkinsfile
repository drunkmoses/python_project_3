pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('0,30 * * * *')])])
                }
                sh 'git clone https://github.com/drunkmoses/python_project_1.git'
            }
        }
    }
}
