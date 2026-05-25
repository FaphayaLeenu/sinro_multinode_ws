import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class BrainNode(Node):

    def __init__(self):
        super().__init__('climate_brain')

        # Declare parameters
        self.declare_parameter('temp_threshold', 35.0)
        self.declare_parameter('hum_threshold', 40.0)

        # Subscribers
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

        # Publisher
        self.pub = self.create_publisher(
            String,
            '/sprinkler_cmd',
            10
        )

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

        # Read live parameter values
        target_temp = self.get_parameter(
            'temp_threshold'
        ).value

        target_hum = self.get_parameter(
            'hum_threshold'
        ).value

        # Logic
        if self.current_temp > target_temp or self.current_hum < target_hum:

            cmd.data = "ON"

            self.get_logger().warn(
                f"Threshold breached! "
                f"(Target Temp: {target_temp})"
            )

        else:
            cmd.data = "OFF"

        self.pub.publish(cmd)

def main():

    rclpy.init()

    node = BrainNode()

    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
