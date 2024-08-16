pipeline {
    agent any

    environment {
        // Define the path to Python and Playwright
        PYTHON_PATH = "C:/Users/dhira/AppData/Local/Programs/Python/Python311/python.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rinkugupta3/Playwright_Automation_DesignSetup'
            }
        }
        stage('Set up Python environment') {
            steps {
                bat "${PYTHON_PATH} -m pip install -r requirements.txt"
            }
        }
        stage('Install Playwright Browsers') {
            steps {
                bat "${PYTHON_PATH} -m playwright install"
            }
        }
        stage('Run Playwright Tests - Dev Environment') {
            environment {
                ENV = 'dev'
            }
            steps {
                script {
                    // Set environment variable for Dev environment
                    bat "set ENV=dev && ${PYTHON_PATH} -m pytest"
                }
            }
        }

        stage('Run Playwright Tests - Staging Environment') {
            environment {
                ENV = 'staging'
            }
            steps {
                script {
                    // Set environment variable for Staging environment
                    bat "set ENV=staging && ${PYTHON_PATH} -m pytest"
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Archive the screenshots from the 'screenshots' directory
            archiveArtifacts artifacts: 'screenshots/**/*', allowEmptyArchive: true
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
