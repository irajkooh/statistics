pipeline {  
  
  agent any
  
  /*options {
    buildDiscarder(logRotator(numToKeepStr: '5', daysToKeepStr: '5'))
      timestamps()
  }*/
  
  environment {
  // These enviromental varables will be used where required in pipeline
    dockerImageName = "irajkoohi/statistics"
    dockerImage = ""    
        
    //registry = "<dockerhub-username>/<repo-name>"
    //registryCredential = '<dockerhub-credential-name>'      
    registry = "irajkoohi/statistics"
    registryCredential = 'Ist1337#%'     
  }
    
  stages {  
    stage('Checkout the Source code') {
    // Use ‘https://github.com/irajkoohi/jenkins-kubernetes-deployment.git’ as the GitHub repository. 
    // This stage will pull the repository and scan all the files in it.  
      steps {
        // git 'https://github.com/irajkooh/statistics.git'        
        /*git branch: 'main',
            credentialsId: 'Github-Credentials',
            url: 'https://github.com/irajkooh/statistics.git'  
        //sh "ls -lat"  */        
        checkout scm  // if jenkins project is setup by scm (Source Control Management) option
      }
    }
    
    /*stage('Build Image from the Source using Docker') {
    // This stage will use the created Dockerfile in repository to build a Docker image named ‘irajkoohi/statistics’.
      steps {
        //git 'https://github.com/irajkoohi/statistics.git'
        script {
          //dockerImage = docker.build dockerImageName                  
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }*/
    
    /*stage('Push created Image to DockerHub') {
    // This stage will push the ‘irajkoohi/statistics’ Docker image to DockerHub using the created ‘DockerHub-Credentials’ in Jenkins.  
      environment {
        registryCredential = 'DockerHub-Credentials'
        }
      steps {
        script {
          docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
          dockerImage.push("latest")
        }
      }
    }*/  

    stage('Deploying React.js container to Kubernetes') {
    // This stage will pull app ‘irajkoohi/statistics:latest’ Docker image from the DockerHub repository irajkoohi/statistics and create a containerized application. 
    // Next, It will then deploy the app container to Kubernetes.  
      steps {
        script {
          kubernetesDeploy(configs: "deployment.yaml", "service.yaml")
        }
      }
    }
    
  }  
}











// ############## pipeline test ##############
/*pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }
}*/

