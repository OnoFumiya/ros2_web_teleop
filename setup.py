import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'ros2_web_teleop'

def get_recursive_files(data_dir: str, install_dir: str) -> list[tuple[str, list[str]]]:
    file_list: list[tuple[str, list[str]]] = []
    for root, dirs, files in os.walk(data_dir):
        dirs[:] = [directory for directory in dirs if directory != "__pycache__"]
        filtered_files = [file_name for file_name in files if not file_name.endswith(".pyc")]
        if filtered_files:
            relative_path = os.path.relpath(root, data_dir)
            target_path = os.path.join(install_dir, relative_path)
            file_list.append(
                (target_path, [os.path.join(root, file_name) for file_name in filtered_files])
            )
    return file_list

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'img'), glob('img/*')),
        *get_recursive_files("web", os.path.join("share", package_name, "web")),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='OnoFumiya',
    maintainer_email='fumiyaono.choi@gmail.com',
    description='A web-based ROS 2 teleoperation interface for controlling robots from a smartphone.',
    license='BSD 3-Clause License',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'teleop_node = ros2_web_teleop.teleop_node:main',
        ],
    },
)
