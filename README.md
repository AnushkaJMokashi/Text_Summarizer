# Text_Summarizer
* Create new envirnment
conda create -n "textS2" python==3.8

* Activate new Environment
conda activate textS2

* Install Directories
pip install -r "requirements.txt"

## If error in installation
pip cache purge
pip install --upgrade pip setuptools wheel
pip install pywinpty==2.0.10
pip install -r requirements.txt

## Run Main file to start pipeline
python main.py
