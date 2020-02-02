from django.db import models
 
class CustomManager(models.Manager):
    ''' Use this manager to get objects that have a deleted field '''

    # def get_queryset(self):
    #     return super(CustomManager, self).get_queryset().filter(is_delete=False)

    def all(self):
        return super(CustomManager, self).get_queryset().filter(is_delete=False)

    def deleted(self):
        return super(CustomManager, self).getquery_set().filter(is_delete=True)
