from typing import Optional
from rclpy.waitable import Waitable
from rostron_interfaces.msg import Robots, Ball, Referee, Field
from rclpy.node import Node
# from rclpy.subscription import Subscription
from .decorators import singleton

@singleton
class World():
    node_: Node = None

    receive_once = [False]

    field : Optional[Field] = None
    field_changed : bool = False

    def init(self, node: Node) -> None:
        self.node_ = node

        node.create_subscription(Field, 'field', self.field_callback)

    
    def field_callback(self, msg: Field) -> None:
        if self.field != msg:
            self.receive_once[0] = True
            self.field = msg
            self.field_changed = True    

class WorldWaitable(Waitable):
    def is_ready(self, _):
        ready = True

        for receive in World().receive_once:
            if not(receive):
                ready = False
        return ready
