import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from morai_msgs.msg import Lamps

class PubLamps(Node):
  def __init__(self):
    super().__init__("Lamps")
    self.publisher_ = self.create_publisher(Lamps, '/lamps', 10)
    timer_period = 1
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
  
  def timer_callback(self):
    msg = Lamps()
    msg.header = Header()
    msg.turn_signal = 2
    msg.emergency_signal = 0
    self.publisher_.publish(msg)
    self.get_logger().info(f'Publishing {self.i} times : {msg}')
    self.i += 1

def main(args=None):
  rclpy.init(args=args)

  publisher = PubLamps()
  try:
    rclpy.spin(publisher)
  except KeyboardInterrupt:
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()




