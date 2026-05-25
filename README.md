# ROS2 Greenhouse Monitoring System

A ROS2 multi-node greenhouse automation project.

## Features
- Temperature sensor node
- Humidity sensor node
- Brain decision node
- Sprinkler actuator node
- ROS2 launch file

## Topics

| Topic | Type | Description |
|---|---|---|
| /climate/temp | Float32 | Temperature data |
| /climate/humidity | Float32 | Humidity data |
| /sprinkler_cmd | String | ON/OFF sprinkler command |

## Run Project

```bash
ros2 launch greenhouse_system greenhouse.launch.py
```

## Architecture

Temp Node ----\
               ---> Brain Node ---> Sprinkler
Humidity ------/

