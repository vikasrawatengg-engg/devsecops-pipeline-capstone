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

# 1. Private hardened S3 Bucket
resource "aws_s3_bucket" "financial_data_lake" {
  bucket = "enterprise-confidential-financial-records-2026"

  tags = {
    Environment = "Production"
    Compliance  = "CIS-Benchmark"
  }
}

# 2. Enforce S3 Bucket Versioning (Resolves CKV_AWS_21)
resource "aws_s3_bucket_versioning" "s3_versioning" {
  bucket = aws_s3_bucket.financial_data_lake.id
  versioning_configuration {
    status = "Enabled"
  }
}

# 3. Server-side encryption with AWS-managed KMS (Resolves CKV_AWS_19 and CKV_AWS_145)
resource "aws_s3_bucket_server_side_encryption_configuration" "s3_enc" {
  bucket = aws_s3_bucket.financial_data_lake.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = "arn:aws:kms:ap-south-1:123456789012:key/sample-key-id"
    }
  }
}

# 4. Strict Public Access Block (Resolves CKV2_AWS_6, CKV_AWS_53, 54, 55, 56)
resource "aws_s3_bucket_public_access_block" "s3_block" {
  bucket                  = aws_s3_bucket.financial_data_lake.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# 5. Ingress restricted strictly to internal subnet
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
