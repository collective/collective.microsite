from Products.CMFCore.interfaces import IFolderish
from Products.Five.browser import BrowserView
from plone.app.layout.navigation.interfaces import INavigationRoot
from zope.interface import alsoProvides
from zope.interface import noLongerProvides


class Miscellaneous(BrowserView):
    """Miscellaneous"""

    def available_to_make_microsite(self):
        return IFolderish.providedBy(self.context) and not INavigationRoot.providedBy(self.context)

    def unavailable_to_make_microsite(self):
        return IFolderish.providedBy(self.context) and INavigationRoot.providedBy(self.context)

    def make_microsite(self):
        alsoProvides(self.context, INavigationRoot)
        self.context.reindexObject(idxs=['object_provides'])
        url = self.context.absolute_url()
        return self.request.response.redirect(url)

    def unmake_microsite(self):
        noLongerProvides(self.context, INavigationRoot)
        self.context.reindexObject(idxs=['object_provides'])
        url = self.context.absolute_url()
        return self.request.response.redirect(url)
