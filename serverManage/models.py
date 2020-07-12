from django.db import models


# Create your models here.

class DbServerInfo(models.Model):
    domain = models.CharField(verbose_name='域名', max_length=50)
    ip = models.GenericIPAddressField(verbose_name='ip地址')
    user = models.CharField(verbose_name='用户', max_length=50)
    user_type = models.CharField(verbose_name='用户类型', max_length=50)

    def __str__(self):
        return f'{self.user}:{self.domain} -- {self.ip}'

    class Meta:
        db_table = 'db_server_info'
