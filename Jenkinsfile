pipeline {
    agent any

    environment {
        IMAGE_NAME = "basawarajss/python-add"
        IMAGE_TAG  = "latest"
        CONTAINER  = "python_add_container"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                echo "Building Docker image..."
                docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                echo "Pushing image to Docker Hub..."
                docker push $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                echo "Removing old container if exists..."
                docker rm -f $CONTAINER || true

                echo "Running container..."
                docker run --name $CONTAINER $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build + Push + Run pipeline completed successfully'
        }
        failure {
            echo '❌ Pipeline failed'
        }
    }
}
