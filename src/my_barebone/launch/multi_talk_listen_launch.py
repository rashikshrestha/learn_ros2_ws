from launch import LaunchDescription
from launch_ros.actions import Node

#! 'generate_launch_description() is the function required for launch file
#! you cannot change the name of this function, else ros2 won't reconize it!!
def generate_launch_description():
    node1 = Node(
        package='my_barebone',
        executable='one_talk_two_listen',
        
    )
    
    node2 = Node(
        package='my_barebone',
        executable='two_talk_one_listen',
    )
    
    launch_description = LaunchDescription([node1, node2])
    
    return launch_description