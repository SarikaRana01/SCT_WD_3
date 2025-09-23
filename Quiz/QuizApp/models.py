from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class QuizCategory(models.Model):
    category=models.TextField(null=False,blank=False)
    type=models.CharField(max_length=20,choices=[("easy","easy"),("medium","medium"),("hard","hard")],null=False,blank=False)
    duration=models.IntegerField(null=False,blank=False,default=15)


    def __str__(self):
        return self.category
    


class QuizQuestions(models.Model):
    category=models.ForeignKey(QuizCategory,on_delete=models.CASCADE,related_name="questions")
    question=models.TextField(null=False,blank=False)
    points=models.IntegerField(default=0,null=False,blank=False)


    def save(self,*args,**kwargs):
        if self.category.type=="easy":
            self.points=5
        elif self.category.type=="medium":
            self.points=10
        else:
            self.points=20
        super().save(*args, **kwargs) 

    def __str__(self):
        return f"{self.question}"
    


class QuizAnswers(models.Model):
    question=models.ForeignKey(QuizQuestions,on_delete=models.CASCADE,related_name="answers")
    answer=models.TextField(null=False,blank=False)
    is_corrected=models.BooleanField(default=False)
    





class UserSubmission(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="usersubmission")
    question=models.ForeignKey(QuizQuestions,on_delete=models.CASCADE,related_name="questionSubmission")
    option=models.TextField()
    correct_ans=models.TextField()
    is_corrected=models.BooleanField(default=False)



    def __str__(self):
        return f"{self.user.username} -> {self.option} -> {self.is_corrected}"




class UserScore(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userscore")
    category=models.ForeignKey(QuizCategory,on_delete=models.CASCADE,related_name="usertype")
    obtained_score=models.IntegerField(default=0)
    total_score=models.IntegerField(default=0)
    time_taken=models.FloatField()
    date=models.DateField(auto_now=True)
    is_passed=models.BooleanField(default=False)
    totalCorrect=models.IntegerField(default=0)
    totalWrong=models.IntegerField(default=0)
    percentage=models.FloatField(default=0.0,)



    def __str__(self):
        return f"{self.user.username} -> {self.total_score}"
    


class UserBoard(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userBoard")
    user_score=models.ForeignKey(UserScore,on_delete=models.CASCADE,related_name="board")
    time_spend=models.TimeField()
    average_score=models.IntegerField()
    total_points=models.IntegerField()



    

