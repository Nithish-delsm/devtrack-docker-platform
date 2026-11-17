# DevTrack - Docker Mastery Project Roadmap

## Overview
Production-style Task & Project Tracker API: FastAPI + PostgreSQL + Redis + Nginx,
fully containerised with Docker Compose and deployed on AWS EC2 (Amazon Linux 2023).

## Learning Objectives
- Build, optimise and secure Docker images
- Networking, volumes, health checks, Compose
- Deploy and troubleshoot on AWS EC2

## Environment
- AWS EC2 t3.small (2 vCPU, 2 GB RAM), Amazon Linux 2023, SSH access

## Phase 1: Environment setup and Docker fundamentals
- [x] Identify OS (Amazon Linux 2023)
- [x] Install Docker Engine 25.0.14 (verified active and enabled)
- [x] Run Docker without sudo (docker group)
- [x] Install Docker Compose plugin v5.7.1 and verify
- [x] Run first container (hello-world)
- [x] Container lifecycle challenge: run, curl, logs, exec, stop, rm (nginx web1)
- [x] Install Git, create project folder, git init
- [x] First commit pushed to GitHub (SSH key auth verified)

## Phase 2: FastAPI application
- [x] Python venv created, FastAPI 0.128.8 and Uvicorn 0.39.0 installed
- [x] /health endpoint written and tested with curl
- [x] Task endpoints (POST/GET /tasks, GET /tasks/{id}) and pinned requirements.txt

## Phase 3: Dockerfile and image building
- [x] .dockerignore and Dockerfile written
- [x] Image built and inspected (168MB, layer cache verified)
- [x] Ran image as container on 127.0.0.1:8000, checked user/python/memory (runs as root, fix in Phase 12)

## Phases 4-15
- [x] 4 Container lifecycle (exit codes, --rm, inspect, top, system df verified)
- [x] 5 Volumes (named volume + Postgres persistence verified; bind mounts not yet practised)
- [x] 6 Networking (custom bridge network, DNS by container name, API to Postgres verified)
- [x] 7 Docker Compose (db + api, healthcheck, depends_on, restart policy, down/up persistence verified)
- [x] 8 PostgreSQL + Redis (SQLAlchemy persistence, password-protected Redis, cache with invalidation and fallback verified)
- [x] 9 Multi-stage build + non-root user (uid 10001) verified; image did not shrink (205MB vs 202MB)
- [x] 10 Nginx reverse proxy (only published port; API unpublished; backend network internal)
- [ ] 11 Health checks, logging, monitoring
- [ ] 12 Container security
- [ ] 13 AWS EC2 deployment
- [ ] 14 Testing and troubleshooting
- [ ] 15 Documentation and GitHub publishing
