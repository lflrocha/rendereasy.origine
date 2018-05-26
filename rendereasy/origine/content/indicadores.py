# -*- coding: utf-8 -*-
"""Definition of the Indicadores content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from rendereasy.origine.interfaces import IIndicadores
from rendereasy.origine.config import PROJECTNAME

IndicadoresSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

IndicadoresSchema['title'].storage = atapi.AnnotationStorage()
IndicadoresSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(IndicadoresSchema, moveDiscussion=False)


class Indicadores(base.ATCTContent):
    """Description of the Example Type"""
    implements(IIndicadores)

    meta_type = "Indicadores"
    schema = IndicadoresSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Indicadores, PROJECTNAME)
