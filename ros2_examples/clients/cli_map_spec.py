import rclpy
from morai_msgs.srv import MoraiMapSpecSrv
from rclpy import node

def main(args=None):
  rclpy.init(args=args)

  node = rclpy.create_node('MoraiMapSpecSrv')
  client = node.create_client(MoraiMapSpecSrv, 'morai_msgs/MoraiMapSpecSrv')

  srv_def = MoraiMapSpecSrv.Request()
  srv_def.request.load_map_data = True

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
          f'Result of MoraiMapSpecSrv : {result}')
      
      break
  node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
