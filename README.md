🚀 Cloud-Native Flask Microservice Platform

A production-style DevOps project demonstrating how to deploy a containerized Flask microservice on Kubernetes with database integration, ingress routing, and monitoring.

This project simulates a real-world cloud-native architecture used in modern DevOps environments.


📌 Project Overview

The application exposes a Flask REST API that connects to a PostgreSQL database and is deployed inside a Kubernetes cluster. The service is exposed externally through NGINX Ingress, while Prometheus and Grafana provide monitoring and observability.


🏗 Architecture

User
  │
  ▼
NGINX Ingress Controller
  │
  ▼
Flask Backend API (Kubernetes Deployment)
  │
  ▼
PostgreSQL Database (Kubernetes Pod)
  │
  ▼
Prometheus → Metrics Collection
  │
  ▼
Grafana → Monitoring Dashboard



⚙️ Tech Stack

Backend

Python

Flask

Containerization

Docker

Orchestration

Kubernetes (Kind)

Database

PostgreSQL

Ingress

NGINX Ingress Controller

Monitoring

Prometheus

Grafana

Helm

Version Control

Git

GitHub


✨ Key Features

✔ Containerized Flask REST API using Docker
✔ Kubernetes deployment with replica scaling
✔ Service exposure using NGINX Ingress Controller
✔ PostgreSQL integration for database connectivity
✔ Prometheus metrics monitoring
✔ Grafana dashboards for visualization
✔ Production-style microservice architecture


🐳 Docker Setup

Build the container image:

docker build -t flask-backend:v1 .

Run locally:

docker run -p 5000:5000 flask-backend:v1


☸ Kubernetes Deployment

Apply Kubernetes manifests:

kubectl apply -f k8s/

Verify pods:

kubectl get pods

Check services:

kubectl get svc


🌐 Access the API

Health check endpoint

/health

Example response:

{
  "status": "UP"
}

API endpoint

/api/message

Example response:

{
  "message": "Hello from Flask Backend 🚀",
  "timestamp": "2026-03-03T09:52:16"
}


📊 Monitoring

Prometheus collects metrics from Kubernetes workloads.

Grafana provides dashboards to visualize:

Pod CPU usage

Memory usage

Cluster health

Application metrics

Access Grafana via:

kubectl port-forward svc/monitoring-grafana 3000:80
🚀 DevOps Concepts Demonstrated

This project demonstrates practical experience with:

Containerization using Docker

Kubernetes deployments and services

Ingress-based routing

Database connectivity inside Kubernetes

Infrastructure observability

Monitoring with Prometheus & Grafana

Microservices architecture

🎯 Learning Outcomes

Through this project I learned how to:

Build and containerize Python applications

Deploy applications on Kubernetes clusters

Expose services using Ingress

Connect microservices with databases

Implement monitoring and observability

Design production-style DevOps architecture

📌 Future Improvements

Add CI/CD pipeline using Jenkins

Deploy on AWS EKS

Add ELK stack for centralized logging

Implement Horizontal Pod Autoscaling

Add GitHub Actions pipeline

👨‍💻 Author

Abhishek

GitHub:
https://github.com/Abhivox
