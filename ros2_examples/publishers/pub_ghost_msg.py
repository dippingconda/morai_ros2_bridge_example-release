import rclpy
from rclpy.node import Node

from morai_msgs.msg import GhostMessage

class TestPublisher(Node):
  def __init__(self):
    super().__init__("GhostMessage")
    self.publisher_ = self.create_publisher(GhostMessage, '/ghost_ctrl_cmd', 10)
    timer_period = 1
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
  
  def timer_callback(self):
    msg = GhostMessage()
    msg.position.x = -939.0759887695312
    msg.position.y =-4.433000087738037 
    msg.position.z = 6.327000141143799
    msg.rotation.x = 0.0
    msg.rotation.y = 0.0
    msg.rotation.z = 0.0
    msg.velocity = 10.0
    msg.steering_angle = -1.0
    self.publisher_.publish(msg)
    self.get_logger().info(f'Publishing {self.i} times : {msg}')
    self.i += 1

def main(args=None):
  rclpy.init(args=args)

  test_publisher = TestPublisher()
  try:
    rclpy.spin(test_publisher)
  except KeyboardInterrupt:
    test_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()




