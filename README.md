# KubeSage AI

AI-powered Kubernetes Platform Operations Engineer

## Problem Statement

Kubernetes incidents are complex and multi-dimensional. Platform teams struggle to connect pod failures, application logs, cluster health, policies, deployment drift, and observability signals into a single remediation path.

`KubeSage AI` is a production-ready portfolio project designed to demonstrate enterprise-grade platform engineering for cloud-native operations. It combines Kubernetes diagnostics, AI-driven root cause analysis, RAG-based knowledge capture, and repair recommendations for infrastructure, CI/CD, Helm, and runbooks.

## Architecture Overview

```text
┌──────────────────────────────┐        ┌───────────────────────┐
│        Kubernetes           │        │    Observability      │
│       Cluster / Apps        │        │ Prometheus / Grafana  │
└──────────────┬──────────────┘        └───────────────┬───────┘
               │                                  │
               │ kubectl / API                      │ metrics / alerts
               ▼                                  ▼
┌──────────────────────────────────────────────────────────────┐
│                       Backend Services                       │
│  - FastAPI Orchestrator                                       │
│  - Kubernetes Collector                                       │
│  - Incident Correlation Engine                                │
│  - AI Reasoning Engine (LangGraph / OpenRouter)               │
│  - RAG Knowledge Store (ChromaDB / embeddings)               │
└──────────────┬─────────────────────────────────────┬─────────┘
               │                                     │
               │                                     │
      ┌────────▼────────┐                   ┌────────▼────────┐
      │  Dashboard API  │                   │  Data Services   │
      │  React + TS UI  │                   │  Postgres / S3   │
      └─────────────────┘                   └─────────────────┘
```

## Features

- Kubernetes incident investigation at enterprise scale
- Multi-source evidence collection: pods, events, logs, deployments, HPA, ingress, services, ConfigMaps, Secrets metadata, node metrics, Prometheus, Grafana, Alertmanager, ArgoCD, Helm, Network Policies, PV/PVC
- AI-driven root cause prioritization, correlated failure explanation, confidence scoring
- Actionable repair guidance: kubectl commands, YAML patches, Helm releases, Terraform changes, GitHub Actions workflows
- Runbook generation, postmortem summaries, incident timeline, and RCA documents
- Clean architecture with domain-driven design, repository pattern, and dependency injection
- Infrastructure-ready deployment using Docker Compose, Helm charts, Kubernetes manifests, and CI/CD pipelines

## Screenshots

- [ ] Dashboard showing incident summary
- [ ] Investigation timeline and confidence score
- [ ] Runbook generator output
- [ ] Repair recommendation panel
- [ ] RAG knowledge search

## Installation

1. Clone the repository

```bash
git clone https://github.com/theycallmejc/KubeSage-AI.git
cd KubeSage-AI
```

2. Install backend dependencies

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

3. Install frontend dependencies

```bash
cd ../frontend
npm install
```

4. Configure environment variables

```bash
cp .env.example .env
```

## Running Locally

```bash
cd backend
uvicorn app.main:app --reload
```

In another terminal:

```bash
cd frontend
npm start
```

## Docker

Build and run the full stack with Docker Compose:

```bash
docker compose build

docker compose up
```

## Kubernetes

Deploy the platform using Helm charts or manifests:

```bash
helm install kubesage ./deploy/helm/kubesage
```

## Roadmap

- Add multi-cluster incident federation
- Add SLO-aware root cause correlation
- Add role-based access control for investigator workflows
- Add audit trail and evidence provenance
- Add native cloud provider incident ingestion for AWS, GCP, Azure

## Future Scope

- Expand RAG knowledge base for internal runbook libraries
- Add automated remediation playbooks using GitHub Actions and Terraform
- Add multi-tenant SaaS support for platform teams
- Add support for Service Mesh observability beyond Istio

## Resume Highlights

- Designed `KubeSage AI`, an enterprise-grade AI-driven Kubernetes platform operations product
- Implemented clean architecture with FastAPI backend, React dashboard, and LangGraph-powered AI reasoning
- Built multi-source Kubernetes diagnostics for cluster, observability, GitOps, and infrastructure
- Delivered repair recommendation generation for Helm, Terraform, GitHub Actions, and kubectl
- Demonstrated cloud-native automation, CI/CD, and observability best practices

---

## Built By

`KubeSage AI` was architected and scaffolded by **theycallmejc** to showcase platform engineering excellence in cloud-native infrastructure, DevOps automation, and enterprise-grade Kubernetes operations.
