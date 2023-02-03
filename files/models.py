from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings


class File(models.Model):
    NEW = 'new'
    UPDATED = 'updated'
    VERIFIED = 'verified'

    STATUSES = (
        (NEW, 'новый'),
        (UPDATED, 'изменен'),
        (VERIFIED, 'проверен')
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files', validators=[FileExtensionValidator(['py'])])
    status = models.CharField(choices=STATUSES, default=NEW, max_length=8)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        storage, path = self.file.storage, self.file.path
        super().delete(*args, **kwargs)
        storage.delete(path)


class Logs(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    logs = models.TextField()

    send_mail = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
