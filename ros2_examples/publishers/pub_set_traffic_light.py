import rclpy
from rclpy.node import Node

from morai_msgs.msg import SetTrafficLight

# Test Map : Surburb 03
class PubSetTrafficLight(Node):
  def __init__(self):
    super().__init__("SetTrafficLight")
    self.publisher_ = self.create_publisher(SetTrafficLight, '/SetTrafficLight', 10)
    timer_period = 1
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
  
  def timer_callback(self):
    msg = SetTrafficLight()
    msg.traffic_light_index = '637'
    msg.traffic_light_status = 1
    self.publisher_.publish(msg)
    self.get_logger().info(f'Publishing {self.i} times : {msg}')
    self.i += 1

def main(args=None):
  rclpy.init(args=args)

  publisher = PubSetTrafficLight()
  try:
    rclpy.spin(publisher)
  except KeyboardInterrupt:
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()




