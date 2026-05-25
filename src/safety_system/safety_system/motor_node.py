import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MotorDriverNode(Node):
    def __init__(self):
        super().__init__('motor_driver')
        self.sub = self.create_subscription(Twist, '/cmd_vel', self.cmd_callback, 10)

    def cmd_callback(self, msg):
        speed = msg.linear.x
        if speed == 0.0:
            self.get_logger().error("*** MOTORS BRAKING - EMERGENCY STOP ***")
        else:
            self.get_logger().info(f"Motors spinning at {speed} m/s")

def main():
    rclpy.init()
    node = MotorDriverNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__': main()
