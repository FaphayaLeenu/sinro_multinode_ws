import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class LidarNode(Node):
    def __init__(self):
        super().__init__('lidar_sensor')
        self.pub = self.create_publisher(Float32, '/distance', 10)
        self.timer = self.create_timer(1.5, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = random.uniform(0.5, 5.0) # Random distance between 0.5m and 5.0m
        self.pub.publish(msg)
        self.get_logger().info(f"Obstacle at: {msg.data:.1f} meters")

def main():
    rclpy.init()
    node = LidarNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__': main()
