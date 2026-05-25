from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='greenhouse_system',
            executable='temp',
            name='temperature_sensor'
        ),

        Node(
            package='greenhouse_system',
            executable='hum',
            name='humidity_sensor'
        ),

        Node(
            package='greenhouse_system',
            executable='brain',
            name='climate_brain'
        ),

        Node(
            package='greenhouse_system',
            executable='sprinkler',
            name='sprinkler_actuator'
        )
    ])
