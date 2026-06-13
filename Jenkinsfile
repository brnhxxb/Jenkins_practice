NU nano 7.2                                  Jenkinsfile
pipeline {
    agent any

    parameters {
        choice(name: 'ENV', choices: ['dev', 'prod'], description: 'Выберите окружение')
    }

    stages {
        stage('Info') {
            steps {
                echo "Deploying to ${params.ENV}"
            }
        }

        stage('Copy files via SSH') {
            steps {
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'my-server',
                            transfers: [
                                sshTransfer(
                                    sourceFiles: '**/*',
                                    remoteDirectory: "/app/${params.ENV}",
                                    removePrefix: ''
                                )
                            ]
                        )
                    ]
                )
            }
        }

        stage('Cleanup') {
            steps {
                cleanWs()
            }
        }
    }
}



