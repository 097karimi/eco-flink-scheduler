# EcoFlinkScheduler

EcoFlinkScheduler is a research prototype for predictive and energy-aware task scheduling in Apache Flink stream processing systems.  
The project combines machine learning-based workload prediction, SLA-aware scheduling, and runtime monitoring to improve energy efficiency while maintaining low end-to-end latency.

## Overview

Modern stream processing systems must handle dynamic and bursty workloads while meeting strict latency and QoS requirements.  
This project proposes a proactive scheduling framework for Apache Flink that uses historical runtime metrics and machine learning predictions to make energy-aware scheduling decisions.

The system is designed as a modular testbed with the following components:

- **Apache Flink**: distributed stream processing engine
- **Apache Kafka**: workload ingestion and stream generation
- **Prediction Service**: ML-based short-term load/latency forecasting
- **Scheduler Module**: energy-aware and SLA-aware decision engine
- **Monitoring Stack**: Prometheus and Grafana for runtime observability

## Key Features

- Predictive task scheduling for streaming workloads
- Energy-aware decision making
- SLA violation reduction
- Heterogeneous worker configuration
- Docker-based reproducible testbed
- Runtime monitoring and visualization
- Baseline comparison with default and heuristic schedulers

## Architecture

The system follows a modular architecture:

1. **Workload Generator** produces streaming events.
2. **Apache Kafka** delivers data to the Flink pipeline.
3. **Apache Flink** processes the stream in a standalone cluster.
4. **Monitoring services** collect runtime metrics.
5. **ML Prediction Service** forecasts future workload or latency.
6. **Scheduler Module** uses predicted and observed metrics to optimize task placement.

## Research Goals

This project aims to:

- reduce cluster energy consumption,
- minimize end-to-end latency,
- reduce SLA violations,
- and evaluate proactive scheduling strategies in heterogeneous environments.

## Experimental Setup

The testbed is based on Docker containers and includes:

- 1 JobManager
- multiple heterogeneous TaskManagers
- Kafka broker
- Prometheus
- Grafana
- ML inference service

Heterogeneity is emulated by assigning different CPU and memory limits to TaskManager containers.

## Tech Stack

- **Apache Flink**
- **Apache Kafka**
- **Docker / Docker Compose**
- **Python**
- **FastAPI**
- **PyTorch / TensorFlow**
- **Prometheus**
- **Grafana**

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Python 3.10+
- Git

### Run the testbed
```bash
git clone https://github.com/your-username/eco-flink-scheduler.git
cd eco-flink-scheduler
docker compose up -d
