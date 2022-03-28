import rclpy
from rclpy.node import Node

from morai_msgs.msg import CollisionData

class SubCollisionData(Node):
  def __init__(self):
    super().__init__("CollisionData")
    self.subscription = self.create_subscription(CollisionData, "/CollisionData", self.callback, 10)
    self.subscription
  
  def callback(self, msg):
    print(f'[Subscription] CollisionData : {msg}')

def main(args=None):
  rclpy.init(args=args)
  subscriber = SubCollisionData()
  rclpy.spin(subscriber)
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
