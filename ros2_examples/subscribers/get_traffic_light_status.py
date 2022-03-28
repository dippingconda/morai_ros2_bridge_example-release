import rclpy
from rclpy.node import Node

from morai_msgs.msg import GetTrafficLightStatus

class SubGetTrafficLightStatus(Node):
  def __init__(self):
    super().__init__("GetTrafficLightStatus")
    self.subscription = self.create_subscription(GetTrafficLightStatus, "/GetTrafficLightStatus", self.callback, 10)
  
  def callback(self, msg):
    print(f'[Subscription] GetTrafficLightStatus : {msg}')

def main(args=None):
  rclpy.init(args=args)
  subscriber = SubGetTrafficLightStatus()
  rclpy.spin(subscriber)
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
