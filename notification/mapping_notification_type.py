from . import frontend_setting
mapping = {
    "apply_job":{
        "model_name":"apply_job",
        "admin_message":"",
        "path":"dashboard/applicants/all",
        "admin_message":"{}",
        "user_message":"{}",
    },
    "approved_jobseekers":{
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
    "post_jobs":{
        "model_name":"Order",
        "path":"jobs/{job_id}",
        "admin_message":"{}",
        "user_message":"{}",
    },
}