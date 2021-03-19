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
        stage('cleanup and requirements before start') {
            steps {
                sh 'rm -rf .git'
                sh 'pip3 install flask'
                sh 'pip3 install selenium'
                sh 'pip3 install pymysql'

            }
        }
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('0,30 * * * *')])])
                }
                sh 'git clone https://github.com/drunkmoses/python_project_1.git'
            }
        }
        stage('run rest app') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start /min python3 rest_app.py'
                    } else {
                        sh 'nohup python3 rest_app.py &'
                    }
                }
            }
        }
        stage('run web app') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start /min python3 web_app.py'
                    } else {
                        sh 'nohup python3 web_app.py &'
                    }
                }
            }
        }
        stage('tests') {
            steps {
                sh 'backend_testing.py'
                sh 'frontend_testing.py'
                sh 'combined_testing.py'
            }
        }
        stage('cleanup') {
            steps {
                sh 'clean_environment.py'
                }
        }
    }
}

