import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import Float32

class HumNode(Node):

    def __init__(self):
        super().__init__('humidity_sensor')

        self.pub = self.create_publisher(
            Float32,
            '/climate/humidity',
            10
        )

        self.create_timer(2.0, self.timer_cb)

    def timer_cb(self):
        msg = Float32()

        msg.data = random.uniform(30.0, 90.0)

        self.pub.publish(msg)

        self.get_logger().info(
            f"Publishing Humidity: {msg.data:.2f}"
        )

def main():
    rclpy.init()

    node = HumNode()

    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
