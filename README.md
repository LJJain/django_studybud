# StudyBud Project

## Github
> https://github.com/LJJain/django_studybud.git

## 日誌
> 2022.10.29
- started Project (studybud) & App (base)
- urls & templates 
- database & createsuperuser

## 筆記
> Models
- auto_now_add 只會新增第一次的時間 / auto_now 只要有修改就會變更時間
- 每次修改就要做一次 makemigrations
- 導入models:

    from .models import Room

    admin.site.register(Room)
- views:

    from .models import Room

## 課程網站
> https://www.youtube.com/watch?v=PtQiiknWUcI&t=297s&ab_channel=TraversyMedia