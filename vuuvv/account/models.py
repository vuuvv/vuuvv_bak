from django.db import models

class ViewPermission(models.Model):
    HTTP_METHOD = (
        ('get', 'get'),
        ('post', 'post'),
        ('put', 'put'),
        ('delete', 'delete'),
        ('head', 'head'),
        ('options', 'options'),
        ('trace', 'trace')
    )
    name = models.CharField(_('name'), max_length=50)
    method = models.CharFiels(_('method'), max_length=20)

    class Meta:
        verbose_name = _('permission')
        verbose_name_plural = _('permissions')
        ordering = ('name',)

    def __unicode__(self):
        return u"%s | %s" %(
            unicode(self.name),
            unicode(self.method)
        )

class User(models.Model):
    username = models.CharField(_('username'), max_length=30, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                    '@/./+/-/_ characters'))

    password = models.CharField(_('password'), max_length=128)
    email = models.CharField(_('e-mail address'), blank=True)

    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    is_superuser = models.BooleanField(_('superuser status'), default=False,
        help_text=_('Designates that this user has all permissions without '
                    'explicitly assigning them.'))
    last_login = models.DateTimeField(_('last login'), default=timezone.now)
    created_date = models.DateTimeField(_('created dated'), default=timezone.now)

    roles = models.ManytoManyField(Role, verbose_name=_('roles'),
        blank=True, help_text=_('The roles this user belongs to. A user will '
                                'get all permissions granted to each of '
                                'his/her role.'))
    view_permissions = models.ManytoManyField(ViewPermission,
        verbose_name=_('user permission'), blank=True,
        help_text='Specific permissions for this user.')

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

class Role(models.Model):
    name = models.CharField(_('name'), max_length=80, unique=True)
    view_permissions = models.ManytoManyField(ViewPermission, blank=True,
                                              verbose_name=_('permissions'))

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')

    def __unicode__(self):
        return self.name

