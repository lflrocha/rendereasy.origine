from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.origine import origineMessageFactory as _



class IVinheta(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    video = schema.Bytes(
        title=_(u"Video"),
        required=False,
        description=_(u"Field description"),
    )
#
