import rclpy
from rclpy.node import Node

from morai_msgs.msg import CtrlCmd

class PubCtrlCmd(Node):
  def __init__(self):
    super().__init__("CtrlCmd")
    self.publisher_ = self.create_publisher(CtrlCmd, '/ctrl_cmd', 10)
    timer_period = 1
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
  
  def timer_callback(self):
    msg = CtrlCmd()
    msg.longl_cmd_type = 1
    msg.accel = 0.5
    msg.brake = 0.0
    msg.steering = 3.14 / 2
    msg.velocity = 0.0
    msg.acceleration = 0.0
    self.publisher_.publish(msg)
    self.get_logger().info(f'Publishing {self.i} times : {msg}')
    self.i += 1

def main(args=None):
  rclpy.init(args=args)

  publisher = PubCtrlCmd()
  try:
    rclpy.spin(publisher)
  except KeyboardInterrupt:
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()




