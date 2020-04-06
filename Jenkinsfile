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
        stage("Connecting with S3"){
            steps{
                withAWS(region:'us-east-2',credentials:'bcfaed0c-5e68-426d-bcbe-fce1c68d0fbf') {
                    s3Upload(bucket: 'backs3',  path:'Back/', includePathPattern:'**/*.xml');
                }
            }
        }

        stage("Debian"){
            steps{
                debianPbuilder additionalBuildResults: '', architecture: '', distribution: 'back', keyring: '', mirrorSite: 'https://github.com/diegocar/movie-analyst-api'
            }
        }
    }

    post {
        always {
            junit '**/*.xml'
        }
    }
}
