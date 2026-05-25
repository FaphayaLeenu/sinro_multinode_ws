import rclpy, random
from rclpy.node import Node
from std_msgs.msg import Float32

class TempNode(Node):
    def __init__(self):
        super().__init__('temp_sensor')
        self.pub = self.create_publisher(Float32, '/climate/temp', 10)
        self.create_timer(2.0, self.timer_cb)

    def timer_cb(self):
        msg = Float32()
        msg.data = random.uniform(20.0, 40.0)
        self.pub.publish(msg)
        self.get_logger().info(f"Publishing Temp: {msg.data:.2f}")

def main():
    rclpy.init()
    node = TempNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
