import rclpy
from rclpy.node import Node
from morai_msgs.msg import SaveSensorData

class PubSaveSensorData(Node):
  def __init__(self):
    super().__init__("SaveSensorData")
    self.publisher_ = self.create_publisher(SaveSensorData, '/SaveSensorData', 10)
    timer_period = 1
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
  
  def timer_callback(self):
    msg = SaveSensorData()
    msg.is_custom_file_name = False
    self.publisher_.publish(msg)
    self.get_logger().info(f'Publishing {self.i} times : {msg}')
    self.i += 1

def main(args=None):
  rclpy.init(args=args)

  publisher = PubSaveSensorData()
  try:
    rclpy.spin(publisher)
  except KeyboardInterrupt:
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()




