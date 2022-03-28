import rclpy
from rclpy.node import Node

from autoware_auto_msgs.msg import VehicleControlCommand

class PubVehicleControlCommand(Node):
  def __init__(self):
    super().__init__("VehicleControlCommand")
    self.publisher_ = self.create_publisher(VehicleControlCommand, '/autoware_auto_msgs/VehicleControlCommand', 10)
    timer_period = 1
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
  
  def timer_callback(self):
    msg = VehicleControlCommand()
    msg.velocity_mps = 100.0
    msg.long_accel_mps2 = 10.0
    msg.front_wheel_angle_rad = 0.0


    self.publisher_.publish(msg)
    self.get_logger().info(f'Publishing {self.i} times : {msg}')
    self.i += 1

def main(args=None):
  rclpy.init(args=args)

  publisher = PubVehicleControlCommand()
  try:
    rclpy.spin(publisher)
  except KeyboardInterrupt:
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()




