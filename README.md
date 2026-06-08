# Pharmacy API (EKS + FastAPI + AWS)

A production-grade backend API built with **FastAPI**, deployed on **AWS EKS (Kubernetes)** using **Docker + Amazon ECR**, and integrated with AWS services like **DynamoDB, SQS, and EventBridge**.

---

## 🚀 Live Architecture


Client
↓
Kubernetes Service (EKS)
↓
FastAPI Pod (Docker Container)
↓
AWS Services:
DynamoDB (Data storage)
SQS (Messaging - optional)
EventBridge (Event publishing)

## 🧱 Tech Stack

- Python 3.11
- FastAPI
- Docker
- Kubernetes (AWS EKS)
- Amazon ECR
- DynamoDB
- AWS SQS
- AWS EventBridge
- AWS IAM (Node IAM Roles)
- Uvicorn

---

## ☁️ AWS Infrastructure

This project runs on:

- EKS Cluster: `pharmacy-cluster`
- Node Group: Managed EC2 nodes
- Container Registry: Amazon ECR
- Region: `eu-west-2`

---

## 📦 Features

- Create drug records
- Retrieve drug data from DynamoDB
- Event publishing via EventBridge
- Containerized microservice
- Auto-scaling Kubernetes deployment
- Health checks with Kubernetes probes

---

## 🐳 Docker

Build image:

```bash
docker build -t pharmacy-api .


---

# 🚀 2. “Real Engineer README Upgrade”


![AWS](https://img.shields.io/badge/AWS-EKS-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestrated-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)

## ⚡ Production Highlights

- Deployed on AWS EKS (real Kubernetes cluster)
- Fixed ImagePullBackOff and CrashLoopBackOff issues
- Built custom Docker image pushed to Amazon ECR
- Configured IAM roles for secure AWS access from pods
- Debugged runtime Python import errors inside containers
- Implemented rolling deployments with zero downtime

## 🔄 CI/CD Pipeline (In Progress)

Current workflow:

1. Local development
2. Docker build
3. Push to ECR
4. Manual kubectl deployment to EKS

Next upgrade:
- GitHub Actions automation
- Automatic deployment on push to main branch

## 🧠 Engineering Skills Demonstrated

- Kubernetes workload debugging (CrashLoopBackOff, ImagePullBackOff)
- AWS IAM permission troubleshooting
- Docker multi-stage build and deployment
- Cloud-native architecture design
- FastAPI backend development
- ECR image management
- Production log debugging