from django.shortcuts import render,redirect
from  django.contrib import messages
from django.db.models import Count,Sum
from .models import QuizCategory,QuizQuestions,QuizAnswers,UserSubmission,UserScore,UserBoard
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Q




def CategoryDisplay_view(request):
    # category=QuizCategory.objects.annotate(questionsCount=Count('questions'))
    category = QuizCategory.objects.all()

    userBoard={}
    try:
        userBoard=UserBoard.objects.get(user=request.user)
    except:
        print()
    context={"category":category,"userBoard":userBoard,"easy":5,"medium":10,"hard":20}
    return render(request,"QuizApp/quizCategory.html",context)




def submission_view(request,id):
    category=QuizCategory.objects.get(id=id)
    questions = QuizQuestions.objects.filter(category=category).prefetch_related("answers").order_by('?')[:15]
    totalQuestions = QuizQuestions.objects.filter(category=category).prefetch_related("answers").order_by('?')[:15].count()
    totalScore=0
    if category.type == "easy":
        totalScore=10*totalQuestions
    elif category.type == "medium":
        totalScore=15*totalQuestions
    else:
        totalScore=20*totalQuestions
    if request.method=="POST":
       score=0
       totalCorrect=0
       userQuiz=[]
       print(category.type,totalScore,totalQuestions)
       questions=QuizQuestions.objects.filter(category=category)
       for question in questions:
            option=request.POST.get(f"q{question.id}")
            if option:
               answer_obj=QuizAnswers.objects.get(id=option)
               if answer_obj.is_corrected:
                   score += question.points
                   totalCorrect += 1
                   userSub=UserSubmission.objects.create(user=request.user,question=question,option=answer_obj.answer,is_corrected=answer_obj.is_corrected,correct_ans=answer_obj.answer)
                   userQuiz.append(userSub)
               else:
                    ans=QuizAnswers.objects.get(question=question,is_corrected=True)
                    userSub=UserSubmission.objects.create(user=request.user,question=question,option=answer_obj.answer,correct_ans=ans.answer)
                    userQuiz.append(userSub)
            else:
                correct_ans=""
                try:
                    ans=QuizAnswers.objects.get(question=question,is_corrected=True)
                    correct_ans=ans.answer
                except:
                    correct_ans=""
                userSub=UserSubmission.objects.create(user=request.user,question=question,option="",correct_ans=correct_ans)
                userQuiz.append(userSub)
        
       is_passed = False
       totalWrong=totalQuestions-totalCorrect
       percentage=(totalCorrect/totalQuestions)*100
       if(percentage>33): 
           is_passed=True
    #    created , userScore = UserScore.objects.get_or_create(user=request.user, category=category,
    #                                                          defaults = { time_taken=float(request.POST.get("time_taken")), total_score=totalScore,obtained_score=score,totalCorrect=totalCorrect,totalWrong=totalWrong,percentage=round(percentage,3)})
    #    if not created:
    #             userScore.obtained_score=score
    #             userScore.total_score=totalScore
    #             userScore.is_passed=is_passed
    #             userScore.totalCorrect=totalCorrect
    #             userScore.totalWrong=totalWrong
    #             userScore.percentage=round(percentage,3)
    #             userScore.time_taken=float(request.POST.get("time_taken"))
    #             userScore.save()

       userScore, created = UserScore.objects.get_or_create(
            user=request.user,
            category=category,
            defaults={
                "total_score": totalScore,
                "obtained_score": score,
                "totalCorrect": totalCorrect,
                "totalWrong": totalWrong,
                "percentage": round(percentage, 2),
                "time_taken": round(float(request.POST.get("time_taken", 0))/60,2)
            }
        )

       if not created:
            # Update existing score
            userScore.obtained_score = score
            userScore.total_score = totalScore
            userScore.is_passed = is_passed
            userScore.totalCorrect = totalCorrect
            userScore.totalWrong = totalWrong
            userScore.percentage = round(percentage, 2)
            userScore.time_taken = round(float(request.POST.get("time_taken", 0))/60,2)
            userScore.save()
       
       
       context={"userScore":userScore,"userQuiz":userQuiz,"totalScore":totalScore,"requiredScore":round((33/100)*totalScore,3),"category":category,"totalQuestions":totalQuestions}
       return render(request,"QuizApp/quizScore.html",context)
    
    questions = QuizQuestions.objects.filter(category=category).prefetch_related("answers").order_by('?')[:15]
    context={"questions":questions,"category":category,"points":totalScore,"duration": category.duration}
    return render(request,"QuizApp/QuizQuestion.html",context)
            
                