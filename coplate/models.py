from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(
        max_length=15, 
        unique=True, 
        blank=True,
        validators=[validate_no_special_characters],
        error_messages={
            "unique":"이미 사용 중인 닉네임입니다.", 
            "validators":"닉네임에 특수문자는 포함될 수 없습니다."
        },
    )
    kakao_id = models.CharField(
        max_length=20, 
        blank=True,
        validators=[validate_no_special_characters],
        error_messages={
            "validators":"카카오ID에 특수문자는 포함될 수 없습니다."
        },
    )
    address = models.CharField(
        max_length=40,
        blank=True,
        validators=[validate_no_special_characters],
        error_messages={
            "validators":"주소에 특수문자는 포함될 수 없습니다."
        },
    )

    def __str__(self):
        return self.email
