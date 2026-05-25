import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SprinklerNode(Node):

    def __init__(self):
        super().__init__('sprinkler_actuator')

        self.create_subscription(
            String,
            '/sprinkler_cmd',
            self.cmd_cb,
            10
        )

    def cmd_cb(self, msg):

        if msg.data == "ON":
            self.get_logger().info(
                "💦 Sprinklers are SPRAYING WATER!"
            )

        else:
            self.get_logger().info(
                "Sprinklers are OFF."
            )

def main():
    rclpy.init()

    node = SprinklerNode()

    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
