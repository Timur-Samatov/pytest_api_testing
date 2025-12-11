pipeline {
    agent any
    
    environment {
        POETRY_VERSION = '1.8.0'
        POETRY_HOME = '/var/jenkins_home/.poetry'
        POETRY_BIN = '/var/jenkins_home/.poetry/bin'
        PATH = "${env.POETRY_BIN}:${env.PATH}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Poetry') {
            steps {
                script {
                    // Install Poetry if not already installed
                    sh '''
                        if ! command -v poetry &> /dev/null; then
                            echo "Installing Poetry..."
                            curl -sSL https://install.python-poetry.org | python3 -
                        else
                            echo "Poetry already installed"
                            poetry --version
                        fi
                    '''
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "Installing dependencies..."
                    poetry install --with dev --no-root
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    echo "Running tests with pytest..."
                    poetry run pytest tests/ -v --tb=short
                '''
            }
            post {
                always {
                    // Archive test results if using junit format
                    // publishTestResults testResultsPattern: 'test-results.xml'
                    echo "Test execution completed"
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}