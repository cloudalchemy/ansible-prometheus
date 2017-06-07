#!groovy

/* Declarative pipeline */
pipeline {
  agent {
    node {
      label 'master'
      customWorkspace 'workspace/prometheus'
    }
  }
  options {
    disableConcurrentBuilds()
    buildDiscarder(logRotator(numToKeepStr: '30'))
    timeout(time: 15, unit: 'MINUTES')
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
  }

  post {
    always {
      sh 'molecule destroy'
    }
    success {
      mattermostSend color: 'good', message: "No. ${BUILD_NUMBER} test of ${JOB_NAME} has finished successfully. <${RUN_DISPLAY_URL}|More information.>"
    }
    failure {
      mattermostSend color: 'danger', message: "No. ${BUILD_NUMBER} test of ${JOB_NAME} has failed. <${RUN_DISPLAY_URL}|More information.>"
    }
  }
}
