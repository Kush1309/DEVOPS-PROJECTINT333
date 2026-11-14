# ============================================================
# outputs.tf — Output Values
# ============================================================

output "instance_id" {
  description = "EC2 Instance ID"
  value       = aws_instance.puppet_node.id
}

output "public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.puppet_node.public_ip
}

output "public_dns" {
  description = "Public DNS name of the EC2 instance"
  value       = aws_instance.puppet_node.public_dns
}

output "web_url" {
  description = "URL to access the Apache web server"
  value       = "http://${aws_instance.puppet_node.public_ip}"
}

output "ssh_command" {
  description = "Command to SSH into the instance"
  value       = "ssh -i puppet-key.pem ubuntu@${aws_instance.puppet_node.public_ip}"
}

output "ami_used" {
  description = "AMI ID used for the instance (Ubuntu 22.04 LTS)"
  value       = data.aws_ami.ubuntu.id
}

