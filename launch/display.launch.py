from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_share = get_package_share_directory('my_robot_rviz')  # your package name
    urdf_file = os.path.join(pkg_share, 'urdf', 'my_robot.urdf')  # path to your URDF

    with open(urdf_file, 'r') as infp:
        robot_description = infp.read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}],
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            # You can specify a config file if you want:
            # arguments=['-d', os.path.join(pkg_share, 'rviz', 'config.rviz')],
        ),
    ])
