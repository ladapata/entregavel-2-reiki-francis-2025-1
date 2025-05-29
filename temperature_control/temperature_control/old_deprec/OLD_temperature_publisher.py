import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64 # esse tópico é atualizado a cada 0,5s

import math
import random

random_number = random.randint(80, 100)
temperature = 25.0 + 5.0 * math.sin(random_number / 10.0)

class temperature_publisher(Node):
  def __init__(self):
    super.__init__('temperature_publisher')
    self.publisher_ = self.create_publisher(Float64, 'temperature', 10)
    # não sei oq botar no 'queue size', então vou botar 10 mesmo, como diz o tutorial do ROS2
    
    timer_period = 0.5 # 0,5s = 2Hz

    self.timer = self.create_timer(timer_period, self.timer_callback)

  def timer_callback(self):
    msg = Float64()
    msg.data = temperature
    self.publisher_.publish(msg)


def main(args=None):
  rclpy.init(args=args)

  temperature_publisher = temperature_publisher()

  rclpy.spin(temperature_publisher)


if __name__ == '__main__':
  main()
