import rclpy
from rclpy.node import Node

from autoware_auto_msgs.msg import VehicleKinematicState

class SubVehicleKinematicState(Node):
  def __init__(self):
    super().__init__("VehicleKinematicState")
    self.subscription = self.create_subscription(VehicleKinematicState, "/autoware_auto_msgs/VehicleKinematicState", self.callback, 10)
    self.subscription
  
  def callback(self, msg):
    print(f'[Subscription] VehicleKinematicState : {msg}')

def main(args=None):
  rclpy.init(args=args)
  subscriber = SubVehicleKinematicState()
  rclpy.spin(subscriber)
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
