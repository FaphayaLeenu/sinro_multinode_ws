import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

class ControllerNode(Node):
    def __init__(self):
        super().__init__('safety_controller')
        # Subscriber
        self.sub = self.create_subscription(Float32, '/distance', self.dist_callback, 10)
        # Publisher
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def dist_callback(self, msg):
        cmd = Twist()
        if msg.data < 2.0:
            cmd.linear.x = 0.0 # STOP!
            self.get_logger().warn("Obstacle close! Sending STOP command.")
        else:
            cmd.linear.x = 5.0 # Drive forward
            self.get_logger().info("Path clear. Sending DRIVE command.")
        self.pub.publish(cmd)

def main():
    rclpy.init()
    node = ControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__': main()
