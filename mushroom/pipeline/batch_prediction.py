from mushroom.exception import MushroomException
from mushroom.logger import logging
from mushroom.predictor import ModelResolver
import pandas as pd
from mushroom.utils import load_object
from sklearn.preprocessing import LabelEncoder
import os,sys
from datetime import datetime

PREDICTION_DIR = "prediction"

import numpy as np
def start_batch_prediction(input_file_path):
    try:
        os.makedirs(PREDICTION_DIR,exist_ok=True)
        logging.info(f"Creating model resolver object")
        model_resolver = ModelResolver(model_registry="saved_models")
        logging.info(f"Reading file :{input_file_path}")
        df = pd.read_csv(input_file_path)

        #Handling Preprocessing before Transformation
        df.replace({"na":np.NAN},inplace=True)
        df['stalk-root'] = df['stalk-root'].replace(to_replace='?',value=np.nan)
        

        #validation
        logging.info(f"Loading transformer to transform dataset")
        transformer = load_object(file_path=model_resolver.get_latest_transformer_path())
        
        input_feature_names =  list(transformer.feature_names_in_)
        
        #Encoding test_df for evaluation
        label_encoder = LabelEncoder()
        for i in input_feature_names:
            df[i] = label_encoder.fit_transform(df[i])
            
        logging.info(df[input_feature_names].head())

        input_arr = transformer.transform(df[input_feature_names])

        logging.info(f"Loading model to make prediction")
        model = load_object(file_path=model_resolver.get_latest_model_path())
        prediction = model.predict(input_arr)
        
        logging.info(f"Target encoder to convert predicted column into categorical")
        target_encoder = load_object(file_path=model_resolver.get_latest_target_encoder_path())

        cat_prediction = target_encoder.inverse_transform(prediction)

        df["prediction"]=prediction
        df["cat_pred"]=cat_prediction


        prediction_file_name = os.path.basename(input_file_path).replace(".csv",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.csv")
        prediction_file_path = os.path.join(PREDICTION_DIR,prediction_file_name)
        df.to_csv(prediction_file_path,index=False,header=True)
        return prediction_file_path
    except Exception as e:
        raise MushroomException(e, sys)