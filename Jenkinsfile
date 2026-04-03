pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "basawarajss/python-stats"
        DOCKER_TAG   = "latest"
    }

    stages {
        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                echo "Building Docker image..."
                docker build -t $DOCKER_IMAGE:$DOCKER_TAG .
                '''
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                sh '''
                echo "Pushing Docker image to Docker Hub..."
                docker push $DOCKER_IMAGE:$DOCKER_TAG
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Docker image built and pushed successfully'
        }
        failure {
            echo '❌ Pipeline failed'
        }
    }
}
