import rclpy
from rclpy.node import Node
import numpy as np

from sensor_msgs.msg import CompressedImage

class SubCompressedImage(Node):
  def __init__(self):
    super().__init__("CompressedImage")
    self.subscription = self.create_subscription(CompressedImage, "/image_jpeg/compressed", self.callback, 10)
  
  def callback(self, msg):
    print(f'[Subscription] imag_jpeg : {msg}')

def main(args=None):
  rclpy.init(args=args)
  subscriber = SubCompressedImage()
  rclpy.spin_once(subscriber)
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
