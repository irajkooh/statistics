pipeline {  
  
  /*options {
    buildDiscarder(logRotator(numToKeepStr: '5', daysToKeepStr: '5'))
      timestamps()
  }*/
  
  environment {
  // These enviromental varables will be used where required in pipeline
    //registry = "<dockerhub-username>/<repo-name>"
    //registryCredential = '<dockerhub-credential-name>'      
    registry = "irajkoohi/statistics"
    registryCredential = 'DockerHub-Credentials'
    //registryCredential = "Ist1337#%"   
    dockerImage = "" 
    
  }
  
  agent any  
  
  stages {  
    stage('Checkout the Source code') {
    // This stage will pull the repository and scan all the files in it.  
      steps {
        /*git branch: 'main', credentialsId: 'Github-Credentials', url: 'https://github.com/irajkooh/statistics.git'  
        sh "ls -lat"  */        
        checkout scm  // if jenkins project is setup by scm (Source Control Management) option
      }
    }
    
   /* stage('Cloning my git') {
      steps {
        git branch: 'main', credentialsId: 'Github-Credentials', url: 'https://github.com/irajkooh/statistics.git'    
        sh "ls -lat"
      }
    } */   
    
    stage('Build Image from the Source code using Docker') {
    // This stage will use the created Dockerfile in the git repository to build a Docker image named ‘irajkoohi/statistics’.
      steps {
        // Cloning my git
        git branch: 'main', credentialsId: 'Github-Credentials', url: 'https://github.com/irajkooh/statistics.git'    
        sh "ls -lat"
        script {
          docker run -u 0 --privileged --name jenkins -it -d -p 8080:8080 -p 50000:50000 \
          -v /var/run/docker.sock:/var/run/docker.sock \
          -v $(which docker):/usr/bin/docker \
          -v /home/jenkins_home:/var/jenkins_home \
          jenkins/jenkins:latest          
          //dockerImage = docker.build registry + ":$BUILD_NUMBER" // docker not found means, the docker container which I’m running Jenkins, wants docker
        }
      }
    }
    
    stage('Push created Image to DockerHub') {
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
      }
    }

    /*stage('Deploying React.js container to Kubernetes') {
    // This stage will pull app ‘irajkoohi/statistics:latest’ Docker image from the DockerHub repository irajkoohi/statistics and create a containerized application. 
    // Next, It will then deploy the app container to Kubernetes.  
      steps {
        script {
          kubernetesDeploy(configs: "deployment.yaml", "service.yaml")
        }
      }
    }*/

    stage('Cleaning up') {
      steps {
        sh "docker rmi $registry:$BUILD_NUMBER"
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

