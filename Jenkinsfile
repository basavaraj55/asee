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
                    // Generate timestamp-based tag
                    IMAGE_TAG = sh(
                        script: "date +%Y%m%d%H%M%S",
                        returnStdout: true
                    ).trim()

                    CONTAINER_NAME = "python_alg_container_${IMAGE_TAG}"

                    echo "Generated Image Tag: ${IMAGE_TAG}"
                    echo "Container Name: ${CONTAINER_NAME}"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                echo "Building Docker image with tag ${IMAGE_TAG}"
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                """
            }
        }

        stage('Tag as Latest') {
            steps {
