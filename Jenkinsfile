node {

    stage('Requirement Analysis') {
        sh '''
        python3 - << 'EOF'
        requirements = ["Login", "Dashboard", "Reports"]
        with open("requirements.txt", "w") as f:
            for r in requirements:
                f.write(r + "\\n")
        print("Requirements documented")
        EOF
        '''
    }

    stage('Design') {
        sh '''
        python3 - << 'EOF'
        with open("requirements.txt", "r") as f:
            req = f.read()

        design = "System Design based on requirements:\\n" + req
        with open("design.txt", "w") as f:
            f.write(design)

        print("Design completed")
        EOF
        '''
    }

    stage('Development') {
        sh '''
        python3 - << 'EOF'
        with open("app.py", "w") as f:
            f.write("print('Application running successfully')\\n")

        print("Code developed")
        EOF
        '''
    }

    stage('Build') {
        sh '''
        python3 - << 'EOF'
        import os
        if os.path.exists("app.py"):
            with open("build.txt", "w") as f:
                f.write("Build successful")
            print("Build successful")
        else:
            raise Exception("Build failed")
        EOF
        '''
    }

    stage('Testing') {
        sh '''
        python3 - << 'EOF'
        import subprocess

        result = subprocess.run(["python3", "app.py"], capture_output=True, text=True)

        if "successfully" in result.stdout:
            print("Tests passed")
        else:
            raise Exception("Tests failed")
        EOF
        '''
    }

    stage('Deployment') {
        sh '''
        python3 - << 'EOF'
        with open("build.txt", "r") as f:
            status = f.read()

        if "successful" in status:
            print("Application deployed successfully")
        else:
            raise Exception("Deployment failed")
        EOF
        '''
    }

    stage('Maintenance') {
        sh '''
        python3 - << 'EOF'
        print("Monitoring and maintenance in progress")
        EOF
        '''
    }
}
