# Jenkins reset commands 


cd ~/devsecops/jenkins

docker-compose down

docker-compose rm

docker volume rm jenkins_jenkins-docker-certs jenkins_jenkins-data

docker-compose up -d

# AWS docker

    sudo yum update -y
    sudo amazon-linux-extras install docker
    sudo yum install docker
    sudo service docker start
    sudo usermod -a -G docker ec2-user

    docker pull tyreebb/docker-flask (name of docker file)
    docker run -p 80:5000 tyreebb/docker-flask 