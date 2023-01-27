from mushroom.entity import artifact_entity,config_entity
from mushroom.exception import MushroomException
from mushroom.logger import logging
from typing import Optional
import os,sys 
from xgboost import XGBClassifier
from mushroom import utils
from sklearn.metrics import f1_score


class ModelTrainer:
    def __init__(self,model_trainer_config:config_entity.ModelTrainerConfig,
                data_transformation_artifact:artifact_entity.DataTransformationArtifact
                ):
        try:
            logging.info(f"{'>>'*20} Model Trainer {'<<'*20}")
            self.model_trainer_config=model_trainer_config
            self.data_transformation_artifact=data_transformation_artifact

        except Exception as e:
            raise MushroomException(e, sys)

    def fine_tune(self):
        try:
            #Wite code for Grid Search CV or Random Search
            #Implemented random-search-cv
            params={
                    "learning_rate"    : [0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ] ,
                    "max_depth"        : [ 3, 4, 5, 6, 8, 10, 12, 15],
                    "min_child_weight" : [ 1, 3, 5, 7 ],
                    "gamma"            : [ 0.0, 0.1, 0.2 , 0.3, 0.4 ],
                    "colsample_bytree" : [ 0.3, 0.4, 0.5 , 0.7 ]
                    }
            random_search = RandomizedSearchCV(classifier,param_distributions=params,n_iter=5,scoring='roc_auc',n_jobs=-1,cv=5,verbose=3)
            random_search.fit(x,y)
            return random_search.best_estimator_,random_search.best_params_
            

        except Exception as e:
            raise MushroomException(e, sys)

    def train_model(self,x,y):
        try:
            xgb_clf =  XGBClassifier(max_depth = 2 , min_child_weight = 3,colsample_bytree=0.1)
            xgb_clf.fit(x,y)
            return xgb_clf
        except Exception as e:
            raise MushroomException(e, sys)


    def initiate_model_trainer(self,)->artifact_entity.ModelTrainerArtifact:
        try:
            logging.info(f"Loading train and test array.")
            train_arr = utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_path)
            test_arr = utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_path)

            logging.info(f"Splitting input and target feature from both train and test arr.")
            x_train,y_train = train_arr[:,:-1],train_arr[:,-1]
            x_test,y_test = test_arr[:,:-1],test_arr[:,-1]

            logging.info(f"Train the model")
            model = self.train_model(x=x_train,y=y_train)

            logging.info(f"Calculating f1 train score")
            yhat_train = model.predict(x_train)
            f1_train_score  =f1_score(y_true=y_train, y_pred=yhat_train)

            logging.info(f"Calculating f1 test score")
            yhat_test = model.predict(x_test)
            f1_test_score  =f1_score(y_true=y_test, y_pred=yhat_test)
            
            logging.info(f"train score:{f1_train_score} and tests score {f1_test_score}")
            #check for overfitting or underfiiting or expected score
            logging.info(f"Checking if our model is underfitting or not")
            if f1_test_score<self.model_trainer_config.expected_score:
                raise Exception(f"Model is not good as it is not able to give \
                expected accuracy: {self.model_trainer_config.expected_score}: model actual score: {f1_test_score}")

            logging.info(f"Checking if our model is overfiiting or not")
            diff = abs(f1_train_score-f1_test_score)

            if diff>self.model_trainer_config.overfitting_threshold:
                raise Exception(f"Train and test score diff: {diff} is more than overfitting threshold {self.model_trainer_config.overfitting_threshold}")

            #save the trained model
            logging.info(f"Saving mode object")
            utils.save_object(file_path=self.model_trainer_config.model_path, obj=model)

            #prepare artifact
            logging.info(f"Prepare the artifact")
            model_trainer_artifact  = artifact_entity.ModelTrainerArtifact(model_path=self.model_trainer_config.model_path, 
            f1_train_score=f1_train_score, f1_test_score=f1_test_score)
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        except Exception as e:
            raise MushroomException(e, sys)



