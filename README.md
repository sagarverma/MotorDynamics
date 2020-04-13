# MotorNN
Train neural network model to learn electrical motor dynamics from electrical quantities.

### Simulated dataset generation
```
git clone https://github.com/sagarverma/MotorRefGen

cd /usr/local/MATLAB/{VERSION}/extern/engines/
sudo chmod -R 775 python
cd python
pip install -e .

cd MotorRefGen
pip install -r requirements.txt
pip install -e .

mkdir dataset

python motorrefgen/gen_sim_pkls.py  --save_dir=../dataset/ --set=train --samples=50
python motorrefgen/gen_sim_pkls.py  --save_dir=../dataset/ --set=val --samples=50
```

### Usage
```
pip install -r requirements.txt
pip install -e .
python motornn/train.py [PASS PROPER ARGS]
```

### Run tests
```
pytest
```
