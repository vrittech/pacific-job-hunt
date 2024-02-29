from django.db import models
from accounts.models import CustomUser
from job.models import JobCategory,Skills,Jobs

# Create your models here.

class Employer(models.Model):
    cv = models.FileField(upload_to='users/employer',null=True)
    user = models.OneToOneField(CustomUser,related_name = 'employer',on_delete = models.CASCADE)
    expected_salary = models.PositiveIntegerField()
    job_category = models.ForeignKey(JobCategory,related_name = 'employer',on_delete = models.PROTECT)
    skills = models.ManyToManyField(Skills,through="EmployerHaveSkills",related_name='employers')

    def __str__(self) -> str:
        return self.user.username

class EmployerHaveSkills(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
    experience = models.PositiveIntegerField()  # in years

class JobsApply(models.Model):
    user = models.ForeignKey(CustomUser,related_name = 'apply_jobs',on_delete = models.CASCADE)
    job = models.ForeignKey(Jobs,related_name ='job_seekers', on_delete = models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.user.username)+'-'+str(self.job.title)

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
