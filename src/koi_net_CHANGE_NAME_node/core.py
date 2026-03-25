from koi_net.core import FullNode
from .config import MyNodeConfig
from .custom_handler import CustomHandler


class MyNode(FullNode):
    config_schema = MyNodeConfig
    custom_handler = CustomHandler