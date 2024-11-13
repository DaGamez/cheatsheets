#Terraform block
terraform {
    required_version=">=1.9.8"
}


output "greeting" {
    value = "Hello Terraform."
}

#aws gcp
provider "random" {}

provider "aws"{}

variable "bucket_name"{
    type=string
    default="bucket3ext"
}

locals{
    aws_account = "${data.aws_caller_identity.current.account_id}-${data.aws_caller_identity.current.user_id}"
}

# bucket 1 is name in terraform no in aws
resource "aws_s3_bucket" "bucket1"{  
}

# bucket 2 with interpolation for recommended name
resource "aws_s3_bucket" "bucket2"{
    bucket= "${data.aws_caller_identity.current.account_id}-bucket2"  
}

# bucket 3 with interpolation for recommended name
resource "aws_s3_bucket" "bucket3"{
    bucket= "${data.aws_caller_identity.current.account_id}-${var.bucket_name}"  
}


#Data siyrces
#objects not managed by terraform
data "aws_caller_identity" "current"{}

data "aws_availability_zones" "available" {   
}

output "bucket_info"{
    value=aws_s3_bucket.bucket1
}

output "aws_caller_info" {
    value=data.aws_caller_identity.current
}

output "aws_availability_zones"{
    value=data.aws_availability_zones.available
}


