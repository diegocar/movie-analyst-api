pipeline {

    agent {
        docker { image 'node:10-alpine' }
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
        stage('Probando'){
            steps{
                sh 'scp -i "DevopsDiegoKey.pem" **/movie-analyst-api-*.tgz ubuntu@3.15.28.24:/home/ubuntu/'
            }
        }       
    }

    post {
        always {
            junit '**/*.xml'
        }
    }
}
