from typing import Optional
from rclpy.waitable import Waitable
from rostron_interfaces.msg import Robots, Ball, Referee, Field
from rclpy.node import Node
# from rclpy.subscription import Subscription
from .decorators import singleton


@singleton
class World():
    node_: Node = None

    # Mobile Data
    allies = []
    opponents = []

    ball : Optional[Ball] = None

    # Geometry Object
    field: Optional[Field] = None

    def init(self, node: Node) -> None:
        self.node_ = node
        # Geometry Object
        node.create_subscription(Field, 'field', self.field_callback, 10)

        # Mobile
        node.create_subscription(Robots, 'allies', self.allies_callback, 10)
        node.create_subscription(
            Robots, 'opponents', self.opponents_callback, 10)

        node.create_subscription(Ball, 'ball', self.ball_callback, 10)

    def field_callback(self, msg: Field) -> None:
        if self.field != msg:
            self.field = msg

    def allies_callback(self, msg: Robots) -> None:
        self.allies = msg.robots

    def opponents_callback(self, msg: Robots) -> None:
        self.opponents = msg.robots

    def ball_callback(self, msg: Ball) -> None:
        self.ball = msg
