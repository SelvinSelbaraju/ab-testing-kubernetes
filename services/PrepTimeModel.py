import joblib
import pandas as pd 
import os
import logging
import datetime
logging.basicConfig(
    level=logging.INFO
) 

class PrepTimeModel(object):
    def __init__(self, models_dir="./models"):
        self.version = os.getenv("VERSION")
        self.models_dir = models_dir
        self.baseline_result = os.getenv("BASELINE_RESULT")
        self.model = None

        if self.baseline_result:
            logging.info(f"Using Baseline Constant Result of: {self.baseline_result}")
        else:
            logging.info("Loading Trained Model")
            self.model = joblib.load(f"{self.models_dir}/model.pkl")
    
    def predict(self, X, feature_names):
        logging.info("Request Received")
        data = pd.DataFrame(X, columns=feature_names)
        logging.info(data)
        predictions = self.model.predict(data)
        return predictions
    
    def metrics(self):
        return [
            # {"type": "GAUGE", "key": "gauge_runtime", "value": self.run_time}
        ]
    
    def tags(self):
        return {"version": self.version}

        
            
