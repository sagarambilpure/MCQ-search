from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import json
import glob
import os


def index(request):
    subjects = glob.glob("search/files/*.csv")
    subjects = [os.path.basename(i)[:-4] for i in subjects]
    return render(request, 'search/index.html', {"subjects": subjects})


def filter_ques(request):
    words = request.GET["words"].lower()
    subject = request.GET["subject"]
    filtered_questions = []
    l = pd.read_csv("search/files/"+subject.lower()+".csv")
    for i in words.split(" "):
        l = l[l["questions"].str.lower().str.contains(i, regex=False)]
    for i in l.iterrows():
        row = i[1].dropna()
        filtered_questions.append(
            {"question": row.iloc[0], "answer": (" || ".join(row.iloc[1:].values))})
    print(filtered_questions)
    return HttpResponse(json.dumps(filtered_questions), content_type='application/json')
