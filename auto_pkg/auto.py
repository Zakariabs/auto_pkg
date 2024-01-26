import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import tf_transformations
#from setled import set_led_color
#from soundnode import play_sound


import random as r

def create_pose_stamped(navigator: BasicNavigator, position_x, position_y, orientation_z):
    q_x, q_y, q_z, q_w =  tf_transformations.quaternion_from_euler(0.0, 0.0, orientation_z)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg()
    pose.pose.position.x = position_x
    pose.pose.position.y = position_y
    pose.pose.position.z = 0.0

    pose.pose.orientation.x = q_x
    pose.pose.orientation.y = q_y
    pose.pose.orientation.z = q_z
    pose.pose.orientation.w = q_w
    
    return pose 



    publisher.publish(msg)

def main():

    rclpy.init()

    rc = BasicNavigator()
    
    #from rclpy.qos import QoSProfile, ReliabilityPolicy
    #from std_msgs.msg import String  # Replace with the actual message type

def main():
    """
    This is the main function that initializes the ROS2 node, creates a publisher, sets the initial pose,
    waits for Nav2 to become active, sends a goal to Nav2, and follows a list of waypoints.
    """
    rclpy.init()

    rc = BasicNavigator()


    # Rest of your code...
    #set initial pose 
    # tb3 gazebo x start position -1.979794
    # tb3 gazebo y start position = -0.499868
    initial_pose = create_pose_stamped(rc,0.0,0.0, 0.0 ) # tb3 world
    #initial_pose_warehouse = create_pose_stamped(rc,-1.998979, -0.500080, 0.0 ) #aws_warehouse 
    #initial_pose_house = create_pose_stamped(rc, -0.5, 1.3, 0.0)
    rc.setInitialPose(initial_pose)
    # --- Wait for Nav2
    rc.waitUntilNav2Active()

    # --- Send Nav2 goal

    # PI = 3.14 = 180° #
    # PI/2 = 1.57 = 90°#
        #############
    # static ranges
    goal_pose1 = create_pose_stamped(rc, 2.5, 1.0, 1.75)
    goal_pose2 = create_pose_stamped(rc, -2.0, 2.0, 1.75)
    goal_pose3 = create_pose_stamped(rc, -1.979794,-0.499868, 0.0)

    # random ranges
    num_coords = 20
    random_coords = []

    # generate random coordinates
    for _ in range(num_coords):
        random_x = r.uniform(-6.0, 6.0)
        random_y = r.uniform(-11.0, 11.0)
        random_pose = create_pose_stamped(rc, random_x, random_y, 1.75)
        random_coords.append(random_pose)
    

    # ---- navigating through a multiple points. 
    wayppoints_list = [goal_pose1, goal_pose2, goal_pose3]

    rc.followWaypoints(wayppoints_list) 
    #rc.followWaypoints(random_coords)  # uncomment this to navigate through random coordinates
    while not rc.isTaskComplete():
        feedback = rc.getFeedback()
        #print(feedback)
        rc.get_logger().warning(str(feedback))
        
    


    print(rc.getResult())
    rclpy.shutdown()


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
