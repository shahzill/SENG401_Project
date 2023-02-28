from django.contrib import admin
from .models import Course
from .models import Tutor
from .models import Comment
from .models import Professor



admin.site.register(Course)
admin.site.register(Tutor)
admin.site.register(Professor)
admin.site.register(Comment)
