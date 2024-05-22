from django.db import models
from accounts.models import CustomUser
from job.models import JobCategory,Skills,Jobs
from professions.models import Profession

# Create your models here.
class ProfessionalInformation(models.Model):
    position = models.CharField(max_length = 1500)
    cv = models.FileField(upload_to='users/jobseeker/images',null=True)
    user = models.OneToOneField(CustomUser,related_name = 'professional_information',on_delete = models.CASCADE)
    expected_salary = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    interest = models.ManyToManyField(JobCategory,related_name="jobseekers_interests")
    about = models.TextField()
    address_1 = models.CharField(max_length = 450)
    address_2 = models.CharField(max_length = 450,null = True,blank = True,default = '')
    profession = models.ForeignKey(Profession,related_name="jobseekers",on_delete = models.SET_NULL,null=True)

    def __str__(self) -> str:
        return self.user.username
    
class JobSeekerHaveSkills(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="jobseeker_skills")
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
    experience = models.PositiveIntegerField(default = 1)  # in years

class JobsApply(models.Model):
    user = models.ForeignKey(CustomUser,related_name = 'apply_jobs',on_delete = models.CASCADE)
    job = models.ForeignKey(Jobs,related_name ='job_seekers', on_delete = models.PROTECT)
    status = models.CharField(max_length = 100 , choices = (('pending',"Pending"),('approved',"Approved"),('rejected',"Rejected")),default = "pending")
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.user.username)+'-'+str(self.job.title)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'job'], name='unique_user_job_application')
        ]

        
