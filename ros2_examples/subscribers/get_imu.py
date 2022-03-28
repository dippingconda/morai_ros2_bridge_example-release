import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Imu

class SubImuMessage(Node):
  def __init__(self):
    super().__init__("ImuMessage")
    self.subscription = self.create_subscription(Imu, "/Imu", self.callback, 10)
  
  def callback(self, msg):
    print(f'[Subscription] IMU Message : {msg}')

def main(args=None):
  rclpy.init(args=args)
  subscriber = SubImuMessage()
  rclpy.spin(subscriber)
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
