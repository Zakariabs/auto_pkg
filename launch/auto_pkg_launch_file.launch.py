from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='auto_pkg',
            executable='auto',
            output='screen'),

    ])