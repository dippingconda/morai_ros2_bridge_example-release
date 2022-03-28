import rclpy
from rclpy.node import Node

from morai_msgs.msg import GPSMessage

class SubGPSMessage(Node):
  def __init__(self):
    super().__init__("GPSMessage")
    self.subscription = self.create_subscription(GPSMessage, "/gps", self.callback, 10)
  
  def callback(self, msg):
    print(f'[Subscription] GPSMessage : {msg}')

def main(args=None):
  rclpy.init(args=args)
  subscriber = SubGPSMessage()
  rclpy.spin(subscriber)
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
