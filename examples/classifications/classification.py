import pandas as pd
from adobe_analytics import Client, ClassificationUploader

client = Client.from_json("my_credentials.json")
suites = client.suites()
suite_ids = list(suites.keys())

dataframe = pd.read_csv("my_classification_data.csv")

uploader = ClassificationUploader(
    client=client,
    suite_ids=suite_ids,
    variable_id="evar24",
    data=dataframe,
    email="my_email",
    description="my trial classification for evar24."
)
uploader.upload()
