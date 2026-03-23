# Swarm Gym PyBullet Drones

Swarm's fork of `gym-pybullet-drones` packages the quadrotor simulation environments we use for Swarm benchmark and control workloads.

This fork keeps the Gymnasium and Stable-Baselines3 2.x compatible environment surface, while adding Swarm-specific improvements:

- custom drone parameters used by Swarm evaluation workloads
- 5D action space with yaw control for richer policy outputs
- yaw-control float32 precision fix for stable behavior at extreme values
- benchmark-oriented environment simplifications used by our training and evaluation loops

Repository: https://github.com/swarm-subnet/swarm-gym-pybullet-drones
