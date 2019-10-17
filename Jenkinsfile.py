#!/usr/bin/env groovy
pipeline {
    agent { docker 'python:3.7' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}