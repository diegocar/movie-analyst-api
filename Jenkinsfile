pipeline {

    agent {
        dockerfile true
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
                sh 'scp -i "DevopsDiegoKey.pem" -o StrictHostKeyChecking=no movie-analyst-api-*.tgz ubuntu@3.22.98.106:/home/ubuntu/'
                sh 'ssh -i "DevopsDiegoKey.pem" -o StrictHostKeyChecking=no ubuntu@3.22.98.106 tar -xvzf /home/ubuntu/movie-analyst-api-1.0.0.tgz'
                sh 'ssh -i "DevopsDiegoKey.pem" -o StrictHostKeyChecking=no ubuntu@3.22.98.106 ls'
    }
}
        stage("Connecting with S3"){
            steps{
                withAWS(region:'us-east-2',credentials:'e1850337-9311-434f-88f5-32e3326df4b3') {
                    s3Upload(bucket: 'backs3',  path:'Back/', includePathPattern:'**/*.xml');
                }
            }
        }

        stage("Debian"){
            steps{
                sh 'alien -d movie-analyst-api-*.tgz'
            }
        }
    }

    post {
        always {
            junit '**/*.xml'
        }
    }
}
