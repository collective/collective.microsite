from plone.dexterity.interfaces import IDexterityContainer
from plone.app.layout.navigation.interfaces import INavigationRoot


class IMicroSite(IDexterityContainer, INavigationRoot):
    """Interface for content type: collective.microsite.MicroSite"""
