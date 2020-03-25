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
                sh 'sudo apk add --no-cache openssh'
                sh 'ssh -i "DevopsDiegoKey.pem" ubuntu@3.15.28.24 pwd'
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
    remote.name = 'Master'
    remote.host = '3.15.28.24'
    remote.user = 'ubuntu'
    remote.allowAnyHosts = true
    remote.identityFile = 'DevopsDiegoKey.pem'
    node{
        stage('Remote SSH') {
            sh 'chmod 400 DevopsDiegoKey.pem'
            sh 'ls -l'
            sshCommand remote: remote, sudo: true, command: "ssh ubuntu@3.15.28.24 pwd"
        }
    }