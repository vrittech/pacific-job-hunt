from django.db import models
from accounts.models import CustomUser
from job.models import Jobs

# Create your models here.
class JobsApply(models.Model):
    user = models.ForeignKey(CustomUser,related_name = 'apply_jobs',on_delete = models.CASCADE)
    job = models.ForeignKey(Jobs,related_name ='job_seekers', on_delete = models.PROTECT)
    status = models.CharField(max_length = 100 , choices = (('pending',"Pending"),('approved',"Approved"),('rejected',"Rejected")),default = "pending")
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.user.username)+'-'+str(self.job.title)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'job'], name='unique_user_job_apply')
        ]
