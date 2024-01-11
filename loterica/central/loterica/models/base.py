from django.db import models


class BaseModels(models.Model):

    abstract = True
    app_label = 'loterica'