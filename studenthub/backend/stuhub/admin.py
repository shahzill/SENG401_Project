from django.contrib import admin
from .models import Course
from .models import Tutor
from .models import Comment
from .models import Professor
from .models import CourseRequest
from.models import Applicant


admin.site.register(Course)
admin.site.register(Tutor)
admin.site.register(Professor)
admin.site.register(Comment)
admin.site.register(CourseRequest)
admin.site.register(Applicant)