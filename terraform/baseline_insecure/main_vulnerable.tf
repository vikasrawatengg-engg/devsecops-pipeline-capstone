terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region                      = "ap-south-1"
  skip_credentials_validation = true
  skip_requesting_account_id  = true
}

# VIOLATION 1: S3 bucket configured with public-read ACL
# VIOLATION 2: S3 bucket missing server-side encryption
resource "aws_s3_bucket" "financial_data_lake" {
  bucket = "enterprise-confidential-financial-records-2026"
  acl    = "public-read"

  tags = {
    Environment = "Dev"
  }
}

# VIOLATION 3: Unrestricted management ingress (0.0.0.0/0 on SSH port 22)
resource "aws_security_group" "management_ssh" {
  name        = "allow_management_ssh"
  description = "Open SSH access"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
