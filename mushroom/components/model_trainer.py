import os,sys
from mushroom.exception import MushroomException 
from mushroom.logger import logging
from datetime import datetime

class TrainingPipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception  as e:
            raise MushroomException(e,sys)   

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name="mushroom_classification"
            self.collection_name="mushroom"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir , "data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2
        except:
            raise MushroomException(e,sys)   
    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception  as e:
            raise MushroomException(e,sys) 

class DataTransformationConfig:
    pass

class DataValidationConfig:
    pass

class ModelTrainerConfig:
    pass


class ModelEvaluationConfig:
    pass

class ModelPusherConfig:
    pass
