# MSR-MiningChallenge26

## Setup
1. create virtual environment: virtualenv .venv
2. pip install -r requirements.txt
3. git clone https://huggingface.co/datasets/hao-li/AIDev

## Update requirements.txt
```
python -m pip freeze -l > requirements.txt
```
- Delete windows or OS specific requirements from the file (Eg., pywinpty)

## Run tests
```
python -m unittest discover -s tests  
```