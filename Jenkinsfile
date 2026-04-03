pipeline {
    agent any

    environment {
        IMAGE_NAME = "basawarajss/python-alg"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Generate Version Tag') {
            steps {
                script {
                    env.IMAGE_TAG = sh(
                        script: "date +%Y%m%d%H%M%S",
                        returnStdout: true
                    ).trim()

                    env.CONTAINER_NAME = "python_alg_container_${env.IMAGE_TAG}"

                    echo "Image Tag: ${env.IMAGE_TAG}"
                    echo "Container Name: ${env.CONTAINER_NAME}"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                """
            }
        }

        stage('Tag as Latest') {
            steps {
                sh """
                docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest
                """
            }
        }

        stage('Push Docker Image') {
            steps {
                sh """
                docker push ${IMAGE_NAME}:${IMAGE_TAG}
                docker push ${IMAGE_NAME}:latest
                """
            }
        }

        stage('Run New Container (Detached)') {
            steps {
                sh """
                docker run -d --name ${CONTAINER_NAME} ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }
    }

    post {
        success {
            echo "✅ alg.py image and container created successfully"
            echo "Image: ${IMAGE_NAME}:${IMAGE_TAG}"
            echo "Container: ${CONTAINER_NAME}"
        }
        failure {
            echo "❌ Pipeline failed"
        }
    }
}
