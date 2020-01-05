import os
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.io.external.kafka import WriteToKafka
from apache_beam.io.textio import WriteToText

def main():

    sdk_endpoint = os.getenv('SDK_ENDPOINT')
    job_server   = os.getenv('JOB_SERVER')
    project_id   = os.getenv('PROJECT_ID')

    options = PipelineOptions([
                      "--runner=PortableRunner",
                      "--environment_config="+sdk_endpoint,
                      "--environment_type=EXTERNAL",
                      "--experiments=beam_fn_api",
                      "--job_endpoint="+job_server
                  ])

    options.view_as(SetupOptions).save_main_session = True

    with beam.Pipeline(options=options) as p:

        lines = ( p | beam.Create(['Hello World.', 'Apache beam']) )

        # Write to GCS
        ( lines | WriteToText('gs://{}/sample.txt'.format(project_id))
        )

        #
        # Send to kafka 
        # WriteToKafka
        # https://github.com/apache/beam/blob/master/sdks/python/apache_beam/io/external/kafka.py
        # 
        # Producer config
        # https://kafka.apache.org/documentation/#producerconfigs
        #
        #( lines  | beam.Map(lambda x: ('payload', x) )
        #         | WriteToKafka(
        #              { 'acks': 'all', 'bootstrap.servers': 'localhost:9092'},
        #              'beam',
        #              'org.apache.kafka.common.serialization.ByteArraySerializer',
        #              'org.apache.kafka.common.serialization.ByteArraySerializer',
        #              'localhost:8097' ))

if __name__ == "__main__":

    main()
