from django.contrib import admin

# Register your models here.
from .models import Question

class QuestionAdmin(admin.ModelAdmin): # 검색기능 
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)

