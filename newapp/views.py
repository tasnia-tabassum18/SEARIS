'''from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def upload(request):
    return render(request,'upload_2.html')
    '''
from .models import course_t
#import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from newapp import models

''' 
def Import_csv(request):
    print('s')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:
          
            myfile = request.FILES['myfile']        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print(excel_file) 
            #empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')            
            files= pd.read_excel("."+excel_file,encoding='utf-8')
            print(type(files))
            #dbframe = files
            toRead1= files['COFFER_COURSE_ID'].values.tolist()
            toRead2= files['COURSE_NAME'].values.tolist()
            toRead3= files['CREDIT_HOUR'].values.tolist()
            count=0
            obj = models.course_t()
            while (count<len(toRead1)):
                print(toRead1[count])
                obj.course_ID=toRead1[count]
                obj.course_name=toRead2[count]
                obj.credit_hours= toRead3[count]
                print(type(obj))
                obj.save()
                count=count+1
 
            return render(request, 'upload.html',{})    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'upload_2.html',{})
    '''
def Import_csv(request):
    print('s')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:
        
            myfile = request.FILES['myfile']        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print(excel_file) 
            empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
            print(type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                
            #fromdate_time_obj = dt.datetime.strptime(dbframe.DOB, '%d-%m-%Y')
                obj = models.course_t.objects.create(course_ID=dbframe.COFFER_COURSE_ID,course_name=dbframe.COURSE_NAME, credit_hours=dbframe.CREDIT_HOUR)
                print(type(obj))
                obj.save()

            return render(request, 'upload_2.html', {
                'uploaded_file_url': uploaded_file_url
                })    
    except Exception as identifier:            
        print(identifier)

    return render(request, 'upload.html',{})