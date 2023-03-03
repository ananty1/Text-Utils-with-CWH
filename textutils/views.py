# I have created this file-Anant highly inspired by CWH
from django.http import HttpResponse
import requests
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    print(djtext,type(djtext))
    remove_punc=request.POST.get('remove_punc','off')
    full_caps=request.POST.get('full_caps','off')
    nwln_remover=request.POST.get('nwln_remover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
 
    params={
        'purpose':'Choose something',
        'analyzed_text':'NOthong to compare',
        }
    punct_list='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed_text=[]
    if remove_punc=='on':
        for text in djtext:
            if text not in punct_list:
                analyzed_text.append(text)
        analyzed_text=''.join(analyzed_text)#list append is  faster than string addition
        params={
        'purpose':'Removed Punctuation',
        'analyzed_text':analyzed_text,
        }
        djtext=analyzed_text
    
    if full_caps=='on':
        analyzed_text=''
        for char in djtext:
            analyzed_text+=char.upper()
        
        params={
        'purpose':'CAPITALIZE TEXT',
        'analyzed_text':analyzed_text,
        }
        djtext=analyzed_text
   
    
    if(nwln_remover=='on'):
        analyzed_text=''
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed_text+=char
        params={
        'purpose':'Removed new line',
        'analyzed_text':analyzed_text,
        }
        djtext=analyzed_text
    
    if(extraspaceremover=='on'):
        analyzed_text=''
        for index,char in enumerate(djtext):
            if djtext[index]!=len(djtext) and djtext[index]==' ' and djtext[index+1]==' ':
                pass
            else:
                analyzed_text+=char
        
        params={
        'purpose':'Removed Extra Space',
        'analyzed_text':analyzed_text,
        }
        djtext=analyzed_text
    
    if(charcount=='on'):
        analyzed_text=f'The total Count of charcters in {djtext} :'
        count=len(djtext)
        analyzed_text+=str(count)
        params={
        'purpose':'Removed Extra Space',
        'analyzed_text':analyzed_text,
        }

    if (remove_punc!='on' and nwln_remover!='on' and extraspaceremover!='on' and charcount!='on' and full_caps!='on'):
        return HttpResponse("PLease select any operation and try again.")
    return render(request,'analyze.html',params)


