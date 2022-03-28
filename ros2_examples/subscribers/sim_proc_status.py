import rclpy
from rclpy.node import Node

from morai_msgs.msg import MoraiSimProcStatus

class SubMoraiSimProcStatus(Node):
  def __init__(self):
    super().__init__("MoraiSimProcStatus")
    self.subscription = self.create_subscription(MoraiSimProcStatus, "/sim/process/state/msg/MoraiSimProcStatus", self.callback, 10)
    self.subscription
  
  def callback(self, msg):
    print(f'[Subscription] MoraiSimProcStatus : {msg}')

def main(args=None):
  rclpy.init(args=args)
  subscriber = SubMoraiSimProcStatus()
  rclpy.spin(subscriber)
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
