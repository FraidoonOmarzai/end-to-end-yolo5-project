# end-to-end-yolo5-project
* implementation of end to end waste-detection using yolo5 on custom datasets

## Steps:

1. Git clone the repository and Define template of the project

```bash
touch template.py
python3 template.py
```

2. define setup.py scripts, Create environment and install dependencies

```bash
conda create -n yolo5 python=3.7 -y
conda activate yolo5 
pip install -r requirements.txt
```
3. Install labelimg and preparing the dataset
```bash
pip3 install labelImg
labelimg
```

* our images folders should be in the following structures and add the images in train and val
* Then we will use `labelimg` to get classes and coordinates.
* Prepare the dataset and store in google drive
```bash
# folder structures
images
└───train <- training images
│   └───images
│   │   │   ---.jpeg
│   │   │   ---.jpeg
│   │   │   ...      
│   └───labels
│       │   ---
│       │   ...
│   
└───val <- testing images
│   └───images
│   │   │   ---.jpeg
│   │   │   ---.jpeg
│   │   │   ...      
│   └───labels
│       │   ---
│       │   ... 
|
|_____data.yaml

```

4. Define `logging`, `utils` and `exception handlers`

5. Run the notebook in google colab for testing purposes and download it to research directory
```bash
# Implementation of waste-detection using yolo5 in colab

* clone YOLOv5 repository
* install dependencies `requirements.txt`
* download the dataset from google drive and unzip
* Define Model Configuration and Architecture
* Train Custom YOLOv5 Detector
* Evaluate Custom YOLOv5 Detector Performance
* Export Trained Weights for Future Inference
```

```bash
### Workflows:
1. Update config.yaml
2. Update params.yaml
3. Update the entity and configuration manager `yolo5/entity/config_entity.py`
4. Update the components
5. Update the pipeline 
6. Update dvc.yaml
```

6. **Data Ingestion**
* define config/config.yaml -> create 01_data_ingestion.ipynb
* define config_entity.py -> create components/data_ingestion.py -> add pipeline and run dvc.yaml
```bash
dvc init
dvc repro
```

7. **Data validation**
* check whether the files and directories are exist
* define config/config.yaml -> create 02_data_validation.ipynb
* define config_entity.py -> create components/data_validation.py -> add pipeline and run dvc.yaml

8. **Model Training**
* git clone the yolo5 repository
```bash
# clone YOLOv5 repository
git clone https://github.com/ultralytics/yolov5.git  # clone repo
```