# Code for the paper "Modeling Electrical Motor Dynamics using Encoder-Decoder with Recurrent Skip Connection" (Accepted in AAAI 2020)

This is the github repository containing the code for the paper ["Modeling Electrical Motor Dynamics using Encoder-Decoder with Recurrent Skip Connection"](https://sagarverma.github.io/others/AAAI-VermaS.4719.pdf) by Sagar Verma, Nicolas Henwood, Marc Castella, Francois Malrait, and Jean-Christophe Pesquet.

[Project page](https://sagarverma.github.io/dynamics.html)

## Requirements
The code has been tested on:

- 2xNvidia V100 GPU
- Ubuntu 18.04 LTS on 48 vCPUs and 186 GB of RAM
- Python 3.6.10 
- [Pytorch](https://pytorch.org/) v1.4.0


## Dataset

[Motor Data](https://sagarverma.github.io/others/motor_data.tar.xz)


## Run

Installation

```
git clone https://github.com/INRIA-OPIS/MotorNN.git
git checkout AAAI2020_release
pip install -r requirements.txt
pip install -e .
```

Download and extract dataset. Create weights and logs path.

To train a model use following

```
cd MotorNN
python motor_dynamics/summoner.py --gpu=0 --task=train --train_sim_dir={DATA_PATH}/train_sim/ --val_sim_dir={DATA_PATH}/val_sim/ --weights_dir={WEIGHTS_PATH} --logs_dir={LOGS_PATH} --model=deep_cnn --epochs=100 --batch_size=512 --lr=0.1 --inp_quants='voltage_d,voltage_q,speed' --out_quants='current_d' --stride=1 --window=100 --act=relu --loss=mse
```

## Contact
For any queries, please contact
```
Sagar Verma: sagar15056@iiitd.ac.in
```
