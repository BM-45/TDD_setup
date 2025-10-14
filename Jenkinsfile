pipeline {
  agent any
  environment {
    PYTHON   = 'C:\\Users\\bhanu mallik\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
    VENV_DIR = '.venv'
    ACTIVATE = "${VENV_DIR}\\Scripts\\activate"
  }

  stages {
    stage('Checkout') {
      steps {
        deleteDir()
        git branch: 'main', url: 'https://github.com/BM-45/TDD_setup.git'
        bat 'dir'
      }
    }

    stage('Setup Python Environment') {
      steps {
        bat """
          if not exist "${VENV_DIR}" "${PYTHON}" -m venv "${VENV_DIR}"
          call "${ACTIVATE}"
          where python
          python --version
          pip --version
          python -m pip install --upgrade pip
          if exist requirements.txt (
            pip install -r requirements.txt
          ) else (
            pip install pytest coverage
          )
        """
      }
    }

    stage('Run Tests with Coverage') {
      steps {
        bat """
          call "${ACTIVATE}"
          coverage run -m pytest -v --junitxml=test-results.xml
          coverage report
          coverage html
        """
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'htmlcov/**', fingerprint: true
      // Re-enable when JUnit plugin is installed:
      // junit allowEmptyResults: true, testResults: 'test-results.xml'
      echo 'Done'
    }
  }
}
