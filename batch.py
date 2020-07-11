import apache_beam as beam
import argparse
from apache_beam.options.pipeline_options import PipelineOptions
from sys import argv

PROJECT_ID = 'aniket-g'
SCHEMA = 'sr:INTEGER,abv:FLOAT,id:INTEGER,name:STRING,style:STRING,ounces:FLOAT'

def discard_incomplete(data):
    """Filters out records that don't have an information."""
    return len(data['abv']) > 0 and len(data['id']) > 0 and len(data['name']) > 0 and len(data['style']) > 0


def convert_types(data):
    """Converts string values to their appropriate type."""
    data['abv'] = float(data['abv']) if 'abv' in data else None
    data['id'] = int(data['id']) if 'id' in data else None
    data['name'] = str(data['name']) if 'name' in data else None
    data['style'] = str(data['style']) if 'style' in data else None
    data['ounces'] = float(data['ounces']) if 'ounces' in data else None
    return data

def del_unwanted_cols(data):
    """Delete the unwanted columns"""
    del data['ibu']
    del data['brewery_id']
    return data

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    known_args = parser.parse_known_args(argv)

    p = beam.Pipeline(options=PipelineOptions())

    (p | 'ReadData' >> beam.io.ReadFromText('gs://ag-pipeline/batch/beers.csv', skip_header_lines =1)
       | 'SplitData' >> beam.Map(lambda x: x.split(','))
       | 'FormatToDict' >> beam.Map(lambda x: {"sr": x[0], "abv": x[1], "ibu": x[2], "id": x[3], "name": x[4], "style": x[5], "brewery_id": x[6], "ounces": x[7]}) 
       | 'DeleteIncompleteData' >> beam.Filter(discard_incomplete)
       | 'ChangeDataType' >> beam.Map(convert_types)
       | 'DeleteUnwantedData' >> beam.Map(del_unwanted_cols)
       | 'WriteToBigQuery' >> beam.io.WriteToBigQuery(
           '{0}:beer.beer_data'.format(PROJECT_ID),
           schema=SCHEMA,
           write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND))
    result = p.run()
    result.wait_until_finish()
