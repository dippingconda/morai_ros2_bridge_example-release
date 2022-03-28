import rclpy
from rclpy.node import Node

from autoware_auto_msgs.msg import VehicleStateCommand

class PubVehicleStateCommand(Node):
  def __init__(self):
    super().__init__("VehicleStateCommand")
    self.publisher_ = self.create_publisher(VehicleStateCommand, '/autoware_auto_msgs/VehicleStateCommand', 10)
    timer_period = 1
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
    self.blinker = {"Left":2, "Right":3, "Hazard":4}
    self.gear = {"P":1, "R":2, "N":3, "D":4}
  
  def timer_callback(self):
    msg = VehicleStateCommand()
    msg.gear = self.gear["D"]
    msg.blinker = self.blinker["Hazard"]


    self.publisher_.publish(msg)
    self.get_logger().info(f'Publishing {self.i} times : {msg}')
    self.i += 1

def main(args=None):
  rclpy.init(args=args)

  publisher = PubVehicleStateCommand()
  try:
    rclpy.spin(publisher)
  except KeyboardInterrupt:
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()




