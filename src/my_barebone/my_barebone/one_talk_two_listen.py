from wonderwords import RandomWord

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class OneTalkTwoListen(Node):
    def __init__(self):
        super().__init__('one_talk_two_listen')
        
        #! Publisher
        self.my_publisher = self.create_publisher(String, '/random_word_c', 10)
        self.my_timer = self.create_timer(2, self.my_timer_callback)
        
        #! Subscriber 1
        self.my_subscriber_1 = self.create_subscription(
            String, '/random_word_a', self.my_listener_callback_1, 10
        )
       
        #! Subscriber 2 
        self.my_subscriber_2 = self.create_subscription(
            String, '/random_word_b', self.my_listener_callback_2, 10
        )
        
        #! Random word generator
        self.random_word_generator = RandomWord()
       
        #! Node Start Log 
        self.get_logger().info("I talk random words starting from 'c'@2Hz, and listen to random words starting from 'a' and 'b'")
        
        
    def my_timer_callback(self):
        msg = String()
        msg.data = self.get_random_word('c')
        self.my_publisher.publish(msg)
        
    def my_listener_callback_1(self, msg):
        self.get_logger().info(f"I heard from 1: {msg.data}")
        
    def my_listener_callback_2(self, msg):
        self.get_logger().info(f"I heard from 2: {msg.data}")
        
    def get_random_word(self, letter):
        random_word = self.random_word_generator.word(starts_with=letter)
        return random_word
        
        
def main():
    rclpy.init()
    one_talk_two_listen = OneTalkTwoListen()
    rclpy.spin(one_talk_two_listen)
    one_talk_two_listen.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()