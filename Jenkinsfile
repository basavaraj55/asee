pipeline {
    agent any

    stages {
        stage('Create Directory and File') {
            steps {
                script {
                    def baseDir = "/var/lib/jenkins/asee"
                    def newDir  = "${baseDir}/build_${env.BUILD_NUMBER}"
                    def newFile = "${newDir}/info.txt"

