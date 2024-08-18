#! ROS2 imports
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimpleListener(Node):
    def __init__(self):
        super().__init__("simple_listener") # Name of Node
        
        #! Create a Subscriber
        self.my_subscriber = self.create_subscription(
            String, 'random_name', self.my_listener_callback, 10
        )
        
        self.get_logger().info("Simple Listener has started listening!")
       
    def my_listener_callback(self, msg):
        self.get_logger().info(f"I heard: {msg.data}")
        

def main():
    rclpy.init()
    simple_listener = SimpleListener()
    rclpy.spin(simple_listener)
    simple_listener.destroy_node()
    rclpy.shutdown()
    

if __name__=='__main__':
    main()