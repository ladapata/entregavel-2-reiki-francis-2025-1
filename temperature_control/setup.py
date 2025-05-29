from setuptools import find_packages, setup

package_name = 'temperature_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
    		'temperature_monitor = temperature_control.temperature_monitor:main', # temperature_monitor PUBLISHER, SUBSCRIBER e SERVICE SERVER
    		'temperature_publisher = temperature_control.temperature_publisher:main', # temperature_publisher PUBLISHER
    		'temperature_avg_monitor = temperature_control.temperature_avg_monitor:main', # temperature_avg_monitor SUBSCRIBER
    		'average_client_reset = temperature_control.average_client_reset:main' # average_reset_client CLIENT
        ],
    },
)
