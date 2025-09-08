import logging
from koi_net.processor.handler import HandlerType
from koi_net.processor.knowledge_object import KnowledgeObject
from koi_net.context import HandlerContext
from .core import node

logger = logging.getLogger(__name__)

"""
@node.pipeline.register_handler(
    handler_type=HandlerType.RID,
    rid_types=[]
)
def my_handler(ctx: HandlerContext, kobj: KnowledgeObject):
    ...
"""
