from django.db import models


class Log(models.Model):

    LEVEL = (
        ('0', 'Информация'),
        ('1', 'Замечание'),
        ('2', 'Неисправность'),
        ('3', 'Срочное сообщение')
    )

    created = models.DateTimeField(auto_now_add=True)
    station = models.ForeignKey('devices.Station', null=True, verbose_name='Связанная станция', on_delete=models.SET_NULL)
    device = models.ForeignKey('devices.Device', null=True, verbose_name='Связанное устройство', on_delete=models.SET_NULL)
    type = models.CharField(max_length=1, choices=LEVEL, default=0)
    text = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.text
