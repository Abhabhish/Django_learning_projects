from django.contrib import admin
from .models import Question,Choice

# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=-1


class QuestionAdmin(admin.ModelAdmin):
    # fields=["pub_date","question_text"]
    fieldsets=[
        ("Question",{"fields":["question_text"]}),
        ("Date",{"fields":["pub_date"]})
    ]
    inlines=[ChoiceInline]
    list_display=[
        "question_text",
        "pub_date",
        "was_published_recently",
    ]
    list_filter=["pub_date"]
    search_fields=["question_text"]

admin.site.register(Question,QuestionAdmin)