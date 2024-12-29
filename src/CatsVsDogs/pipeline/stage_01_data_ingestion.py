from CatsVsDogs.config import ConfigurationManager
from CatsVsDogs.components import DataIngestion
from CatsVsDogs.utils import download_file

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        download_file(url=data_ingestion_config.source_URL , dest_path=data_ingestion_config.local_data_file)
        data_ingestion.unzip_and_clean()