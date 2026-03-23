pipeline {
    agent any

    stages {
        stage('Create Directory and File') {
            steps {
                script {
                    def baseDir = "/var/lib/jenkins/ase"
                    def newDir  = "${baseDir}/build_${env.BUILD_NUMBER}"
                    def newFile = "${newDir}/info.txt"

                    echo "Creating directory..."
                    sh "mkdir -p ${newDir}"

                    echo "Creating file inside directory..."
                    sh "echo 'File created by Jenkins build ${env.BUILD_NUMBER}' > ${newFile}"

                    echo "Directory and file created successfully"
                }
            }
        }
    }
}
