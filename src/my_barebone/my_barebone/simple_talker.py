from random import choice
from string import ascii_lowercase
from wonderwords import RandomWord

#! ROS2 imports
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#! Node class
class SimpleTalker(Node):
    def __init__(self):
        super().__init__("simple_talker") # Name of the Node
       
        #! Create a Publisher 
        self.my_publisher = self.create_publisher(String, 'random_name', 10)
        
        #! Create a Timer
        self.my_timer = self.create_timer(0.5, self.my_timer_callback)
        
        #! Random word generator
        self.random_word_generator = RandomWord()
        
        #! Count
        self.count = 0
        
        self.get_logger().info("Simple Talker has started talking!")
        
    def my_timer_callback(self):
        #! Publish random word 
        my_msg = String()
        my_msg.data = self.get_random_word()
        self.my_publisher.publish(my_msg)
        
    def get_random_word(self):
        random_alphabet = choice(ascii_lowercase)
        w1 = self.random_word_generator.word(starts_with=random_alphabet, include_parts_of_speech=["adjectives"])
        w2 = self.random_word_generator.word(starts_with=random_alphabet, include_parts_of_speech=["nouns"])
        random_word = f"{self.count}. {w1} {w2}" 
        self.count += 1
        return  random_word

        
#! Main Function
def main():
    rclpy.init()
    simple_talker = SimpleTalker()
    rclpy.spin(simple_talker)
    simple_talker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()