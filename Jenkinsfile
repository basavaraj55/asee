pipeline {
    agent any

    stages {
        stage('Check Base Directory') {
            steps {
                script {
                    def baseDir = "/var/lib/jenkins/asee"
                    def newDir  = "${baseDir}/build_${env.BUILD_NUMBER}"
                    def newFile = "${newDir}/info.txt"

                    if (fileExists(baseDir)) {
                        echo "✅ Base directory exists: ${baseDir}"

                        // Create new directory
                        sh "mkdir -p ${newDir}"
                        echo "✅ New directory created: ${newDir}"

                        // Create file inside new directory
                        sh "echo 'File created by Jenkins build ${env.BUILD_NUMBER}' > ${newFile}"
                        echo "✅ File created: ${newFile}"

                    } else {
                        error "❌ Base directory does NOT exist: ${baseDir}. Failing build."
                    }
                }
            }
        }

        stage('Build Stage') {
            steps {
                echo "✅ Build completed successfully"
            }
        }
    }
}
``
