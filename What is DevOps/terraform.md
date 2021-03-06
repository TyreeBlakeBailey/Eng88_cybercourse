# TerraForm

## What Is Terraform?
Terraform is one of the most popular Infrastructure-as-code (IaC) tool, used by DevOps teams to automate infrastructure tasks. It is used to automate the provisioning of your cloud resources. Terraform is an open-source, cloud-agnostic provisioning tool developed by HashiCorp and written in GO language.

Used to write code to automate the creation of the infrastructure
for example when you start creating the AWS 



## Terraform commands
    terraform init
    terraform validate
    terraform plan
    terraform apply
    ssh ec2-user@ec2-34-243-221-232.eu-west-1.compute.amazonaws.com
    terraform destroy

### main.tf

    This file allows you set up a AWS intances by running the files below

```terraform
terraform {
  required_providers{
    aws = {
      source = "hashicorp/aws"
      version = "~> 3.0"

    }
  }
}

provider "aws" {
  region = "eu-west-1"
}

resource "aws_default_vpc" "tyree_web_server_vpc_tf"{

}


data "aws_subnet_ids" "tyree_web_server_subnet_tf"{
  vpc_id = aws_default_vpc.tyree_web_server_vpc_tf.id
}


resource "aws_security_group" "tyree_web_server_security_group_tf" {
  name = "tyree_web_server_security_group"

  vpc_id = aws_default_vpc.tyree_web_server_vpc_tf.id

  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress{
  from_port = 0
  to_port = 0
  protocol = -1
  cidr_blocks = ["0.0.0.0/0"]
  }

}


variable "aws_private_key"{
default = "/home/kali/.ssh/cyber-tblake-bailey-key.pem"
}

resource "aws_instance" "tyree_web_server_instance"{
  ami                         = "ami-0f89681a05a3a9de7"
  instance_type               = "t2.micro"
  subnet_id                   = tolist(data.aws_subnet_ids.tyree_web_server_subnet_tf.ids)[0]
  associate_public_ip_address = true
  key_name                    = "cyber-tblake-bailey-key"
  vpc_security_group_ids      = [aws_security_group.tyree_web_server_security_group_tf.id]

  connection {
    type ="ssh"
    host = self.public_ip
    user = "ec2-user"
    private_key = file(var.aws_private_key)
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo amazon-linux-extras install docker -y",
      "sudo yum install docker -y",
      "sudo service docker start",
      "sudo usermod -a -G docker ec2-user"
    ]
  }

  provisioner "remote-exec" {
    inline = [
      "docker run -d -p 80:5000 tyreebb/docker-flask"
    ]
  }
}



```
![img_10.png](img_10.png)