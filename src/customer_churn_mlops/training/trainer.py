from customer_churn_mlops.common.logger import logger


class ModelTrainer:
    """
    Train, evaluate and save the best ML model.
    """

    def __init__(self):
        logger.info("Initializing Model Trainer...")
