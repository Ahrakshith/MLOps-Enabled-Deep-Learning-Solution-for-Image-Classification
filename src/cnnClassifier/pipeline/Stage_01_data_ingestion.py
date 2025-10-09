from numpy.ma.core import get_data

from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier import logger


STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        self.config=ConfigurationManager()
        self.data_ingestion_config=self.config.get_data_ingestion_config()
        self.data_ingestion = DataIngestion(config=self.data_ingestion_config)
        self.data_ingestion.download_file()
        self.data_ingestion.extract_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
