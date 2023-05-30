from django.db import models


# Create your models here.
class Schedule(models.Model):
    service_provider = models.ForeignKey(
        "auth.User", related_name="schedules", on_delete=models.CASCADE
    )
    date_time = models.DateTimeField()
    custumer_name = models.CharField(max_length=255)
    custumer_email = models.EmailField()
    custumer_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.custumer_name
