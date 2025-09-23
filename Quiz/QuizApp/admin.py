from django.contrib import admin
from .models import QuizCategory,QuizQuestions,QuizAnswers,UserSubmission,UserScore,UserBoard



class QuizAnswersInline(admin.TabularInline):
    model = QuizAnswers
    extra = 4  # show 4 empty fields for options
    max_num = 4
    min_num = 4

class QuizQuestionsAdmin(admin.ModelAdmin):
    inlines = [QuizAnswersInline]
    list_display = ('question', 'category', 'points')
    list_filter = ('category',)



class QuizAnswersAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'is_corrected')



class QuizCategroyAdmin(admin.ModelAdmin):
    list_display=('category','type','duration')



class UserSubmissionAdmin(admin.ModelAdmin):
    list_display=('user','question','option','is_corrected')


class UserScoreAdmin(admin.ModelAdmin):
    list_display=('user','category','obtained_score',)



admin.site.register(QuizAnswers, QuizAnswersAdmin)
admin.site.register(QuizCategory,QuizCategroyAdmin)
admin.site.register(UserSubmission,UserSubmissionAdmin)
admin.site.register(UserScore,UserScoreAdmin)
admin.site.register(QuizQuestions, QuizQuestionsAdmin)
admin.site.register(UserBoard)
