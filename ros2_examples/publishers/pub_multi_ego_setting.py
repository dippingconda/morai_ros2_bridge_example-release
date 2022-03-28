import rclpy
from rclpy.node import Node

from morai_msgs.msg import MultiEgoSetting

class PubMultiEgoSetting(Node):
  def __init__(self):
    super().__init__("MultiEgoSetting")
    self.publisher_ = self.create_publisher(MultiEgoSetting, '/ego_setting', 10)
    timer_period = 1
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
  
  def timer_callback(self):
    msg = MultiEgoSetting()
    msg.number_of_ego_vehicle = 1
    msg.camera_index = 2
    msg.ego_index.append(2)
    msg.global_position_x.append(-939.0759887695312)
    msg.global_position_y.append(-4.433000087738037)
    msg.global_position_z.append(6.327000141143799)
    msg.global_roll.append(0)
    msg.global_pitch.append(0)
    msg.global_yaw.append(0)
    msg.velocity.append(50)
    msg.gear.append(3)
    msg.ctrl_mode.append(16)
    self.publisher_.publish(msg)
    self.get_logger().info(f'Publishing {self.i} times : {msg}')
    self.i += 1

def main(args=None):
  rclpy.init(args=args)

  publisher = PubMultiEgoSetting()
  try:
    rclpy.spin(publisher)
  except KeyboardInterrupt:
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()




