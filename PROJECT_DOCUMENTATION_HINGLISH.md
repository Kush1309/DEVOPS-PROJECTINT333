# Project Documentation: Automated Cloud Infrastructure & Configuration Management
### INT333 – DevOps Advance Configuration Management
**Author:** Kushagra | **Roll Number:** 63 | **Reg. No:** 12323868  
**Faculty Guide:** Harpreet Kaur (Assistant Professor, CSE) | **LPU Batch:** 2023–2027

---

## 1. Yeh Project Karta Kya Hai? (Core Concept)

Real-world companies me jab bhi koi naya application deploy karna hota hai, toh do sabse bade challenges aate hain:
1. **Server banana (Provisioning):** Har baar manually AWS console me jakar click-click karke EC2 instance, security group, networking banana slow aur error-prone hota hai.
2. **Server configure karna (Configuration Management):** Server banne ke baad uske andar Apache, software packages, config files manually install karna mushkil hota hai, aur **Configuration Drift** (servers ke configurations ka aapas me alag ho jana) ho jata hai.

### 💡 Is Project ka Solution:
Yeh project do industry-standard tools ko jod kar **100% automated pipeline** banata hai:

```
[ Terraform ]                     [ Puppet ]                   [ Apache Web Server ]
  (Step 1)                          (Step 2)                         (Step 3)
AWS pe EC2 Server aur       Server ke andar jakar        Browser me live dashboard
Security Group banata hai   Apache software install      chalata hai (Port 80)
                            aur configure karta hai
```

* **Terraform** jawab deta hai: *"Mujhe kaisa server aur cloud network chahiye?"* (Infrastructure as Code - IaC)
* **Puppet** jawab deta hai: *"Is server ke andar kaun se softwares aur files hone chahiye?"* (Configuration Management - CM)

---

## 2. Architecture & Workflow (Starting Se Ending Tak)

Jab tum terminal me `terraform apply` chalate ho, toh background me ye steps hote hain:

```
                    +------------------------------------+
                    |  1. Developer runs terraform apply |
                    +-----------------+------------------+
                                      |
                                      v
                    +------------------------------------+
                    |  2. AWS Cloud (Mumbai Region)      |
                    |     - Security Group (Port 22, 80) |
                    |     - EC2 Instance (Ubuntu 22.04)  |
                    +-----------------+------------------+
                                      |
                                      v
                    +------------------------------------+
                    |  3. cloud-init (User Data Script)  |
                    |     - System update                |
                    |     - Puppet Agent v8 Install      |
                    +-----------------+------------------+
                                      |
                                      v
                    +------------------------------------+
                    |  4. Puppet Catalog Execution       |
                    |     - package { 'apache2': ensure} |
                    |     - service { 'apache2': running}|
                    |     - file { index.html: deployed} |
                    +-----------------+------------------+
                                      |
                                      v
                    +------------------------------------+
                    |  5. Output: Live Web Dashboard     |
                    |     http://13.201.137.244 (Port 80)|
                    +------------------------------------+
```

---

## 3. Project File Structure & Explanation

Tumhare project folder (`devops-project/`) me ye files hain:

| File Name | Kaam (Purpose) |
|-----------|----------------|
| `terraform/main.tf` | AWS Provider, Ubuntu 22.04 AMI, Security Group (Port 22 & 80), aur EC2 `aws_instance` define karta hai. Isme `user_data` script likha hai jo boot hote hi Puppet chalata hai. |
| `terraform/variables.tf` | Region (`ap-south-1`), instance type (`t3.micro`), aur SSH key pair (`puppet-key`) ke default parameters store karta hai. |
| `terraform/outputs.tf` | Deploy hone ke baad Public IP, URL, aur SSH command print karta hai. |
| `puppet/manifests/site.pp` | Puppet ka code jisme declarative syntax me likha hai ki Apache installed hona chahiye, running hona chahiye, aur custom HTML page hona chahiye. |
| `index.html` | Ultra-modern Nixtio Bento Grid UI dashboard jo Apache server serve karta hai. |
| `puppet-key.pem` | AWS EC2 server me secure SSH login karne ke liye private key. |

