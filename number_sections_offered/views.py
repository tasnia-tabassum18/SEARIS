from urllib import request
from django.shortcuts import render

# Create your views here.
def chart(request):
    query="""
            SELECT ( 
                CASE 
                    
                    WHEN S.enroll_capacity BETWEEN  1 AND 10 THEN '  1-10'  
                    WHEN S.enroll_capacity BETWEEN 11 AND 20 THEN ' 11-20'  
                    WHEN S.enroll_capacity BETWEEN 21 AND 30 THEN ' 21-30'  
                    WHEN S.enroll_capacity BETWEEN 31 AND 35 THEN ' 31-35'  
                    WHEN S.enroll_capacity BETWEEN 36 AND 40 THEN ' 36-40'  
                    WHEN S.enroll_capacity BETWEEN 41 AND 50 THEN ' 41-50'  
                    WHEN S.enroll_capacity BETWEEN 51 AND 55 THEN ' 51-55' 
                    WHEN S.enroll_capacity BETWEEN 56 AND 60 THEN ' 56-60' 
                    WHEN S.enroll_capacity > 60 THEN ' 60+'
                END 
            ) AS Enrollment, S.dept_id AS department, COUNT(*) AS Total_Sections
            FROM section_t S, department_t D
            WHERE 
                S.dept_id = D.dept_id
                AND D.school_title="SETS" AND
                S.session= {n} AND S.year={m} AND Enrollment= 1-10
            GROUP BY Enrollment, department
            ORDER BY  Enrollment,department ASC
            """ 
        with connection.cursor() as cursor:
            cursor.execute(query)   
            result = cursor.fetchall()

    return render(request,'Number_of_section_offered_SETS.html')