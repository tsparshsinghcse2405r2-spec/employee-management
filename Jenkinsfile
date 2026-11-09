pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'python -m pytest --junitxml=results.xml --cov=employee'
            }
        }
    }
    post {
        always {
            junit 'results.xml'
        }
        success {
            echo 'All tests passed.'
        }
        failure {
            echo 'Build failed: one or more tests failed.'
        }
    }
}
