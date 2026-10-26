
pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    }

    stages {
        stage('1. Checkout Source') {
            steps {
                echo 'Checking out PulseCart source code'
                checkout scm
            }
        }

        stage('2. Test Application') {
            steps {
                sh 'python3 -m py_compile app.py'
                sh 'grep -q "def health" app.py'
                echo 'Application checks passed'
            }
        }

        stage('3. Build Docker Image') {
            steps {
                sh 'minikube image build -t pulsecart:latest .'
            }
        }

        stage('4. Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s.yaml'
                sh 'kubectl rollout status deployment/pulsecart --timeout=180s'
            }
        }

        stage('5. Verify Deployment') {
            steps {
                sh 'kubectl get deployment pulsecart'
                sh 'kubectl get pods -l app=pulsecart'
                sh 'kubectl get service pulsecart-service'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: PulseCart CI/CD pipeline completed!'
        }
        failure {
            echo 'Pipeline failed. Check the Console Output for the error.'
        }
    }
}

