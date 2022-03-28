import rclpy
from rclpy.node import Node

from morai_msgs.msg import ObjectStatusList

class SubObjectInfo(Node):
  def __init__(self):
    super().__init__("ObjectInfo")
    self.subscription = self.create_subscription(ObjectStatusList, "/Object_topic", self.callback, 10)
    self.subscription
  
  def callback(self, msg):
    print(f'[Subscription] ObjectInfo : {msg}')

def main(args=None):
  rclpy.init(args=args)
  subscriber = SubObjectInfo()
  rclpy.spin(subscriber)
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
