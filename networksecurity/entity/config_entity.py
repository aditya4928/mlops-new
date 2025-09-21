#All configuration details specified here

from datetime import datetime
import os
from networksecurity.constant import training_pipeline

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)


class TrainingPipelineConfig:
    def __init__(self):
        # Name of the pipeline
        self.pipeline_name = training_pipeline.PIPELINE_NAME #"NetworkSecurity"
        
        
        timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")  # Unique timestamp for each run
        self.artifact_dir = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp) # Directory where all outputs/artifacts of this run will be saved ("artifact")
        
        # Directory to save final trained model
        self.model_dir = os.path.join("final_model") # "final_model"
        
        # Save timestamp as a string for reference
        self.timestamp = timestamp


# This class holds configuration specifically for data ingestion
class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME  #"Artifacts/data_ingestion"
        )
        
        # Path to save feature store CSV file
        self.feature_store_file_path = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,  #"Artifacts/data_ingestion/feature_store/phisingData.csv"
            training_pipeline.FILE_NAME 
        )
        
        # Path to save training CSV file
        
        self.training_file_path = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR, #"Artifacts/data_ingestion/ingested/train.csv"
            training_pipeline.TRAIN_FILE_NAME 
        )
        
        # Path to save testing CSV file
        
        self.testing_file_path = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,  # "Artifacts/data_ingestion/ingested/test.csv"
            training_pipeline.TEST_FILE_NAME 
        )
        
        # Train-test split ratio
        self.train_test_split_ratio = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        
        # MongoDB collection and database names
        self.collection_name = training_pipeline.DATA_INGESTION_COLLECTION_NAME  # "NetworkData"
        self.database_name = training_pipeline.DATA_INGESTION_DATABASE_NAME  # "mlops"

