from setuptools import setup

package_name = 'ros2_examples'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shpark',
    maintainer_email='shpark@morai.ai',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Publishers
            'pub_ctrl_cmd = ros2_examples.publishers.pub_ctrl_cmd:main',
            'pub_ghost_msg = ros2_examples.publishers.pub_ghost_msg:main',
            'pub_ego_setting = ros2_examples.publishers.pub_multi_ego_setting:main',
            'pub_set_traffic_light = ros2_examples.publishers.pub_set_traffic_light:main',
            'pub_insn_control = ros2_examples.publishers.pub_insn_control:main',
            'pub_turn_signal_lamps = ros2_examples.publishers.pub_turn_signal_lamps:main',
            'pub_sensor_pos_control = ros2_examples.publishers.pub_sensor_pos_control:main',
            'pub_scenario_load = ros2_examples.publishers.pub_scenario_load:main',
            'pub_save_sensor_data = ros2_examples.publishers.pub_save_sensor_data:main',
            'pub_aa_vehicle_state_cmd = ros2_examples.publishers.vehicle_state_cmd:main',
            'pub_aa_vehicle_ctrl_cmd = ros2_examples.publishers.vehicle_ctrl_cmd:main',
            # Subscribers
            'sub_ego_vehicle_status = ros2_examples.subscribers.ego_vehicle_status:main',
            'sub_vehicle_collision_data = ros2_examples.subscribers.vehicle_collision_data:main',
            'sub_object_info = ros2_examples.subscribers.object_info:main',
            'sub_collision_data = ros2_examples.subscribers.collision_data:main',
            'sub_get_traffic_light_status = ros2_examples.subscribers.get_traffic_light_status:main',
            'sub_get_intersection_status = ros2_examples.subscribers.get_intersection_status:main',
            'sub_replay_info = ros2_examples.subscribers.replay_info:main',
            'sub_sim_proc_status = ros2_examples.subscribers.sim_proc_status:main',
            'sub_get_gps = ros2_examples.subscribers.get_gps:main',
            'sub_get_imu = ros2_examples.subscribers.get_imu:main',
            'sub_get_image = ros2_examples.subscribers.get_image_jpeg:main',

            'sub_aa_vehicle_odometry = ros2_examples.subscribers.vehicle_odometry:main',
            'sub_aa_vehicle_kinematic_state = ros2_examples.subscribers.vehicle_kinematic_state:main',
            'sub_aa_vehicle_state_report = ros2_examples.subscribers.vehicle_state_report:main',
            # Service clients
            'cli_event_cmd = ros2_examples.clients.cli_event_cmd:main',
            'cli_vehicle_spec = ros2_examples.clients.cli_vehicle_spec:main',
            'cli_tl_info = ros2_examples.clients.cli_tl_info:main',
            'cli_sim_proc = ros2_examples.clients.cli_sim_proc:main',
            'cli_map_spec = ros2_examples.clients.cli_map_spec:main',
            'cli_scenario_load = ros2_examples.clients.cli_scenario_load:main'
        ],
    },
)
