from django.shortcuts import render

QUIZ_FILENAME="quiz.txt"


def homepageadmin(request):
    return render(request, 'homepageadmin.html')


def addquizhome(request):
    return render(request, 'addquiz.html')


def addquiz(request):
    quizname = request.POST.get("quizname")
    fp = open(QUIZ_FILENAME, 'a')
    fp1 = open(QUIZ_FILENAME)
    data = fp1.readlines()
    quizes = []
    for i in data:
        quizes.append(i.strip())
    print(quizes)
    fp1.close()
    if quizname in quizes:
        return render(request, 'addquiz.html', {"error": "quiz already exists"})
    else:
        fp.write(quizname+"\n")
        fp.close()
        return render(request, 'addquestionhome.html', {"quizname": quizname})


def addquestionhome(request):
    return render(request, 'addquestionhome.html')


def addquestion(request):
    quizname = request.POST.get("quizname")
    question = request.POST.get("question")
    op1 = request.POST.get("op1")
    op2 = request.POST.get("op2")
    op3 = request.POST.get("op3")
    op4 = request.POST.get("op4")
    ans = request.POST.get("ans")
    fp1 = open(quizname + ".txt", "a")
    fp1.write("{}|{}|{}|{}|{}|{}".format(question, op1, op2, op3, op4, ans))
    fp1.close()
    return render(request, 'addquestionhome.html', {"quizname": quizname})


def addquestiontoexistinghome(request):
    fp1 = open(QUIZ_FILENAME)
    data = fp1.readlines()
    quizes = []
    for i in data:
        quizes.append(i.strip())
    print(quizes)
    return render(request, 'addquestiontoexisting.html', {"quizes": quizes})


def addquestiontoexisting(request):
    fp1 = open(QUIZ_FILENAME)
    data = fp1.readlines()
    quizes = []
    for i in data:
        quizes.append(i.strip())
    quizname = request.POST.get("quizname")
    question = request.POST.get("question")
    op1 = request.POST.get("op1")
    op2 = request.POST.get("op2")
    op3 = request.POST.get("op3")
    op4 = request.POST.get("op4")
    ans = request.POST.get("ans")
    fp1 = open(quizname + ".txt", "a")
    fp1.write("{}|{}|{}|{}|{}|{}".format(question, op1, op2, op3, op4, ans)+"\n")
    fp1.close()
    return render(request, 'addquestiontoexisting.html', {"quizes": quizes})
# Create your views here.
