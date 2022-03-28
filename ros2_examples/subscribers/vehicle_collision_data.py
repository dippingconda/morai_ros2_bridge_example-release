import rclpy
from rclpy.node import Node

from morai_msgs.msg import VehicleCollisionData

class SubVehicleCollisionData(Node):
  def __init__(self):
    super().__init__("VehicleCollisionData")
    self.subscription = self.create_subscription(VehicleCollisionData, "/VehicleCollisionData", self.callback, 10)
    self.subscription
  
  def callback(self, msg):
    print(f'[Subscription] VehicleCollisionData : {msg}')

def main(args=None):
  rclpy.init(args=args)
  subscriber = SubVehicleCollisionData()
  rclpy.spin(subscriber)
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
