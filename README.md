# ============================================================
# README.md — Project Documentation
# INT333 | Kushagra | Roll No. 63
# ============================================================

# Automated Cloud Infrastructure Provisioning & Configuration Management
### Using Terraform and Puppet

**Course:** INT333 – DevOps Advance Configuration Management  
**Author:** Kushagra | Roll No. 63 | Reg. No. 12323868  
**University:** Lovely Professional University | Batch: 2023–2027

---

## Architecture Overview

```
[ Developer ]
     |
     | terraform apply
     v
[ AWS EC2 (Ubuntu 22.04) ]   <-- Terraform provisions this
     |
     | user_data bootstrap script
     v
[ Puppet Agent (puppet apply) ]  <-- Puppet configures this
     |
     v
[ Apache Web Server running on port 80 ]
     |
     v
[ Browser: http://<public-ip> ]
```

## Project Structure

```
devops-project/
├── terraform/
│   ├── main.tf          # EC2, Security Group, AMI data source
│   ├── variables.tf     # Input variables (region, instance type, key)
│   └── outputs.tf       # Outputs: IP, URL, SSH command
├── puppet/
│   └── manifests/
│       └── site.pp      # Puppet manifest: Apache install + config
└── README.md
```

## Prerequisites

| Tool      | Version    | Download |
|-----------|------------|----------|
| Terraform | >= 1.0     | https://developer.hashicorp.com/terraform/install |
| AWS CLI   | >= 2.0     | https://aws.amazon.com/cli/ |
| AWS Account | –        | IAM user with EC2 permissions |
| Key Pair  | `puppet-key` | Must exist in AWS ap-south-1 region |

## Deployment Steps

### 1. Initialize Terraform
```bash
cd terraform
terraform init
```

### 2. Preview the plan
```bash
terraform plan
```

### 3. Apply (provision infrastructure)
```bash
terraform apply
# Type 'yes' when prompted
```

### 4. Access the web server
After ~3-5 minutes (for Puppet to configure Apache):
```
http://<public_ip>
```
The public IP is shown in the Terraform output.

### 5. SSH into the instance (optional)
```bash
ssh -i puppet-key.pem ubuntu@<public_ip>
# Check Puppet log:
sudo cat /var/log/puppet-apply.log
```

### 6. Destroy (cleanup)
```bash
terraform destroy
```

## What Terraform Creates

| Resource | Details |
|----------|---------|
| Security Group | Allows SSH (22) + HTTP (80) |
| EC2 Instance | Ubuntu 22.04 LTS, t2.micro (Free Tier) |

## What Puppet Configures

| Resource | Action |
|----------|--------|
| `apache2` package | Installed |
| `apache2` service | Running + enabled on boot |
| `/var/www/html/index.html` | Custom page deployed |

## Test Cases

| Test | Command | Expected |
|------|---------|----------|
| Instance running | `terraform show` | State = running |
| SSH access | `ssh ubuntu@<ip>` | Login successful |
| Apache running | `systemctl status apache2` | Active (running) |
| HTTP response | `curl http://<ip>` | HTML page returned |
| Idempotency | Run puppet apply again | 0 resources changed |

