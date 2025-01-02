from CatsVsDogs.pipeline import BaseModelPreparationPipeline , DataIngestionTrainingPipeline , TrainingPipeline


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
     
STAGE_NAME = "Base Model Preparation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   base_model_preparation = BaseModelPreparationPipeline()
   base_model_preparation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.critical(f"stage {STAGE_NAME} failed")
        raise e
     
STAGE_NAME = "Training stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   training_pipeline = TrainingPipeline()
   training_pipeline.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.critical(f"stage {STAGE_NAME} failed")
        raise e