import sys
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import tf_transformations

# ... (other necessary imports)

def create_pose_stamped(navigator, position_x, position_y, orientation_z):
    
    q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, orientation_z)
    pose = PoseStamped()  # Indent this line one level further
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


def main():
    rclpy.init()

    rc = BasicNavigator()

    while True:
        try:
            # Get coordinates from the terminal
            x_str = input("Enter x coordinate (or 'stop' to quit): ")
            if x_str.lower() == "stop":
                break
            x = float(x_str)
            y_str = input("Enter y coordinate: ")
            y = float(y_str)

            # Create PoseStamped message
            pose = create_pose_stamped(rc, x, y, 0.0)  # Assuming 0.0 for orientation_z

            # ... (navigate to the pose using your navigation library)

        except ValueError:
            print("Invalid input. Please enter numerical coordinates or 'stop'.")

    rclpy.shutdown()

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
