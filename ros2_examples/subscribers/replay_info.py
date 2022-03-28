import rclpy
from rclpy.node import Node

from morai_msgs.msg import ReplayInfo

class SubReplayInfo(Node):
  def __init__(self):
    super().__init__("ReplayInfo")
    self.subscription = self.create_subscription(ReplayInfo, "/ReplayInfo_topic", self.callback, 10)
    self.subscription
  
  def callback(self, msg):
    print(f'[Subscription] ReplayInfo : {msg}')

def main(args=None):
  rclpy.init(args=args)
  subscriber = SubReplayInfo()
  rclpy.spin(subscriber)
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
