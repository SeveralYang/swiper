from datetime import datetime
from user.models import User

def get_rcmd_users(user:User):
    sex = user.profile.date_sex
    location = user.profile.location
    now_year = datetime.today().year
    min_year = now_year - user.profile.max_data_age 
    max_year = now_year- user.profile.min_data_age 
    users = User.objects.filter(
        location=location,
        sex=sex,
        birth_year__gte=min_year,
        birth_year__lte=max_year
    )

    for u in users:
        print(u.nick_name)
        
    return users