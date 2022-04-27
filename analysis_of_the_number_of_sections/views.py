from django.db import connection
from django.shortcuts import render

# Create your views here.
def generate(request):

    
    query1= """
            select d.school_title, count(*) AS Count
            from section_t AS S, department_t AS D
            where S.dept_id=D.dept_id AND
            S.session= {n} AND S.year={m} AND
            enroll_capacity<50
            group BY S.dept_id
            """
    with connection.cursor() as cursor:
        cursor.execute(query1)   
        result = cursor.fetchall()
    query2= """
                select sum(Count) AS total
                from(
                    select d.school_title, count(*) AS Count
                    from section_t AS S, department_t AS D
                    where S.dept_id=D.dept_id AND
                    S.session= {n} AND S.year={m} AND
                    enroll_capacity<50
                    group BY S.dept_id) AS total
            """
    result=[]
    with connection.cursor() as cursor:
        cursor.execute(query2)   
        result = cursor.fetchall()
        context={
            'school_title':school_title
            'school_total':count
            'total':total
        }
        return render(request,'Analysis_the_number_of_sections.html')
