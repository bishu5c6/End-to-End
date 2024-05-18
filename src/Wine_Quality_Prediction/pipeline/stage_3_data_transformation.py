from src.Wine_Quality_Prediction.exception import CustomException
from src.Wine_Quality_Prediction import logger
from src.Wine_Quality_Prediction.components.data_transformation import DataTransformation
from src.Wine_Quality_Prediction.config.configuration import ConfigurationManager
from pathlib import Path


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()

            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            logger.exception(e)
            raise CustomException(e, sys)
            