---

## 4. Puppet Code Samajhna (Declarative Language)

Puppet traditional scripts se alag hota hai. Script me tum bolte ho *"Ye command chalao"*. Puppet me tum **Desired State** bolte ho:

```puppet
node default {

  # 1. Ensure apache2 package install ho
  package { 'apache2':
    ensure => installed,
  }

  # 2. Ensure apache2 service chal rahi ho aur boot pe enable ho
  service { 'apache2':
    ensure  => running,
    enable  => true,
    require => Package['apache2'], # Package install hone ke baad hi service start hogi
  }

  # 3. Ensure custom index.html file present ho
  file { '/var/www/html/index.html':
    ensure  => file,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0644',
    source  => '/tmp/index.html',
    require => Package['apache2'],
    notify  => Service['apache2'], # Agar file badle toh Apache reload ho jaye
  }
}
```

### 🔑 Key Concept: Idempotency (Faculty ka favourite question)
Agar tum Puppet ko 100 baar bhi run karoge:
* Pehli baar: Apache install hoga (1 change).
* Doosri baar: Puppet dekhega ki Apache pehle se installed hai, toh kuch nahi karega (0 changes).
Is property ko **Idempotency** kehte hain.

---

## 5. Kaise Use Hota Hai? (Step-by-Step Commands)

### Step 1: AWS Credentials & Folder Check
```bash
cd "c:\Users\Kushagra Saxena\Desktop\devops-project\terraform"
aws sts get-caller-identity
```

### Step 2: Terraform Initialize (Plugins download)
```bash
terraform init
```

### Step 3: Terraform Plan (Review changes)
```bash
terraform plan
```
*(Yeh batata hai ki kitne resources create hone wale hain bina actual creation kiye)*

### Step 4: Infrastructure Deploy Karna
```bash
terraform apply -auto-approve
```
*(Yeh 1-2 minute me AWS Mumbai me EC2 instance aur firewall create kar deta hai)*

### Step 5: Web Browser Me Check Karna
Jo IP terminal me aati hai, usko browser me open karo:
```
http://<Public_IP>
(Example: http://13.201.137.244)
```

### Step 6: SSH Login Karke Check Karna (Optional)
```bash
ssh -i ../puppet-key.pem ubuntu@13.201.137.244
sudo systemctl status apache2
```

### Step 7: Clean Up (Destroy - Taaki bill na aaye)
Jab faculty ko dikha chuke ho aur kaam khatam ho jaye:
```bash
terraform destroy -auto-approve
```

---

## 6. Faculty Viva Questions & Answers (Full Marks Strategy)

### Q1: Terraform aur Puppet me kya difference hai?
> **Answer:** "Sir/Ma'am, Terraform ek **Infrastructure as Code (IaC)** tool hai jo cloud resources (like AWS EC2, VPC, Subnets) provision karta hai. Jabki Puppet ek **Configuration Management** tool hai jo OS ke andar packages install, update, aur services manage karta hai."

### Q2: Idempotency kya hoti hai?
> **Answer:** "Idempotency ka matlab hai ki script ko chahe kitni bhi baar run karein, result hamesha same 'Desired State' hi rahega bina duplicate changes kiye. Agar Apache pehle se installed hai toh Puppet dobara install nahi karega."

### Q3: Configuration Drift kya hota hai aur Puppet usse kaise rokta hai?
> **Answer:** "Agar koi admin manual server me jakar Apache stop kar de ya config change kar de, toh usse Configuration Drift bolte hain. Puppet agent har 30 min me catalog match karta hai aur drift hote hi Apache ko wapas restart aur correct state me le aata hai."

### Q4: Tumne t3.micro kyu choose kiya?
> **Answer:** "Sir, AWS ap-south-1 (Mumbai) region me `t3.micro` AWS Free Tier eligible instance type hai, jisme 2 vCPUs aur 1 GiB RAM milti hai jo Linux + Apache + Puppet workloads ke liye cost-effective aur optimal hai."

