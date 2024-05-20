from django.db import models
from accounts.models import CustomUser
from job.models import JobCategory,Skills,Jobs
from socialmedia.models import SocialMedia

# Create your models here.

class ProfessionalInformation(models.Model):
    position = models.CharField(max_length = 1500)
    cv = models.FileField(upload_to='users/jobseeker/images',null=True)
    user = models.OneToOneField(CustomUser,related_name = 'jobseeker',on_delete = models.CASCADE)
    expected_salary = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    job_category = models.ForeignKey(JobCategory,related_name = 'jobseekers',on_delete = models.PROTECT)
    
    def __str__(self) -> str:
        return self.user.username
    
class JobSeekerHaveSkills(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="jobseeker_skills")
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
    experience = models.PositiveIntegerField(default = 1)  # in years

class WorkExperience(models.Model):
    designation = models.CharField(max_length = 2000)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="work_experience")
    experience = models.PositiveIntegerField()  # in years
    company_name  = models.CharField(max_length = 1500)
    designation = models.CharField(max_length = 1000)
    job_categories = models.ForeignKey(JobCategory,related_name = "work_experience",on_delete = models.SET_NULL,null = True)
    joined_date = models.DateField(null = True)
    end_date  = models.DateField(null = True)
    still_work = models.BooleanField(default = False)

class Education(models.Model):
    college = models.CharField(max_length = 2000)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="educations")
    degree_name = models.CharField(max_length = 1000)  # in years
    company_name  = models.CharField(max_length = 1500)
    education_level = models.CharField(max_length = 1000)
    joined_date = models.DateField(null = True)
    end_date  = models.DateField(null = True)

class MySocialMedia(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="social_media")
    url = models.URLField()
    social_media = models.ForeignKey(SocialMedia,related_name="jobseeker_socialmedia",on_delete=models.CASCADE)

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

        

# {
#     "cv": "path/to/cv.pdf",
#     "user": 1,  // Assuming the user ID to whom this employer belongs
#     "expected_salary": 50000,
#     "job_category": 1,  // Assuming the job category ID
#     "skills": [  // Assuming skills are specified as a list of skill IDs
#         {"skill": 1, "experience": 2},  // Skill ID and experience in years
#         {"skill": 2, "experience": 3}
#     ]
# }
