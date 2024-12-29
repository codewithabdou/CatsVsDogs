import os
from zipfile import ZipFile
from CatsVsDogs.entity import DataIngestionConfig
from CatsVsDogs.logging import logger


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        logger.info(f"Data Ingestion initialized with config: {config}")

    
    def _get_updated_list_of_files(self, list_of_files):
        logger.info(f"Filtering files from total {len(list_of_files)} files")
        updated_files = [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]
        logger.info(f"Found {len(updated_files)} valid image files")
        return updated_files
    
    
    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        
        if not os.path.exists(target_filepath):
            logger.debug(f"Extracting file: {f}")
            zf.extract(f, working_dir)
            logger.info(f"Extracted file: {f} to {target_filepath}")
        else:
            logger.debug(f"File already exists: {f}")
        
        if os.path.getsize(target_filepath) == 0:
            logger.warning(f"Found empty file, removing: {f}")
            os.remove(target_filepath)


    def unzip_and_clean(self):
        logger.info(f"Starting unzip and clean process from {self.config.local_data_file}")
        try:
            with ZipFile(file=self.config.local_data_file, mode="r") as zf:
                logger.debug("ZIP file opened successfully")
                list_of_files = zf.namelist()
                logger.info(f"Found {len(list_of_files)} files in zip archive")
                
                updated_list_of_files = self._get_updated_list_of_files(list_of_files)
                
                logger.info(f"Starting preprocessing of {len(updated_list_of_files)} files")
                for f in updated_list_of_files:
                    self._preprocess(zf, f, self.config.unzip_dir)
                
                logger.info("Unzip and clean process completed successfully")
        except Exception as e:
            logger.error(f"Error during unzip and clean process: {str(e)}")
            raise e