from django.db import models
from accounts.models import CustomUser
from job.models import Jobs

# Create your models here.
class JobsBookmark(models.Model):
    user = models.ForeignKey(CustomUser,related_name = 'saved_jobs',on_delete = models.CASCADE)
    job = models.ForeignKey(Jobs,related_name ='saved_jobs', on_delete = models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.user.username)+'-'+str(self.job.title)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'job'], name='unique_user_job_bookmark_application')
        ]