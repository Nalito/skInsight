# skin-defect-detection
![skInsight](logo.png)

## Initial Setup:
Clone repo and create a virtual environment
```
$ git clone https://github.com/Nalito/skin-defect-detection.git
$ cd skin-defect-detection
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install -r requirements.txt
```

## Model Development
The model development code is contained in this [Jupyter notebook](skin_defect_detection.ipynb).

## Deployment to Azure App Services
The deployed application is available here: [skInsight](https://skinsight-e6e6hmhhgjfdf7ec.canadacentral-01.azurewebsites.net/) 🤗

## Streamlit Deployment
```
$ (venv) streamlit run
```

The deployed application is available here: https://skinsight.streamlit.app/ 🤗
