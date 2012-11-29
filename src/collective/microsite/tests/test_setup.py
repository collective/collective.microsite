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

    def test_rolemap__collective_microsite_Manage_micro_site__rolesOfPermission(self):
        permission = "collective.microsite: Manage micro site"
        roles = [item['name'] for item in self.portal.rolesOfPermission(permission) if item['selected'] == 'SELECTED']
        roles.sort()
        self.assertEqual(roles, [
            'Manager',
            'Site Administrator'])

    def test_rolemap__collective_microsite_Manage_micro_site__acquiredRolesAreUsedBy(self):
        permission = "collective.microsite: Manage micro site"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission), '')

    def get_ctype(self, name):
        return getToolByName(self.portal, 'portal_types').getTypeInfo(name)

    def test_types__collective_microsite_MicroSite__i18n_domain(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertEqual(ctype.i18n_domain, 'collective.microsite')

    def test_types__collective_microsite_MicroSite__meta_type(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertEqual(ctype.meta_type, 'Dexterity FTI')

    def test_types__collective_microsite_MicroSite__title(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertEqual(ctype.title, 'MicroSite')

    def test_types__collective_microsite_MicroSite__description(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertEqual(ctype.description, '')

    def test_types__collective_microsite_MicroSite__content_icon(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertEqual(ctype.getIcon(), '')

    def test_types__collective_microsite_MicroSite__allow_discussion(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertFalse(ctype.allow_discussion)

    def test_types__collective_microsite_MicroSite__global_allow(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertTrue(ctype.global_allow)

    def test_types__collective_microsite_MicroSite__filter_content_types(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertFalse(ctype.filter_content_types)

    def test_types__collective_microsite_MicroSite__allowed_content_types(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertEqual(ctype.allowed_content_types, ())

    def test_types__collective_microsite_MicroSite__schema(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertEqual(ctype.schema, 'plone.directives.form.Schema')

    def test_types__collective_microsite_MicroSite__klass(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertEqual(ctype.klass, 'collective.microsite.content.MicroSite')

    def test_types__collective_microsite_MicroSite__add_permission(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertEqual(ctype.add_permission, 'collective.microsite.ManageMicroSite')

    def test_types__collective_microsite_MicroSite__behaviors(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertEqual(ctype.behaviors, (
            'plone.app.content.interfaces.INameFromTitle',
            'plone.app.dexterity.behaviors.metadata.IDublinCore'))

    def test_types__collective_microsite_MicroSite__default_view(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertEqual(ctype.default_view, 'view')

    def test_types__collective_microsite_MicroSite__default_view_fallback(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertFalse(ctype.default_view_fallback)

    def test_types__collective_microsite_MicroSite__view_methods(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertEqual(ctype.view_methods, ('view',))

    def test_types__collective_microsite_MicroSite__default_aliases(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        self.assertEqual(
            ctype.default_aliases,
            {'edit': '@@edit', 'sharing': '@@sharing', '(Default)': '(dynamic view)', 'view': '(selected layout)'})

    def test_types__collective_microsite_MicroSite__action__view__title(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.title, 'View')

    def test_types__collective_microsite_MicroSite__action__view__condition(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.condition, '')

    def test_types__collective_microsite_MicroSite__action__view__url_expr(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.getActionExpression(), 'string:${folder_url}/')

    def test_types__collective_microsite_MicroSite__action__view__visible(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        action = ctype.getActionObject('object/view')
        self.assertTrue(action.visible)

    def test_types__collective_microsite_MicroSite__action__view__permissions(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.permissions, (u'View',))

    def test_types__collective_microsite_MicroSite__action__edit__title(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.title, 'Edit')

    def test_types__collective_microsite_MicroSite__action__edit__condition(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.condition, '')

    def test_types__collective_microsite_MicroSite__action__edit__url_expr(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.getActionExpression(), 'string:${object_url}/edit')

    def test_types__collective_microsite_MicroSite__action__edit__visible(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        action = ctype.getActionObject('object/edit')
        self.assertTrue(action.visible)

    def test_types__collective_microsite_MicroSite__action__edit__permissions(self):
        ctype = self.get_ctype('collective.microsite.MicroSite')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.permissions, (u'Modify portal content',))

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

    def test_uninstall__types__collective_microsite_MicroSite(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.microsite'])
        self.assertIsNone(self.get_ctype('collective.microsite.MicroSite'))
