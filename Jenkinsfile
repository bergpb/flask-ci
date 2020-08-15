pipeline {
    agent any
    environment {
        FLASK_ENV = 'TESTING'
        FLASK_APP = 'app.py'
        DEBUG = true
	}
    stages {
        stage('Checkout') {
            steps {
                git "https://github.com/bergpb/flask-ci.git"
            }
        }
        stage ("Install Dependencies") {
            steps {
                sh """
                python3 -m venv .venv
                . .venv/bin/activate
                pip install --upgrade pip
                pip install -r ${env.WORKSPACE}/requirements.txt
                """
            }
        }
        stage('Run Tests') {
            steps {
                sh """
                . .venv/bin/activate
                echo "Running the unit test..."
                make test
                """
            }
        }
        stage('Run Coverage') {
            steps {
                sh """
                . .venv/bin/activate
                echo "Generating coverage..."
                make coverage
                """
            }
        }
    }
    post {
        always {
            cleanWs()
        }
        success {
            echo "Success"
        }
        failure {
            echo "Send e-mail, when failed"
        }
    }
}
