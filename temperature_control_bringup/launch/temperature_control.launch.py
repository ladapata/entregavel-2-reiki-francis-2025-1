from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    ld = LaunchDescription()

    node_1 = Node(
	package='temperature_control',
	executable='temperature_monitor',
	name='temperature_monitor'
	)

    node_2 = Node(
	package='temperature_control',
	executable='temperature_avg_monitor',
	name='temperature_avg_monitor'
	)

    node_3 = Node(
	package='temperature_control',
	executable='temperature_publisher',
	name='temperature_publisher'
	)

    node_4 = Node(
	package='temperature_control',
	executable='average_client_reset',
	name='average_client_reset'
	)
    
    ld.add_action(node_1)
    ld.add_action(node_2)
    ld.add_action(node_3)
    ld.add_action(node_4)
    
    return ld
