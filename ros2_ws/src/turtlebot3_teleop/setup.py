from setuptools import setup

package_name = 'turtlebot3_teleop'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[
        'turtlebot3_teleop.teleop_node',
        'turtlebot3_teleop.turtlebot_controller',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Seu Nome',
    maintainer_email='seu_email@example.com',
    description='Pacote de teleoperação para Turtlebot3',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop_node = turtlebot3_teleop.teleop_node:main',
            'turtlebot_controller = turtlebot3_teleop.turtlebot_controller:main',
        ],
    },
)

