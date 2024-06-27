from . import frontend_setting
mapping = {
    "company_register":{
        "model_name":"Company",
        "path":"",
        "admin_message":"new company has created",
        "user_message":"",
    },
    "post_jobs":{
        "model_name":"Jobs",
        "path":"jobs/{job_id}",
        "admin_message":"{}",
        "user_message":"{}",
    },
    "apply_job":{ #these goes to employer,and jobseekers
        "model_name":"apply_job",
        "admin_message":"",
        "path":"dashboard/applicants/all",
        "admin_message":"{}",
        "user_message":"{}",
    },
    "approved_jobseekers":{ #these goes to jobseekers
        "model_name":"Job",
        "path":"jobs/{job_id}",
        "admin_message":"{}",
        "user_message":"{}",
    },
    "password_changed":{
        "model_name":"CustomUser",
        "path":"notifications",
        "admin_message":"Your password has been changed",
        "user_message":"{}",
    },
  

}