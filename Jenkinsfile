pipeline {
    agent any

    environment {
        // Virtual environment directory
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/rinkugupta3/Playwright_Automation_DesignSetup'
            }
        }

        stage('Set up Python environment') {
            steps {
                // Install Python virtual environment
                sh 'python3 -m venv ${VENV_DIR}'  // Ensure correct Python version
                // Activate virtual environment and install dependencies
                sh '''
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Playwright Tests') {
            steps {
                // Activate virtual environment and run tests
                sh '''
                . ${VENV_DIR}/bin/activate
                pytest --headless --maxfail=1 --disable-warnings -v
                '''
            }
        }

        stage('Publish Results') {
            steps {
                // Publish test results (ensure correct path)
                junit '**/reports/*.xml'
            }
        }
    }

    post {
        always {
            // Cleanup (optional, depends on your use case)
            sh 'deactivate || true'
            deleteDir()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
