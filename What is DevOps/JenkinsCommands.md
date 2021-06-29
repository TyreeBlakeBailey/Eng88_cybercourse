# Jenkins reset commands 


cd ~/devsecops/jenkins

docker-compose down

docker-compose rm

docker volume rm jenkins_jenkins-docker-certs jenkins_jenkins-data

docker-compose up -d

