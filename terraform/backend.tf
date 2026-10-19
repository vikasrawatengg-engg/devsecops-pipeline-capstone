terraform {
  backend "s3" {
    bucket = "devsecops-capstone-tfstate-vikas"
    key    = "production/terraform.tfstate"
    region = "ap-south-1"
  }
}
