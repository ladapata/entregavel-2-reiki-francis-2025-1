import rclpy
from rclpy.node import Node

from example_interfaces.srv import SetBool # esse serviço é atualizado aleatoriamente


class average_client_reset(Node):

  def __init__(self):
    super().__init__('average_client_reset')
    self.cli = self.create_client(SetBool, 'reset_average')

    while not self.cli.wait_for_service(timeout_sec=10.0):
      self.get_logger().info('pra um serviço demorado desses, tinha que ser Brasil...')

    self.req = SetBool.Request()


  def send_request(self, reseta):
    self.req.reseta = input
    return self.cli.call_async(self.rec)


def main():
  rclpy.init()

  node = average_client_reset()
  rclpy.spin(node)
  node.detroy_node()
  rclpy.shutdown()
  

if __name__ == '__main__':
  main()
