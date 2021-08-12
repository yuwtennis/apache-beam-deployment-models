# apache-beam-deployment-models

Sample deployment models for apache beam. Pipelines are created using python for now.

## Target audience

People who use apache beam.

## Motivation

I would like to help people who are having trouble with implementing deployments.

## Directory model
```
.
├── libs
├── __main__.py
├── models
│   └── docker
│       └── flink-session-cluster
│           ├── docker-compose.yml
│           └── Dockerfile
├── README.md
└── requirements.txt
```

## Available deployment models

Detailed instructions are on wiki.

| Platform | Topologies | Wiki |
| ---------- | -------- | ------------ |
| Docker | Flink Session Cluster | [Flink Session Cluster on Docker](https://github.com/yuwtennis/apache-beam-deployment-models/wiki/Flink-Session-Cluster-on-Docker) 