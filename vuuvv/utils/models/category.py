from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.transaction import commit_on_success

from mptt.models import MPTTModel, TreeForeignKey

class TreeCategory(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, verbose_name=_('Parent'), related_name='children')
    name = models.CharField(_('Name'), max_length=100)
    slug = models.CharField(_('Slug'), max_length=100)
    url = models.CharField(_('URL'), max_length=255, blank=True, editable=False, db_index=True)

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(TreeCategory, self).__init__(*args, **kwargs)
        self._old_url = self.url

    def __unicode__(self):
        return u'%s' % (self.name)

    @commit_on_success
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = self.name.lower()

        cached_urls = {}

        if self.is_root_node():
            self.url = u'/%s/' % self.slug if self.slug else u'/'
        else:
            self.url = u'%s%s/' % (self.parent.url, self.slug)
        super(TreeCategory, self).save(*args, **kwargs)
        if self.is_leaf_node() or self.url == self._old_url:
            return

        descendants = self.get_descendants()

        stack = [self]
        last_page = self
        for node in descendants:
            parent = stack[-1]
            if node.rght < last_page.rght:
                # child node
                stack.append(last_page)
                parent = last_page
            else:
                # tree up
                while node.rght > parent.rght:
                    stack.pop()
                    parent = stack[-1]

            node.url = u'%s%s/' % (parent.url, node.slug)
            super(TreeCategory, node).save()
            last_page = node


