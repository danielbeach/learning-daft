from daft.io import IOConfig, S3Config
import daft
import os
from datetime import datetime

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")

def handler(event, context):
       t1 = datetime.now()
       io_config = IOConfig(s3=S3Config(key_id=os.environ['AWS_ACCESS_KEY_ID'], 
                                          access_key=os.environ['AWS_SECRET_ACCESS_KEY']))
       raw_data = daft.read_csv("s3://confessions-of-a-data-guy/daft-large-data/output.csv",
                                   io_config=io_config)


       raw_data.collect().write_deltalake("s3://confessions-of-a-data-guy/daftdeltalake", mode="overwrite")
       t2 = datetime.now()
       print(f"Time taken: {t2-t1}")