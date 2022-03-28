import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from morai_msgs.msg import IntersectionControl

# Test Map : Surburb 03
class PubInsnControl(Node):
  def __init__(self):
    super().__init__("InsnControl")
    self.publisher_ = self.create_publisher(IntersectionControl, '/InsnControl', 10)
    timer_period = 1
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
  
  def timer_callback(self):
    msg = IntersectionControl()
    msg.header = Header()
    msg.intersection_index = 20
    msg.intersection_status = 1
    msg.intersection_status_time = 10.0
    self.publisher_.publish(msg)
    self.get_logger().info(f'Publishing {self.i} times : {msg}')
    self.i += 1

def main(args=None):
  rclpy.init(args=args)

  publisher = PubInsnControl()
  try:
    rclpy.spin(publisher)
  except KeyboardInterrupt:
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()




