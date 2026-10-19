terraform {
  backend "s3" {
    bucket = "devsecops-capstone-tfstate-vikas"
    key    = "live/terraform.tfstate"
    region = "ap-south-1"
  }
}
