pipeline {
    agent any

    stages {
        stage('Check Directory') {
            steps {
                script {
                    def dirPath = "/var/lib/jenkins/asee"

                    if (fileExists(dirPath)) {
                        echo "Directory exists: ${dirPath}"
                    } else {
                        error "Directory does NOT exist: ${dirPath}. Failing build."
                    }
                }
            }
        }

        stage('Build Stage') {
            steps {
                echo "Build is running because directory exists"
            }
        }
    }
}
