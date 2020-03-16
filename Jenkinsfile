pipeline {

    agent {
        docker { image 'node:10-alpine' }
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

        stage('Archive Artifact'){
            steps{
                sh 'npm pack | tail -n 1'
                archiveArtifacts artifacts: '**/test-results.xml', fingerprint: true
                archiveArtifacts artifacts: '**/movie-analyst-api-*.tgz', fingerprint: true
            }
        }       
    }

    post {
        always {
            junit '**/*.xml'
        }
    }
}
