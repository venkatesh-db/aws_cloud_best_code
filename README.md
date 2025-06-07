# 🚀 AWS Python Automation Samples

Welcome to the **AWS Python Automation Code Samples** repository!  
This collection is a hands-on resource to help you **automate common AWS tasks using Python and Boto3** – ideal for DevOps engineers, cloud architects, and automation enthusiasts.

---

## 📌 Features

- ✅ Automate AWS EC2 Instance Creation & Management  
- ✅ Manage S3 Buckets: Upload, Download, Lifecycle Policies  
- ✅ Schedule Backups for RDS using Python  
- ✅ Monitor AWS Resources via CloudWatch  
- ✅ Automate IAM Role/User/Policy Management  
- ✅ Deploy Lambda Functions with CI/CD Hooks  
- ✅ Use Step Functions to Orchestrate Multi-step Tasks

---

## 🧠 Use Cases

| Use Case                      | Python Script            | Description                              |
|------------------------------|--------------------------|------------------------------------------|
| Launch EC2 Instance          | `ec2_launch.py`          | Create EC2 with tags, key pair, and SG   |
| S3 File Backup               | `s3_backup.py`           | Upload files, set retention, and archive |
| IAM Policy Auto Setup        | `iam_setup.py`           | Create roles, attach policies programmatically |
| RDS Snapshot Scheduler       | `rds_backup.py`          | Scheduled snapshots and deletion logic   |
| CloudWatch Alarm Automation  | `cloudwatch_alerts.py`   | Setup CPU usage and cost alerts          |
| Lambda Deployment Automation | `lambda_deploy.py`       | Package and deploy Lambda functions via CLI |
| Step Functions Orchestration | `step_function_workflow.py` | Define and deploy workflows             |

---

## ⚙️ Requirements

- Python 3.7+
- Boto3
- AWS CLI (configured with credentials)
- Optional: `virtualenv` for isolated environments

Install dependencies:

```bash
pip install -r requirements.txt
