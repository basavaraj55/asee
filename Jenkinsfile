node {

    stage('Checkout Repository') {
        git branch: 'main',
            url: 'https://github.com/basavaraj55/asee.git'
    }

    stage('Requirement Analysis') {
        echo 'Requirement analysis completed'
    }

    stage('Design') {
        echo 'Design completed'
    }

    stage('Run Repo Python File') {
        sh '''
        echo "Running Python file from repository"
        ls -l
        python3 add.py
        '''
    }

    stage('Build') {
        echo 'Build completed'
    }

    stage('Test') {
        echo 'Tests completed'
    }

    stage('Deploy') {
        echo 'Deployment completed'
    }
}
