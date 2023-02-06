import os
from glob import glob

from setuptools import setup

package_name = 'rasptank'
submodules = 'rasptank/control_modules'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, submodules],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), 
				glob('launch/self_sim_launch.py')),
        (os.path.join('share', package_name), 
				glob('launch/move_robot_launch.py')),
        (os.path.join('share', package_name), 
				glob('launch/color_tracking_launch.py')),
																					 				 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'color_tracking = rasptank.color_tracking:main',
            'color_tracking_cpy = rasptank.copy_color_tracking:main',
            'check_color = rasptank.check_color:main', 
        ],
    },
)
