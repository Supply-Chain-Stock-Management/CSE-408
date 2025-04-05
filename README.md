# 🚚 Supply Chain and Stock Management (Microservices Architecture)

This project is a modular and scalable microservices-based system designed to handle supply chain and stock operations. Built with Docker and Kubernetes, and managed through Kong API Gateway, it aims to demonstrate core backend microservices orchestration for enterprise logistics.

---

## 🧱 Microservices Overview

Each microservice runs independently and is containerized with Docker. All services are deployed to a Kubernetes cluster and are managed via Kong API Gateway, with **3 replicas per service** to ensure scalability and high availability.

### 📦 Current Services

| Service              | Description                                 |
|----------------------|---------------------------------------------|
| 🧾 Inventory Service | Handles product stock and warehouse data    |
| 📦 Order Service     | Manages customer orders and processing      |
| 🚛 Transport Service | Coordinates logistics and delivery tracking |
| 🔐 Auth Service      | Manages user login and authentication flows |

---

## 🛠️ Tech Stack

- 🐳 Docker
- ☸️ Kubernetes
- 🦍 Kong API Gateway
- 🌐 REST APIs (ExperssJS and Django)
- MongoDB and Postgres(used by relevant services)
- [In Progress] Kafka/RabbitMQ (Message Broker)
- [In Progress] JWT-based Authentication

---


> Note: Each service is deployed with 3 replicas for load balancing and fault tolerance.

---

## 🚀 Running the Project

> 🧪 This is an **incomplete build**. Message broker and JWT support are planned.

### Prerequisites

- Docker & Docker Compose
- Kubernetes Cluster (Minikube, KIND, AWS EKS cluster)
- Chocolatey or Helm (for Kong installation)
- kubectl
- Kong
