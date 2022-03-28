import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from morai_msgs.msg import SensorPosControl

class PubSensorPosControl(Node):
  def __init__(self):
    super().__init__("SensorPosControl")
    self.publisher_ = self.create_publisher(SensorPosControl, '/SensorPosControl', 10)
    timer_period = 1
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
  
  def timer_callback(self):
    msg = SensorPosControl()
    msg.sensor_index.append(1)
    msg.pose_x.append(1.50)
    msg.pose_y.append(-0.02)
    msg.pose_z.append(2.20)
    msg.roll.append(0.0)
    msg.pitch.append(0.0)
    msg.yaw.append(0.0)
    self.publisher_.publish(msg)
    self.get_logger().info(f'Publishing {self.i} times : {msg}')
    self.i += 1

def main(args=None):
  rclpy.init(args=args)

  publisher = PubSensorPosControl()
  try:
    rclpy.spin(publisher)
  except KeyboardInterrupt:
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()




