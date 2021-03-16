def checkOs(){
    if (isUnix()) {
        def uname = sh script: 'uname', returnStdout: true
        if (uname.startsWith("Darwin")) {
            return "Macos"
        }
        else {
            return "Linux"
        }
    }
    else {
        return "Windows"
    }
}

pipeline {
    agent any
    stages {
        stage('cleanup before start') {
            steps {
                sh 'rm -rf .git'
            }
        }
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('0,30 * * * *')])])
                }
                sh 'git https://github.com/drunkmoses/python_project_1.git'
            }
        }
        stage('run rest app') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start /min python rest_app.py'
                    } else {
                        sh 'nohup python rest_app.py &'
                    }
                }
            }
        }
        stage('run web app') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start /min python web_app.py'
                    } else {
                        sh 'nohup python web_app.py &'
                    }
                }
            }
        }
    }
}
