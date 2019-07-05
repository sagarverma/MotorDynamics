import torch

from motor_dynamics.utils.parser import get_parser_with_args
from motor_dynamics.train import train

parser = get_parser_with_args()
opt = parser.parse_args()

if opt.task == 'train_sim':
    train(opt)
