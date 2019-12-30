FROM alpine:latest

WORKDIR /app

RUN apk update && apk add --no-cache --virtual .build-deps \
      curl \
      && curl https://repo1.maven.org/maven2/org/apache/beam/beam-runners-flink-1.8-job-server/2.16.0/beam-runners-flink-1.8-job-server-2.16.0.jar -L -O -s \
      && apk del .build-deps

RUN apk add --no-cache openjdk8-jre

ENTRYPOINT java -jar /app/beam-runners-flink-1.8-job-server-2.16.0.jar --flink-master-url ${FLINK_MASTER_URL} --artifacts-dir ${ARTIFACTS_DIR} --job-host ${JOB_HOST} --job-port ${JOB_PORT}
