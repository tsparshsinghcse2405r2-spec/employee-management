pipeline {
    agent any

    environment {
        PATH = "C:\\anaconda;C:\\anaconda\\Scripts;C:\\anaconda\\Library\\bin;${env.PATH}"
    }

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
            junit allowEmptyResults: true, testResults: 'results.xml'
        }
        success {
            echo 'All tests passed.'
        }
        failure {
            echo 'Build failed: one or more tests failed.'
        }
    }
}