from wonderwords import RandomWord

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TwoTalkOneListen(Node):
    def __init__(self):
        super().__init__('two_talk_one_listen')
        
        #! Publisher 1
        self.my_publisher_1 = self.create_publisher(String, '/random_word_a', 10)
        self.my_timer_1 = self.create_timer(0.5, self.my_timer_callback_1)
        
        #! Publisher 2
        self.my_publisher_2 = self.create_publisher(String, '/random_word_b', 10)
        self.my_timer_2 = self.create_timer(1, self.my_timer_callback_2)
        
        #! Subscriber
        self.my_subscriber = self.create_subscription(
            String, '/random_word_c', self.my_listener_callback, 10
        )
        
        #! Random word generator
        self.random_word_generator = RandomWord()
        
        self.get_logger().info("I talk random words starting from 'a'@0.5Hz and 'b'@1Hz, and listen to random words starting from 'c'")
        
        
    def my_timer_callback_1(self):
        msg = String()
        msg.data = self.get_random_word('a')
        self.my_publisher_1.publish(msg)
        
    def my_timer_callback_2(self):
        msg = String()
        msg.data = self.get_random_word('b')
        self.my_publisher_2.publish(msg)
        
    def my_listener_callback(self, msg):
        self.get_logger().info(f"I heard: {msg.data}")
        
    def get_random_word(self, letter):
        random_word = self.random_word_generator.word(starts_with=letter)
        return random_word
        
        
def main():
    rclpy.init()
    two_talk_one_listen = TwoTalkOneListen()
    rclpy.spin(two_talk_one_listen)
    two_talk_one_listen.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()