from django.db import models


class IzUser(models.Model):
    username = models.CharField(max_length=32, verbose_name='사용자명')
    useremail = models.CharField(max_length=128, verbose_name="사용자 이메일")
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')


    # 어드민 페이지에 유저이름으로 관리하게 할 수 있음.
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'iz_user'
        verbose_name_plural = '아이즈원 사용자'