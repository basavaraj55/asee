pipeline {
    agent any

    stages {
        stage('Execute stats.py') {
            steps {
                sh '''
                echo "Listing files in workspace:"
                ls -l

                echo "Running stats.py"
                python3 stats.py
                '''
            }
        }
    }
}
