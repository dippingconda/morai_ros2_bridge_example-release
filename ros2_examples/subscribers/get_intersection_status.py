import rclpy
from rclpy.node import Node

from morai_msgs.msg import IntersectionStatus

class SubIntersectionStatus(Node):
  def __init__(self):
    super().__init__("IntersectionStatus")
    self.subscription = self.create_subscription(IntersectionStatus, "/InsnStatus", self.callback, 10)
    self.subscription
  
  def callback(self, msg):
    print(f'[Subscription] IntersectionStatus : {msg}')

def main(args=None):
  rclpy.init(args=args)
  subscriber = SubIntersectionStatus()
  rclpy.spin(subscriber)
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
