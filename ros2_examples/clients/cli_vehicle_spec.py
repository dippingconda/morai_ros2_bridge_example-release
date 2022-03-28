import rclpy
from morai_msgs.srv import MoraiVehicleSpecSrv
from rclpy import node

def main(args=None):
  rclpy.init(args=args)

  node = rclpy.create_node('MoraiVehicleSpecSrv')
  client = node.create_client(MoraiVehicleSpecSrv, 'morai_msgs/MoraiVehicleSpecSrv')

  srv_def = MoraiVehicleSpecSrv.Request()
  srv_def.request.unique_id = 0

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
          f'Result of MoraiVehicleSpecSrv : {result}')
      
      break
  node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
