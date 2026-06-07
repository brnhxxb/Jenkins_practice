pipeline {
    agent any

    stages {
        stage('Auto Deploy') {
            steps {
                echo "Auto deploy"
                echo "Branch: ${env.GIT_BRANCH}"
                echo "Commit: ${env.GIT_COMMIT}"
            }
        }

        stage('Cleanup') {
            steps {
                cleanWs()
            }
        }
    }
}
