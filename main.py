from CatsVsDogs.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from CatsVsDogs.logging import logger



STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.critical(f"stage {STAGE_NAME} failed")
        raise e