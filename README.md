# Autonomous Navigation Package Using TURTLEBOT3 for ROS2

This package provides a simple way to control a turtlebot3 mobile robot's navigation in ROS2 using the `nav2_simple_commander` library.

## Dependencies

- ROS2 Foxy or later
- Nav2Stack
- geometry_msgs
- tf_transformations

## Installation

1. Make sure you have ROS2 installed. Follow the instructions [here](https://docs.ros.org/en/humble/Installation.html).

2. Clone this repository into your ROS2 workspace:

    ```bash
    cd ~/ros2_ws/src
    git clone https://github.com/zakariabs/auto_pkg.git
    ```

3. Build the package:

    ```bash
    cd ~/ros2_ws
    colcon build --packages-select auto_pkg
    ```

4. Source the setup script:

    ```bash
    source ~/ros2_ws/install/setup.bash
    ```

## Usage

To run the `auto.py` script, use the following command:

```bash
ros2 run auto_pkg auto.py
```

To launch the package using the provided launch file, use:

```bash
ros2 launch auto_pkg auto_pkg_launch_file.launch.py
```

## Modes

The `auto.py` script in this package supports two modes:

### Static Mode

In this mode, the robot follows predefined waypoints. To set static waypoints, modify the script where static ranges are defined:

```python
# static ranges
goal_pose1 = create_pose_stamped(rc, 2.5, 1.0, 1.75)
goal_pose2 = create_pose_stamped(rc, -2.0, 2.0, 1.75)
goal_pose3 = create_pose_stamped(rc, -1.979794, -0.499868, 0.0)
```

Adjust these poses based on your desired static waypoints.

### Random Mode

In this mode, the robot navigates randomly generated waypoints. To set random waypoints, modify the script where random ranges are defined:

```python
# random ranges
num_coords = 20
random_coords = []

for _ in range(num_coords):
    random_x = r.uniform(-6.0, 6.0)
    random_y = r.uniform(-11.0, 11.0)
    random_pose = create_pose_stamped(rc, random_x, random_y, 1.75)
    random_coords.append(random_pose)
```

Customize the parameters within the loop to generate random waypoints as needed.

After setting waypoints, choose either the static or random mode and follow it with:

```python
rc.followWaypoints(waypoints_list)  # Uncomment the appropriate line for static coords
# rc.followWaypoints(random_coords) # Uncomment the appeopeiate line for random ranges
```

Choose either the static or random mode based on your navigation requirements.

## License

This package is licensed under the [Apache-2.0](LICENSE).
```
