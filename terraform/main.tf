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

# REMEDIATION: Private bucket with public access block and AES-256 encryption
resource "aws_s3_bucket" "financial_data_lake" {
  bucket = "enterprise-confidential-financial-records-2026"

  tags = {
    Environment = "Production"
    Compliance  = "CIS-Benchmark"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "s3_enc" {
  bucket = aws_s3_bucket.financial_data_lake.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "s3_block" {
  bucket                  = aws_s3_bucket.financial_data_lake.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# REMEDIATION: Ingress restricted strictly to corporate management subnet
resource "aws_security_group" "management_ssh" {
  name        = "allow_management_ssh"
  description = "Restricted corporate SSH access"

  ingress {
    description = "Corporate SSH Bastion Ingress"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.10.0/24"]
  }
}
