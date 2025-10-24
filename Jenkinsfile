pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'iris-ml-app'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from repository...'
                checkout scm
            }
        }
        
        stage('Build Docker Image with Tests') {
            steps {
                echo 'Building Docker image (tests run during build)...'
                sh """
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                """
            }
        }
        
        stage('Run Container Test') {
            steps {
                echo 'Testing container...'
                sh """
                    docker run --rm ${DOCKER_IMAGE}:latest
                """
            }
        }
        
        stage('Clean Up') {
            steps {
                echo 'Cleaning up old images...'
                sh """
                    docker image prune -f
                """
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully! ✅'
        }
        failure {
            echo 'Pipeline failed! ❌'
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}