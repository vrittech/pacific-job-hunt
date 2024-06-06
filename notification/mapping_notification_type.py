from . import frontend_setting
mapping = {
    "apply_job":{
        "model_name":"Appointment",
        "admin_message":"",
        "path":"appointments",
        "admin_message":"{}",
        "user_message":"{}",
    },
    "approved_jobseekers":{
        "model_name":"Order",
        "path":"orderDetails/:{order_id}",
        "admin_message":"{}",
        "user_message":"{}",
    },
    "password_changed":{
        "model_name":"CustomUser",
        "path":"notifications",
        "admin_message":"{}",
        "user_message":"{}",
    },
    "post_jobs":{
        "model_name":"Order",
        "path":"orderDetails/{order_id}",
        "admin_message":"{}",
        "user_message":"{}",
    },
}