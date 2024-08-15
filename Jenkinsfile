pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository from Git
                git 'https://github.com/rinkugupta3/Playwright_Automation_DesignSetup'
            }
        }
        stage('Set up Python environment') {
            steps {
                // Ensure Python is installed and set up your environment
                script {
                    def pythonPath = "C:\\Python39"  // Update with your Python path
                    def pythonExe = "${pythonPath}\\python.exe"

                    // Verify Python installation
                    bat "${pythonExe} --version"

                    // Install dependencies (if needed)
                    bat "${pythonExe} -m pip install -r requirements.txt"
                }
            }
        }
        stage('Run Playwright Tests') {
            steps {
                // Run your Playwright tests
                script {
                    def pythonPath = "C:\\Python39"  // Update with your Python path
                    def pythonExe = "${pythonPath}\\python.exe"

                    // Run your test script (update 'test_script.py' with your actual script)
                    bat "${pythonExe} -m playwright test"
                }
            }
        }
    }
    post {
        always {
            // This block will always run, regardless of the pipeline status
            echo 'Cleaning up...'
            // Any clean-up steps you need to perform
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
