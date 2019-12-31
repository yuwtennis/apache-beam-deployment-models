# -*- coding: utf-8 -*-

import os
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

def main():

    sdk_endpoint = os.getenv('SDK_ENDPOINT')
    job_server   = os.getenv('JOB_SERVER')

    options = PipelineOptions([
                      "--runner=PortableRunner",
                      "--environment_config="+sdk_endpoint,
                      "--environment_type=EXTERNAL",
                      "--experiments=beam_fn_api",
                      "--job_endpoint="+job_server
                  ])

    options.view_as(SetupOptions).save_main_session = True

    with beam.Pipeline(options=options) as p:

        lines = ( p | beam.Create(['Hello World.']) )

if __name__ == "__main__":

    main()
