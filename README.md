# apache-beam-deployment-models

Sample deployment models for apache beam. Pipelines are created using python.

## Directory model
```
.
├── libs                              # Libraries used for models
├── __main__.py                       # Entry point
├── models                            # Files required for deployment
│   └── flink-session-cluster
│       ├── docker-compose.yml
│       └── Dockerfile
├── README.md
└── requirements.txt
```

## Available deployment models
This repository includes configuration for sample beam deployment.

For detailed instructions for deploying (see [wiki](https://github.com/yuwtennis/beam-deployment/wiki))
