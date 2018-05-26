from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.origine import origineMessageFactory as _



class IColuna(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    foto = schema.Bytes(
        title=_(u"Foto"),
        required=True,
        description=_(u"Field description"),
    )
#
    autor = schema.TextLine(
        title=_(u"Autor"),
        required=True,
        description=_(u"Field description"),
    )
#
