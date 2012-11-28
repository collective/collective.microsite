from Products.CMFCore.utils import getToolByName
from collective.microsite.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_collective_microsite_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.microsite'))

    def test_actions__object_buttons__make_microsite__title(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'make_microsite')
        self.assertEqual(action.title, 'Make micro site')

    def test_actions__object_buttons__make_microsite__description(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'make_microsite')
        self.assertEqual(action.description, '')

    def test_actions__object_buttons__make_microsite__url_expr(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'make_microsite')
        self.assertEqual(action.url_expr, 'string:${globals_view/getCurrentObjectUrl}/@@make-microsite')

    def test_actions__object_buttons__make_microsite__permissions(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'make_microsite')
        self.assertEqual(action.permissions, ('collective.microsite: Manage micro site',))

    def test_actions__object_buttons__make_microsite__visible(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'make_microsite')
        self.assertTrue(action.visible)

    def test_actions__object_buttons__unmake_microsite__title(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unmake_microsite')
        self.assertEqual(action.title, 'Unmake micro site')

    def test_actions__object_buttons__unmake_microsite__description(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unmake_microsite')
        self.assertEqual(action.description, '')

    def test_actions__object_buttons__unmake_microsite__url_expr(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unmake_microsite')
        self.assertEqual(action.url_expr, 'string:${globals_view/getCurrentObjectUrl}/@@unmake-microsite')

    def test_actions__object_buttons__unmake_microsite__permissions(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unmake_microsite')
        self.assertEqual(action.permissions, ('collective.microsite: Manage micro site',))

    def test_actions__object_buttons__unmake_microsite__visible(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        action = getattr(object_buttons, 'unmake_microsite')
        self.assertTrue(action.visible)

    def test_browserlayer(self):
        from collective.microsite.browser.interfaces import ICollectiveMicrositeLayer
        from plone.browserlayer import utils
        self.failUnless(ICollectiveMicrositeLayer in utils.registered_layers())

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-collective.microsite:default'), u'0')

    def test_uninstall__actions__object_buttons__make_microsite(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.microsite'])
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        self.assertFalse(hasattr(object_buttons, 'make_microsite'))

    def test_uninstall__actions__object_buttons__unmake_microsite(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.microsite'])
        portal_actions = getToolByName(self.portal, 'portal_actions')
        object_buttons = getattr(portal_actions, 'object_buttons')
        self.assertFalse(hasattr(object_buttons, 'unmake_microsite'))

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.microsite'])
        self.failIf(installer.isProductInstalled('collective.microsite'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.microsite'])
        from collective.microsite.browser.interfaces import ICollectiveMicrositeLayer
        from plone.browserlayer import utils
        self.failIf(ICollectiveMicrositeLayer in utils.registered_layers())
