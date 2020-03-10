pipeline {
    
    agent {
        docker { image 'node:7-alpine' }
    }

    stages {
        
        stage('Install dependencies Stage') { 
            steps {
                sh 'npm install'
            }
        }
        stage('Test Stage'){
            steps{
                sh 'npm test'
            }
        }

    }
}