# ============================================================
# main.tf — Terraform Configuration for Automated Cloud
# Infrastructure Provisioning
# Project: Automated Cloud Infrastructure Provisioning and
#          Configuration Management Using Terraform and Puppet
# Author : Kushagra (Roll No. 63)
# Course : INT333 – DevOps Advance Configuration Management
# ============================================================

terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# ----------------------------------------------------------
# Provider Configuration
# ----------------------------------------------------------
provider "aws" {
  region = var.aws_region
}

# ----------------------------------------------------------
# Data Sources
# ----------------------------------------------------------

# Fetch the latest Ubuntu 22.04 LTS AMI (Canonical)
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

# Fetch the default VPC
data "aws_vpc" "default" {
  default = true
}

# ----------------------------------------------------------
# Security Group — allow SSH (22) and HTTP (80)
# ----------------------------------------------------------
resource "aws_security_group" "puppet_sg" {
  name        = "puppet-apache-sg"
  description = "Allow SSH and HTTP traffic for Puppet-managed Apache server"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    description = "SSH access"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP access"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name    = "puppet-apache-sg"
    Project = "INT333-DevOps"
    Author  = "Kushagra-RollNo63"
  }
}

# ----------------------------------------------------------
# EC2 Instance — Ubuntu 22.04 LTS (t3.micro, Free Tier)
# ----------------------------------------------------------
resource "aws_instance" "puppet_node" {
  ami                         = data.aws_ami.ubuntu.id
  instance_type               = var.instance_type
  key_name                    = var.key_name
  vpc_security_group_ids      = [aws_security_group.puppet_sg.id]
  associate_public_ip_address = true
  user_data_replace_on_change = true

  # Bootstrap script: installs Puppet agent and applies the manifest
  user_data = <<-EOF
#!/bin/bash
exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1

export DEBIAN_FRONTEND=noninteractive

# Wait for apt/dpkg lock release
while fuser /var/lib/dpkg/lock-frontend >/dev/null 2>&1; do
  echo "Waiting for dpkg lock..."
  sleep 3
done

# Update system
apt-get update -y
apt-get install -y wget curl gnupg

# Install Puppet Agent
wget -q https://apt.puppet.com/puppet8-release-jammy.deb -O /tmp/puppet-release.deb
dpkg -i /tmp/puppet-release.deb
apt-get update -y
apt-get install -y puppet-agent || apt-get install -y puppet

# Setup Puppet manifest directory
mkdir -p /etc/puppetlabs/code/environments/production/manifests

cat << 'PUPPET' > /etc/puppetlabs/code/environments/production/manifests/site.pp
node default {
  package { 'apache2':
    ensure => installed,
  }

  service { 'apache2':
    ensure  => running,
    enable  => true,
    require => Package['apache2'],
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0644',
    content => "<html>
  <head>
    <title>Puppet Managed Server</title>
    <style>
      body { font-family: Arial, sans-serif; text-align: center; margin-top: 80px; background: #f4f4f4; }
      h1   { color: #2c3e50; }
      .box { background: white; display: inline-block; padding: 40px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
      .badge { background: #e74c3c; color: white; padding: 4px 10px; border-radius: 4px; font-size: 0.85em; }
    </style>
  </head>
  <body>
    <div class=\"box\">
      <h1>&#9989; Automated Web Server - Configured by Puppet</h1>
      <p>This server was <strong>provisioned</strong> by <span class=\"badge\">Terraform</span> and
         <strong>configured</strong> by <span class=\"badge\" style=\"background:#3498db\">Puppet</span>.</p>
      <hr/>
      <p><strong>Project:</strong> INT333 &ndash; DevOps Advance Configuration Management</p>
      <p><strong>Author:</strong> Kushagra &nbsp;|&nbsp; Roll No. 63</p>
      <p><strong>Institution:</strong> Lovely Professional University</p>
    </div>
  </body>
</html>
",
    require => Package['apache2'],
    notify  => Service['apache2'],
  }
}
PUPPET

# Apply Puppet manifest
if [ -x /opt/puppetlabs/bin/puppet ]; then
  /opt/puppetlabs/bin/puppet apply /etc/puppetlabs/code/environments/production/manifests/site.pp
elif command -v puppet >/dev/null 2>&1; then
  puppet apply /etc/puppetlabs/code/environments/production/manifests/site.pp
else
  apt-get install -y apache2
  systemctl start apache2
  systemctl enable apache2
fi

echo "Provisioning complete!"
EOF

  tags = {
    Name    = "puppet-apache-node"
    Project = "INT333-DevOps"
    Author  = "Kushagra-RollNo63"
  }
}
