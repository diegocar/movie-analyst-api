pipeline {

    agent {
        dockerfile true
    }

    stages {
        
        stage('Install dependencies Stage') { 
            steps {
                sh 'npm clean-install'
            }
        }
        stage('Test Stage'){
            steps{
                sh 'npm test'
            }
        }
        stage('Generate Artifact'){
            steps{
                sh 'npm pack | tail -n 1'
            }
        }
        stage('Archive Artifacts'){
            steps{
                archiveArtifacts artifacts: '**/movie-analyst-api-*.tgz', fingerprint: true
                archiveArtifacts artifacts: '**/test-results.xml', fingerprint: true
            }
        }
        stage('Deploying Artifact'){
            steps{
                sh 'chmod 400 DevopsDiegoKey.pem'
                sh 'scp -i "DevopsDiegoKey.pem" -o StrictHostKeyChecking=no movie-analyst-api-*.tgz ubuntu@3.15.28.24:/home/ubuntu/'
                sh 'ssh -i "DevopsDiegoKey.pem" -o StrictHostKeyChecking=no ubuntu@3.15.28.24 ls'
            }
        }
    }

    

    post {
        always {
            junit '**/*.xml'
        }
    }
}