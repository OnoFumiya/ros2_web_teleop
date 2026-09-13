from setuptools import find_packages, setup

package_name = 'ros2_web_teleop'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
        ],
    },
)
