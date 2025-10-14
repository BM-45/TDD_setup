pipeline {
    agent any

    environment {
        PYTHON = "python"
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/BM-45/TDD_setup.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat """
                %PYTHON% -m venv %VENV_DIR%
                call %VENV_DIR%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install pytest flake8 coverage
                """
            }
        }

        stage('Lint Code') {
            steps {
                bat """
                call %VENV_DIR%\\Scripts\\activate
                flake8 *.py
                """
            }
        }

        stage('Run Tests with Coverage') {
            steps {
                bat """
                call %VENV_DIR%\\Scripts\\activate
                coverage run -m pytest --junitxml=test-results.xml -v
                coverage report
                coverage html
                """
            }
        }
    }

    post {
        always {
            // Publish test results to Jenkins
            junit 'test-results.xml'
            archiveArtifacts artifacts: 'htmlcov/**', fingerprint: true
        }
    }
}
