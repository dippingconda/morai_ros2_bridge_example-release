import rclpy
from morai_msgs.srv import MoraiScenarioLoadSrv
from rclpy import node

def main(args=None):
  rclpy.init(args=args)

  node = rclpy.create_node('MoraiScenarioLoadSrv')
  client = node.create_client(MoraiScenarioLoadSrv, 'morai_msgs/MoraiScenarioLoadSrv')

  srv_def = MoraiScenarioLoadSrv.Request()
  srv_def.request.file_name = "1"
  srv_def.request.delete_all = False
  srv_def.request.load_network_connection_data = False
  srv_def.request.load_ego_vehicle_data = False
  srv_def.request.load_surrounding_vehicle_data = True
  srv_def.request.load_pedestrian_data = False
  srv_def.request.load_obstacle_data = False
  srv_def.request.set_pause = False

  while not client.wait_for_service(timeout_sec=10.0):
    node.get_logger().info('service not available, waiting again...')
  
  node.get_logger().info(f'{srv_def}')
  future = client.call_async(srv_def)
  while rclpy.ok():
    rclpy.spin_once(node)
    if future.done():
      try:
        result = future.result()
      except Exception as e:
        node.get_logger().info('Service call failed %r' %(e,))
      else:
        node.get_logger().info(
          f'Result of MoraiScenarioLoadSrv : {result}')
      
      break
  node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
