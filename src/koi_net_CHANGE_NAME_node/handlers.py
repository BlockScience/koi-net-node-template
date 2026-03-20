from dataclasses import dataclass
from logging import Logger

from koi_net.components.interfaces import KnowledgeHandler, HandlerType, STOP_CHAIN
from koi_net.protocol import KnowledgeObject


@dataclass
class MyKnowledgeHandler(KnowledgeHandler):
    log: Logger
    
    handler_type=HandlerType.RID
    rid_types=()
    
    def handle(self, kobj: KnowledgeObject):
        self.log.info(f"Handling {kobj.rid}")
