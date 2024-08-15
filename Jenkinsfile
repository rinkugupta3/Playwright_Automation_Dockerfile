pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository from Git
                git branch: 'main', url: 'https://github.com/rinkugupta3/Playwright_Automation_DesignSetup'
            }
        }
        stage('Set up Python environment') {
            steps {
                script {
                    def pythonPath = "C:/Users/dhira/AppData/Local/Programs/Python/Python311"
                    def pythonExe = "${pythonPath}/python.exe"
                    // Verify Python installation
                    bat "${pythonExe} --version"
                    // Install dependencies (if needed)
                    bat "${pythonExe} -m pip install -r requirements.txt"
                }
            }
        }
        stage('Run Playwright Tests') {
            steps {
                script {
                    def pythonPath = "C:C:/Users/dhira/AppData/Local/Programs/Python/Python311"
                    def pythonExe = "${pythonPath}/python.exe"
                    // Run your Playwright tests
                    bat "${pythonExe} -m playwright test"
                }
            }
        }
    }
    post {
        always {
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