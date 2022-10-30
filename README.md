# StudyBud Project

## Github
> https://github.com/LJJain/django_studybud.git

## 日誌
> 2022.10.29
- started Project (studybud) & App (base)
- urls & templates 
- database & createsuperuser
- forms
- User Login & Register
> 2022.10.30
- setting static files

## 筆記
> Models
- auto_now_add 只會新增第一次的時間 / auto_now 只要有修改就會變更時間
- 每次修改就要做一次 makemigrations
- 導入models:

    from .models import Room

    admin.site.register(Room)
- views:

    from .models import Room

> Filter
- {% url 'home' %}?q={{topic.name}}
- from django.db.models import Q #動態filter 作為多個search的篩選條件

> Setting Static
- settings.py
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]




## 課程網站
> https://www.youtube.com/watch?v=PtQiiknWUcI&t=297s&ab_channel=TraversyMedia