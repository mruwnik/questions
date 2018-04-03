from django.contrib import admin

from answers.models import Question, Category, Answer, Source


admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(Source)
