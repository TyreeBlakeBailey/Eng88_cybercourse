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

resource "aws_default_vpc" "web_server_vpc_tf"{

}


data "aws_subnet_ids" "web_server_subnet_tf"{
  vpc_id = aws_default_vpc.web_server_vpc_tf.id
}


resource "aws_security_group" "web_server_security_group_tf" {
  name = "web_server_security_group"

  vpc_id = aws_default_vpc.web_server_vpc_tf.id

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

resource "aws_instance" "web_server_instance"{
  ami                         = "ami-0f89681a05a3a9de7"
  instance_type               = "t2.micro"
  subnet_id                   = tolist(data.aws_subnet_ids.web_server_subnet_tf.ids)[0]
  associate_public_ip_address = true
  key_name                    = "cyber-tblake-bailey-key"
  vpc_security_group_ids      = [aws_security_group.web_server_security_group_tf.id]
}


```