from koi_net.core import FullNode
from .config import MyNodeConfig
from .handlers import MyKnowledgeHandler


class MyNode(FullNode):
    config_schema = MyNodeConfig
    my_knowledge_handler = MyKnowledgeHandler