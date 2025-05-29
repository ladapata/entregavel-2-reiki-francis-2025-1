import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64 # esse tópico é atualizado a cada 0,5s


class temperature_avg_monitor(Node):

  def __init__(self):
    super().__init__('temperature_avg_monitor')
    self.subscription = self.create_subscription(Float64, 'average_temperature', self.listener_callback, 10)
    self.subscription

  def listener_callback(self, msg):
    self.get_logger().info('A temperatura média é de "%f" graus Célsius.' %msg.data)


def main(args=None):
  rclpy.init(args=args)

  node = temperature_avg_monitor()
  rclpy.spin(node)
  node.detroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()
