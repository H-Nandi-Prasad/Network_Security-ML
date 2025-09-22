import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import  DataIngestionConfig
from networksecurity.entity.artifacts_entity import DataIngestionArtifacts
from networksecurity.entity.config_entity import TrainingPipelineConfig


if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiating the ingestion")
        dataingestionartifacts=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifacts)

    except Exception as e:
        raise NetworkSecurityException(sys,e)