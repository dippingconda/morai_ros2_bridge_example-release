import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from morai_msgs.msg import ScenarioLoad

# Test map : V_RHT_HighwayJunction_1
class PubScenarioLoad(Node):
  def __init__(self):
    super().__init__("ScenarioLoad")
    self.publisher_ = self.create_publisher(ScenarioLoad, '/ScenarioLoad', 10)
    timer_period = 1
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
  
  def timer_callback(self):
    msg = ScenarioLoad()
    msg.file_name = "1"
    msg.delete_all = False
    msg.load_network_connection_data = False
    msg.load_ego_vehicle_data = False
    msg.load_surrounding_vehicle_data = True
    msg.load_pedestrian_data = False
    msg.load_obstacle_data = False
    msg.set_pause = False
    self.publisher_.publish(msg)
    self.get_logger().info(f'Publishing {self.i} times : {msg}')
    self.i += 1

def main(args=None):
  rclpy.init(args=args)

  publisher = PubScenarioLoad()
  try:
    rclpy.spin(publisher)
  except KeyboardInterrupt:
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()




