from collective.microsite.browser.interfaces import ICollectiveMicrositeLayer
from collective.microsite.interfaces import IMicroSite
from five import grok


grok.templatedir('templates')


class MicroSiteView(grok.View):
    """View class for content type: collective.microsite.MicroSite"""
    grok.context(IMicroSite)
    grok.layer(ICollectiveMicrositeLayer)
    grok.name('view')
    grok.require('zope2.View')
    grok.template('microsite')

    def title(self):
        return self.context.Title()

    def description(self):
        return self.context.Description()
