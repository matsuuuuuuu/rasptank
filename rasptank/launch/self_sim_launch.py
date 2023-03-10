import os


from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.actions import LogInfo
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    port = LaunchConfiguration('port', default='/dev/ttyUSB0')

    frame_id = LaunchConfiguration('frame_id', default='base_scan')
    return LaunchDescription([
        Node(
            package='rasptank',
            executable='velocity_publisher',
            #parameters=[{'use_sim_time':True}],
        ),
        Node(
            package='rasptank',
            executable='sim_relayer',
            #parameters=[{'use_sim_time':True}],
        ),
        DeclareLaunchArgument(
            'port',
            default_value=port,
            description='Specifying usb port to connected lidar'),

        DeclareLaunchArgument(
           'frame_id',
            default_value=frame_id,
            description='Specifying frame_id of lidar. Default frame_id is \'laser\''),

        Node(
            package='hls_lfcd_lds_driver',
            executable='hlds_laser_publisher',
            name='hlds_laser_publisher',
            parameters=[{'port': port, 'frame_id': frame_id}],
           output='screen'),

    ])