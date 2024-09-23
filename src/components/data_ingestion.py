import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#intialize the data ingestion configuration

@dataclass

class DataIngestionconfig:
    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")
    raw_data_path=os.path.join("artifacts","raw.csv")


#cretate a data ingestion class

class DataIngestion:
    def __init__(self):
        self.ingestion_cofig=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method starts")


        try:
            df=pd.read_csv(os.path.join("notebooks/data/gemstone.csv"))
            logging.info("Dataset read as pandas Dataframe")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_cofig.raw_data_path)), exist_ok=True)

            df.to_csv(self.ingestion_cofig.raw_data_path,index=False)

            logging.info("train test split")
            train_set,test_set=train_test_split(df,test_size=0.3,random_state=42)
            train_set.to_csv(self.ingestion_cofig.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_cofig.test_data_path,index=False,header=True)

            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_cofig.train_data_path,
                self.ingestion_cofig.test_data_path


            )



        except Exception as e:
            logging.info("Error occured in Data Ingestion copnfig")
            raise CustomException(e,sys)


           
