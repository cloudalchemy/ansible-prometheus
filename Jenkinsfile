#!groovy

/* Declarative pipeline */
pipeline {
  agent {
    node {
      label 'master'
      customWorkspace "workspace/${JOB_NAME.split('/')[1]}"
    }
  }
  options {
    disableConcurrentBuilds()
    buildDiscarder(logRotator(numToKeepStr: '30'))
    timeout(time: 15, unit: 'MINUTES')
  }
  environment {
    GIT_COMMITER = sh( script: "git show -s --pretty=%an", returnStdout: true ).trim()
    GIT_URL = sh( script: "git config --get remote.origin.url", returnStdout: true ).trim()
  }
  stages {
    stage('Check syntax') {
      steps {
        sh 'molecule syntax'
      }
    }
    stage('Provision environment') {
      steps {
        sh 'molecule create'
      }
    }
    stage('Run ansible') {
      steps {
        sh 'molecule converge'
      }
    }
    stage('Run Tests'){
      steps {
        sh 'molecule idempotence'
        sh 'molecule verify'
      }
    }
    stage('Add new tag and push it to repository'){
      when { branch "master" }
      steps {
        sh '''
          LAST=$(git log -1 --pretty=%B | head -n1)
          if [ $(expr "$LAST" : "Merge pull request.*/feature.*") -gt 0 ]; then 
            git tag $(git tag | sort | tail -n1 | awk -F '.' '{print $1"."($2+1)"."0}')
          else
            git tag $(git tag | sort | tail -n1 | awk -F '.' '{print $1"."$2"."($3+1)}')
          fi
        '''
        withCredentials([[$class: 'StringBinding', credentialsId: '84b13c41-cc5e-4802-b057-e85c232d347b', variable: 'GITHUB_TOKEN']]) {
          sh "git push https://${GITHUB_TOKEN}:@${GIT_URL.replace( 'https://', '')} --tags"
        }
      }
    }
    stage('Import to ansible galaxy'){
      when { branch "master" }
      steps {
        withCredentials([[$class: 'StringBinding', credentialsId: '84b13c41-cc5e-4802-b057-e85c232d347b', variable: 'GITHUB_TOKEN']]) {
          sh 'ansible-galaxy login --github-token $GITHUB_TOKEN'
          sh "ansible-galaxy import SoInteractive ${JOB_NAME.split('/')[1]}"
        }
      }
    }
  }

  post {
    always {
      sh 'molecule destroy'
      deleteDir()
    }
    success {
      mattermostSend color: 'good', message: "Pipeline <${RUN_DISPLAY_URL}|#${BUILD_NUMBER}> of <https://github.com/SoInteractive/${JOB_NAME.split('/')[1]}/tree/${BRANCH_NAME}|${JOB_NAME}> branch by ${GIT_COMMITER} finished successfully in ${currentBuild.durationString.replaceAll('and counting','')}"
    }
    failure {
      mattermostSend color: 'danger', message: "Pipeline <${RUN_DISPLAY_URL}|#${BUILD_NUMBER}> of <https://github.com/SoInteractive/${JOB_NAME.split('/')[1]}/tree/${BRANCH_NAME}|${JOB_NAME}> branch by ${GIT_COMMITER} failed in ${currentBuild.durationString.replaceAll('and counting','')}"
    }
  }
}
