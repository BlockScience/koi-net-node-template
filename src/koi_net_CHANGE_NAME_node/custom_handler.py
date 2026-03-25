from dataclasses import dataclass
from logging import Logger

from koi_net.components.interfaces import KnowledgeHandler, HandlerType, STOP_CHAIN
from koi_net.protocol import KnowledgeObject


@dataclass
class CustomHandler(KnowledgeHandler):
    # add dependencies here:
    log: Logger
    
    handler_type=HandlerType.RID
    rid_types=()
    
    def handle(self, kobj: KnowledgeObject):
        # return nothing, a modified knowledge object, or STOP_CHAIN
        
        self.log.info(f"Handling {kobj.rid}")
