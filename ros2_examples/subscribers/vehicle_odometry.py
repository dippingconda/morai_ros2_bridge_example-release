import rclpy
from rclpy.node import Node

from autoware_auto_msgs.msg import VehicleOdometry

class SubVehicleOdometry(Node):
  def __init__(self):
    super().__init__("VehicleOdometry")
    self.subscription = self.create_subscription(VehicleOdometry, "/autoware_auto_msgs/VehicleOdometry", self.callback, 10)
    self.subscription
  
  def callback(self, msg):
    print(f'[Subscription] VehicleOdometry : {msg}')

def main(args=None):
  rclpy.init(args=args)
  subscriber = SubVehicleOdometry()
  rclpy.spin(subscriber)
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
