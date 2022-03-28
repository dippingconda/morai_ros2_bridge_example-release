import rclpy
from morai_msgs.srv import MoraiSimProcSrv
from rclpy import node

def main(args=None):
  rclpy.init(args=args)

  node = rclpy.create_node('MoraiSimProcSrv')
  client = node.create_client(MoraiSimProcSrv, 'morai_msgs/MoraiSimProcSrv')

  srv_def = MoraiSimProcSrv.Request()
  srv_def.request.sim_process_status = 1
  srv_def.request.replay_option = 1
  srv_def.request.rosbag_file_name = ""
  srv_def.request.replay_target_option = 1
  srv_def.request.replay_speed = 1
  srv_def.request.start_time = 0

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
          f'Result of MoraiSimProcSrv : {result}')
      
      break
  node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
