from django.db import models
from django.utils.translation import ugettext_lazy as _

from vuuvv.shop.models import Shop

class Category(TreeCategory):
    shop = models.ForeignKey(Shop, related_name='categories', verbose_name='Site')

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

class Product(models.Model):
    category = models.ManyToManyField(Category, verbose_name=_('Category'), related_name='products')
    name = models.CharField(_('Name'), max_length=100)
    slug = models.SlugField(_('Slug'))
    sku = models.CharField(_('SKU'), blank=True, max_length=30)
    price = models.FloatField(_('Price'), default=0.0)
    base_unit = models.CharField(_('Base Unit'), max_length=20)
    active = models.BooleanField(_('Active'), default=False)
    creation_date = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
    ordering = models.IntegerField(_('Sort Order'), default=999)

    related_products = models.ManyToManyField("self", verbose_name=_(u"Related products"), blank=True, null=True,
        symmetrical=False, related_name="reverse_related_products")

    accessories = models.ManyToManyField("Product", verbose_name=_(u"Acessories"), blank=True, null=True,
        symmetrical=False, through="ProductAccessories",
        related_name="reverse_accessories")

    weight = models.FloatField(_('Weight'), default=0.0)
    height = models.FloatField(_('Height'), d    weight = models.FloatField(_(u"Weight"), default=0.0)
    height = models.FloatField(_(u"Height"), default=0.0)
    length = models.FloatField(_(u"Length"), default=0.0)
    width = models.FloatField(_(u"Width"), default=0.0)efault=0.0)
    length = models.FloatField(_('Length'), default=0.0)
    width = models.FloatField(_('Width'), default=0.0)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ('ordering', )

class Unit(models.Model):
    product = models.ManyToManyField(Product, verbose_name=_('Product'), related_name="units")
    name = models.CharField(_('Name'), max_length=20)
    quantity = models.IntegerField(_('Quantity'))
    ordering = models.IntegerField(_('Sort Order'), default=999)

    def __unicode__(self):
        return u'%s<%d>' % (self.name, self.quantity)

    class Meta:
        verbose_name = _("Unit")
        verbose_name_plural = _("Units")
        ordergin = ('ordering',)

class PropertyKey(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    description = models.TextField(_('Description'), blank=True)
    ordering = models.IntegerField(_('Sort Order'), default=999)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _("PropertyKey")
        verbose_name_plural = _("PropertyKeys")
        ordergin = ('ordering',)

class Property(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('Product'), related_name='properties')
    key = models.ForeignKey(PropertyKey, verbose_name=_('Property Key'), related_name='properties')
    value = models.CharField(_('Value'), max_length=50)

    def __unicode__(self):
        return u'%s<%s>' % (self.key.name, self.value)

    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")
        ordergin = ('ordering',)

class OptionGroup(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('Product'), related_name='option_groups')
    name = models.CharField(_('Name'), max_length=50)
    ordering = models.IntegerField(_('Sort Order'), default=999)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _("OptionGroup")    weight = models.FloatField(_(u"Weight"), default=0.0)
    height = models.FloatField(_(u"Height"), default=0.0)
    length = models.FloatField(_(u"Length"), default=0.0)
    width = models.FloatField(_(u"Width"), default=0.0)
        verbose_name_plural = _("OptionGroups")
        ordergin = ('ordering',)

class Option(models.Model):
    group = models.ForeignKey(OptionGroup, verbose_name=_('Option Group'), related_name='options')
    name = models.CharField(_('Name'), max_length=100)
    price_change = models.FloatField(_('Price'), blank=True, null=True, default=0.0)
    ordering = models.IntegerField(_('Sort Order'), default=999)

    def __unicode__(self):
        return u'%s<%s>' % (self.group.name, self.name)

    class Meta:
        verbose_name = _("Option")
        verbose_name_plural = _("Option")
        ordergin = ('ordering',)

class Image(models.Model):
    content_type = models.ForeignKey(ContentType, verbose_name=_('Content type'), related_name='images', blank=True, null=True)
    content_id = moddels.PositiveIntegerField(_('Content id'), blank=True, null=True)
    content = generic.GenericForeignKey(ct_field='content_type', fk_field='content_id')

    name = models.CharField(_('Name'), blank=True, max_length=100)
    ordering = models.IntegerField(_('Sort Order'), default=999)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
        ordergin = ('ordering',)

class File(models.Model):
    content_type = models.ForeignKey(ContentType, verbose_name=_('Content type'), related_name='files', blank=True, null=True)
    content_id = moddels.PositiveIntegerField(_('Content id'), blank=True, null=True)
    content = generic.GenericForeignKey(ct_field='content_type', fk_field='content_id')

