import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class BrainNode(Node):
    def __init__(self):
        super().__init__('climate_brain')

        self.create_subscription(
            Float32,
            '/climate/temp',
            self.temp_cb,
            10
        )

        self.create_subscription(
            Float32,
            '/climate/humidity',
            self.hum_cb,
            10
        )

        self.pub = self.create_publisher(String, '/sprinkler_cmd', 10)

        self.current_temp = 25.0
        self.current_hum = 50.0

    def temp_cb(self, msg):
        self.current_temp = msg.data
        self.check_climate()

    def hum_cb(self, msg):
        self.current_hum = msg.data
        self.check_climate()

    def check_climate(self):
        cmd = String()

        if self.current_temp > 35.0 or self.current_hum < 40.0:
            cmd.data = "ON"
        else:
            cmd.data = "OFF"

        self.pub.publish(cmd)

        self.get_logger().info(
            f"Temp={self.current_temp:.2f}, "
            f"Humidity={self.current_hum:.2f} "
            f"--> Sprinkler {cmd.data}"
        )

def main():
    rclpy.init()
    node = BrainNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
