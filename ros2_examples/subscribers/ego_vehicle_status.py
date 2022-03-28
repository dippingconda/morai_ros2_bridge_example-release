import rclpy
from rclpy.node import Node

from morai_msgs.msg import EgoVehicleStatus

class SubEgoVehicleStatus(Node):
  def __init__(self):
    super().__init__("EgoVehicleStatus")
    self.subscription = self.create_subscription(EgoVehicleStatus, "/Ego_topic", self.callback, 10)
    self.subscription
  
  def callback(self, msg):
    print(f'[Subscription] EgoVehicleStatus : {msg}')

def main(args=None):
  rclpy.init(args=args)
  subscriber = SubEgoVehicleStatus()
  rclpy.spin(subscriber)
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
