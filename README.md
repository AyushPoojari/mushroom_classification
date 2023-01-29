# Mushroom Classification System

The project classifies the given real time dataset of Mushroom as poisonous or edible . It uses python , MongoDB , AWS and Apache Airflow to accomplish this.


<b>Documentation :</b>

<b>1. High Level Document (HLD) :</b> https://drive.google.com/file/d/1vCMnj9Il1AFOQ5eimC1mL5PuGzMRZ-iN/view?usp=sharing <br>
<b>2. Low Level Document (LLD) :</b> https://drive.google.com/file/d/1vCMnj9Il1AFOQ5eimC1mL5PuGzMRZ-iN/view?usp=sharing <br>
<b>3. Architecture :</b> https://drive.google.com/file/d/1vCMnj9Il1AFOQ5eimC1mL5PuGzMRZ-iN/view?usp=sharing <br>
<b>4. Wireframe Document :</b> https://drive.google.com/file/d/1vCMnj9Il1AFOQ5eimC1mL5PuGzMRZ-iN/view?usp=sharing <br>
<b>5. Detailed Project Report (DPR) :</b> https://drive.google.com/file/d/1vCMnj9Il1AFOQ5eimC1mL5PuGzMRZ-iN/view?usp=sharing <br>

<b>ABSTRACT :</b>
Mushrooms have been consumed since earliest history. The word Mushroom is derived from the French word for Fungi and Mold. Now-a-days, Mushroom are popular valuable food because they are low in calories, carbohydrate, Fat, sodium and also cholesterol free. Besides this, Mushroom provides important nutrients, including selenium, potassium, riboflavin, niacin, Vitamin D, proteins and fiber. All together with a long history as food source. Mushroom are important for their healing capacity and properties in traditional medicine. It has reported beneficial effects for health and treatment of some disease. Many nutraceutical properties are described in Mushroom like cancer and antitumor attributes. Mushroom act as antibacterial, immune system enhancer and cholesterol lowering Agent. Additionally, they are important source of bio-active compounds. This work is a machine learning model that classifies mushrooms into 2 classes: Poisonous and Edible depending on the features of the mushroom. During this machine learning implementation, we are going to see which features are important to predict whether a mushroom is poisonous or edible.

<b>Problem Statement :</b>
The Audubon Society Field Guide to North American Mushrooms contains descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom (1981). Each species is labelled as either definitely edible, definitely poisonous, or maybe edible but not recommended. This last category was merged with the toxic category. The Guide asserts unequivocally that there is no simple rule for judging a mushroom's edibility, such as "leaflets three, leave it be" for Poisonous Oak and Ivy.

The main goal is to predict which mushroom is poisonous & which is edible.

<b>Tools Used :</b>

![image](https://drive.google.com/drive/u/0/folders/1gZ2L2oNv_QhRDS3XSRlkQb-v4m8C3qPg)

<b>Architecture :</b>

![image](https://drive.google.com/drive/u/0/folders/1gZ2L2oNv_QhRDS3XSRlkQb-v4m8C3qPg)

<b>Apache Airflow Interface :</b>

![image](https://drive.google.com/file/d/12nG4OmW6bZ-3kVeJzql-KWUaBe-qZeyK/view?usp=sharing) 
![image](https://drive.google.com/file/d/1qXJp1b82Mhr7jhpqV9AChZXn39PeP9F1/view?usp=sharing) 
![image](https://drive.google.com/file/d/1cWpmeQt6DR1LINk2QW6ZsNRiJUvy9eeF/view?usp=sharing) 



<b> Conclusion :</b>
- The classification system is successfull able to classify the real-time data wit an accuracy of ~100%.
- The 'poisonous' mushrooms do not have Population Type as Numerous and Abundant according to our data.
- The 'poisonous' mushrooms do not have Habitat Type as Waste according to our data.
- The XGBoost Classifier model has 100% accuracy on both training data and test data.
