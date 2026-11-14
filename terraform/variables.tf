# ============================================================
# variables.tf — Input Variables
# ============================================================

variable "aws_region" {
  description = "AWS region to deploy the infrastructure"
  type        = string
  default     = "ap-south-1"  # Mumbai — closest to India
}

variable "instance_type" {
  description = "EC2 instance type (t2.micro is Free Tier eligible)"
  type        = string
  default     = "t3.micro"
}

variable "key_name" {
  description = "Name of the existing AWS EC2 Key Pair for SSH access"
  type        = string
  default     = "puppet-key"
}
