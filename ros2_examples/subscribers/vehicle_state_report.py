import rclpy
from rclpy.node import Node

from autoware_auto_msgs.msg import VehicleStateReport

class SubVehicleStateReport(Node):
  def __init__(self):
    super().__init__("VehicleStateReport")
    self.subscription = self.create_subscription(VehicleStateReport, "/autoware_auto_msgs/VehicleStateReport", self.callback, 10)
    self.subscription
  
  def callback(self, msg):
    print(f'[Subscription] VehicleStateReport : {msg}')

def main(args=None):
  rclpy.init(args=args)
  subscriber = SubVehicleStateReport()
  rclpy.spin(subscriber)
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
