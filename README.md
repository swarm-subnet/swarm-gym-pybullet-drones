# Swarm Gym PyBullet Drones

This repository is Swarm Subnet's fork of `gym-pybullet-drones`.

It is maintained for the specific control and evaluation workloads used by Swarm benchmark. Compared with the upstream project, this fork includes Swarm-specific simulation changes such as:

- a custom drone configuration used in Swarm environments
- a 5D action space with explicit yaw control
- a float32 precision fix for yaw control at extreme values
- benchmark-oriented environment simplifications for our RL and control loops

The package remains compatible with `gymnasium` and `stable-baselines3` 2.x, and continues to expose the `gym_pybullet_drones` Python package.

## Installation

```sh
git clone git@github.com:swarm-subnet/swarm-gym-pybullet-drones.git
cd swarm-gym-pybullet-drones

conda create -n swarm-drones python=3.10
conda activate swarm-drones

pip install --upgrade pip
pip install -e .
```

## Usage

The environments register through `gym_pybullet_drones` exactly as in upstream. The fork is intended to be consumed by Swarm benchmark and related training code, but the examples remain usable for local experimentation.

## Relationship to upstream

This fork started from `gym-pybullet-drones` and keeps the core environment structure, while carrying Swarm-specific changes needed for our drone evaluation workloads.

Upstream project: https://github.com/utiasDSL/gym-pybullet-drones
Fork repository: https://github.com/swarm-subnet/swarm-gym-pybullet-drones
