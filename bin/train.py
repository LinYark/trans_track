import os
import argparse
from algo.nodes.train_debug import run_train_debug
from algo.nodes.train_normal import run_train_normal

def parse_args():
    """
    args for training.
    """
    parser = argparse.ArgumentParser(description='Parse args for training')
    # for train
    parser.add_argument('--config', type=str,default='config_s', help='yaml configure file name')
    parser.add_argument('--yaml', type=str, default='baseline_s',help='yaml configure file name')
    parser.add_argument('--save_dir', type=str, default="checkpoints", help='root directory to save checkpoints, logs, and tensorboard')
    parser.add_argument('--mode', type=str, choices=["debug", "normal"], default="debug", help="train on single gpu or multiple gpus")
    parser.add_argument('--nproc_per_node', default=1,type=int, help="number of GPUs per node")
    # whether datasets are in lmdb format
    parser.add_argument('--use_lmdb', type=int, choices=[0, 1], default=0)

    args = parser.parse_args()
    return args


def main():
    # Get Input
    args = parse_args()
    setting = { "config":args.config, "save_dir":args.save_dir, "mode": args.mode,\
        "nproc_per_node":args.nproc_per_node,"use_lmdb":args.use_lmdb,"yaml":args.yaml
    }

    assert args.mode == "debug" or args.mode == "normal"
    if args.mode == "debug":
        run_train_debug(setting)
    else:
        run_train_normal(setting)

if __name__ == "__main__":
    main()
