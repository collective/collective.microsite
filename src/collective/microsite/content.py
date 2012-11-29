from collective.microsite.interfaces import IMicroSite
from plone.dexterity.content import Container
from zope.interface import implements


class MicroSite(Container):
    """Content class for MicroSite."""

    implements(IMicroSite)
