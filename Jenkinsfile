pipeline {  
  
  agent any
  
  /*options {
    buildDiscarder(logRotator(numToKeepStr: '5', daysToKeepStr: '5'))
      timestamps()
  }*/
  
  environment {
    dockerImageName = "irajkoohi/statistics"
    dockerImage = ""
    
    //registry = "<dockerhub-username>/<repo-name>"
    //registryCredential = '<dockerhub-credential-name>'  
    
    registry = "irajkoohi/statistics"
    registryCredential = 'Ist1337#%'        
  }
    
  stages {  
      
    stage('Checkout Source') {
      steps {
        // git 'https://github.com/irajkooh/statistics.git'
        
        /*git branch: 'main',
            credentialsId: 'Github-Credentials',
            url: 'https://github.com/irajkooh/statistics.git'  
        //sh "ls -lat"  */
        
        checkout scm  // if jenkins project is setup by scm (Source Control Management) option
      }
    }

    // This Jenkins Pipeline stage will use the created Dockerfile to build a Docker image named "react-app"
    stage('Build image') {
      steps{
        git 'https://github.com/irajkoohi/statistics.git'
        script {
          //dockerImage = docker.build dockerImageName                  
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
        
    /*stage('Pushing Image') {
      environment {
        registryCredential = 'dockerhub-credentials'
        }
      steps {
        script {
          docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
          dockerImage.push("latest")
        }
      }
    }*/  

    /*stage('Deploying React.js container to Kubernetes') {
      steps {
        script {
          kubernetesDeploy(configs: "deployment.yaml", "service.yaml")
        }
      }
    }*/
    
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

