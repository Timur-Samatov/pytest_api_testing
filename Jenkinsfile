pipeline {
    agent any
    
    environment {
        POETRY_HOME = "${env.WORKSPACE}/.poetry"
        POETRY_BIN = "${env.WORKSPACE}/.poetry/bin"
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
                    // Check if Poetry is already available system-wide
                    def poetryExists = sh(script: 'command -v poetry', returnStatus: true) == 0
                    
                    if (poetryExists) {
                        echo "Poetry found in system PATH"
                        sh 'poetry --version'
                    } else {
                        echo "Installing Poetry to workspace..."
                        sh '''
                            export POETRY_HOME="${WORKSPACE}/.poetry"
                            curl -sSL https://install.python-poetry.org | python3 -
                            export PATH="${WORKSPACE}/.poetry/bin:$PATH"
                            poetry --version
                        '''
                    }
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "Installing dependencies..."
                    export PATH="${WORKSPACE}/.poetry/bin:$PATH"
                    poetry install --with dev --no-root
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    echo "Running tests with pytest..."
                    export PATH="${WORKSPACE}/.poetry/bin:$PATH"
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