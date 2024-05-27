from django.db import models
from accounts.models import CustomUser
from job.models import Jobs
from resumes.models import Resumes

# Create your models here.
class JobsApply(models.Model):
    user = models.ForeignKey(CustomUser,related_name = 'apply_jobs',on_delete = models.CASCADE)
    job = models.ForeignKey(Jobs,related_name ='job_seekers', on_delete = models.PROTECT)
    status = models.CharField(max_length = 100 , choices = (('pending',"Pending"),('approved',"Approved"),('rejected',"Rejected")),default = "pending")
    full_name = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200,null = True,blank =  True)
    cv = models.ForeignKey(Resumes,related_name="job_apply",on_delete=models.CASCADE)
    cover_letter_file = models.FileField(upload_to='users/jobseeker/coverletter',null=True,blank=True)
    cover_letter_str = models.TextField(null= True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.user.username)+'-'+str(self.job.title)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'job'], name='unique_user_job_apply')
        ]
