pipeline {
    agent any

    stages {
        stage('Check & Create Directory') {
            steps {
                script {
                    def baseDir = "/var/lib/jenkins/asee"
                    def newDir  = "${baseDir}/build_${env.BUILD_NUMBER}"

                    if (fileExists(baseDir)) {
                        echo "✅ Base directory exists: ${baseDir}"

                        sh "mkdir -p ${newDir}"
                        echo "✅ New directory created: ${newDir}"
                    } else {
                        error "❌ Base directory does NOT exist: ${baseDir}. Failing build."
                    }
                }
            }
        }

        stage('Build Stage') {
            steps {
                echo "✅ Build running after directory creation"
            }
        }
    }
}
