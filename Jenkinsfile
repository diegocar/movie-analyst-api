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
    }

    

    post {
        always {
            junit '**/*.xml'
        }
    }
}

def remote = [:]
    remote.name = 'A Master'
    remote.host = '3.15.28.24'
    remote.user = 'ubuntu'
    remote.allowAnyHosts = true
    remote.identityFile = "/var/jenkins_home/workspace/Primer-pipeline/DevopsDiegoKey.pem"

    node{
        stage('Remote SSH') {
            sshCommand remote: remote, sudo: true, command: "ssh -i "/var/jenkins_home/workspace/Primer-pipeline/DevopsDiegoKey.pem" ubuntu@3.15.28.24 pwd"
        }
    }