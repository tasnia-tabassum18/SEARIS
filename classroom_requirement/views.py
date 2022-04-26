from django.shortcuts import render
from django.db import connection

'''
Classroom requirement summary based on class size, total slots per day, and sections
offered:
Based on a given range of class size (any of the following ranges selected by user: 1-20,
21-30, 31-35, 36-40, 41-50, 51-54, 55-64, 65-124, 125-168; class size = number of
students enrolled in a section), and accordingly the number of sections offered in a
semester, how many classrooms would be needed if each day’s schedule was divided
into seven slots versus the number of such such classroom that are actually available?
What about the same for eight slots?
'''

def classroom_requirement(request):

    query = """     
            SELECT session_name      #to get session names 
            FROM section_t
            GROUP BY session_name
            """
    sessions = [] #creating a dictionary containing all session names
    with connection.cursor() as cursor:
        cursor.execute(query)
        sessions = cursor.fetchall() #fetches all the rows of the query above and stores them as tuples

   
    query = """     
            SELECT syear
            FROM section_t
            GROUP BY syear
            ORDER BY syear
            """
    years = []
    with connection.cursor() as cursor:
        cursor.execute(query)
        years = cursor.fetchall()


# need to add custom code as per table/chart
    if request.method == 'POST':
        year = request.POST.get('selected_year', "2020")
        session = request.POST.get('selected_session', "Autumn")

    else:
        year = years[-1][0]
        session = sessions[-1][0]

    #Used round function here to round the value in 1 decimal place

    query = """
            SELECT DATA.size AS "Class Size", DATA.sections, DATA.class7 AS "Slots-7", DATA.class8 AS "Slots-8"
            FROM(
                SELECT ( 

                    CASE 
                        WHEN s.enroll_capacity  BETWEEN  1 AND  10 THEN '1-10'  
                        WHEN s.enroll_capacity  BETWEEN 21 AND 30 THEN '21-30'  
                        WHEN s.enroll_capacity  BETWEEN 30 AND 35 THEN '30-35'  
                        WHEN s.enroll_capacity  BETWEEN 36 AND 40 THEN '36-40'  
                        WHEN s.enroll_capacity  BETWEEN 41 AND 50 THEN '41-50'  
                        WHEN s.enroll_capacity  BETWEEN 51 AND 54 THEN '51-54'  
                        WHEN s.enroll_capacity  BETWEEN 55 AND 64 THEN '55-64' 
                        WHEN s.enroll_capacity  BETWEEN 65 AND 124 THEN '65-124'
                        WHEN s.enroll_capacity  BETWEEN 124 AND 168 THEN '124-168' 

                        ELSE '0'

                    END 
                ) AS size, ROUND(COUNT(*)/14, 1) AS class7, ROUND(COUNT(*)/16, 1) AS class8,COUNT(*) AS sections

                FROM section_t AS s
                WHERE 
                syear = %(year)s 
                AND session_name = %(session)s
                GROUP BY size
                HAVING size NOT IN('0')
                ORDER BY size
            ) DATA
        UNION
         SELECT COUNT(*)
         FROM (
          SELECT (
                    CASE 
                        WHEN s.capacity>=1 AND s.capacity >=10 AND s.enroll_capacity=0 THEN '1'   
                        WHEN s.capacity>=1 AND s.capacity >=30 AND s.enroll_capacity=0 THEN '21-30'  
                        WHEN s.capacity>=1 AND s.capacity >=35 AND s.enroll_capacity=0 THEN '30-35'  
                        WHEN s.capacity>=1 AND s.capacity >=40 AND s.enroll_capacity=0 THEN '36-40'  
                        WHEN s.capacity>=1 AND s.capacity >=50 AND s.enroll_capacity=0THEN '41-50'  
                        WHEN s.capacity>=1 AND s.capacity >=54 AND s.enroll_capacity=0THEN '51-54'  
                        WHEN s.capacity>=1 AND s.capacity >=64 AND s.enroll_capacity=0 THEN '55-64' 
                        WHEN s.capacity>=1 AND s.capacity >=124 AND s.enroll_capacity=0 THEN '65-124'
                        WHEN s.capacity>=1 AND s.capacity >=168 AND s.enroll_capacity=0 THEN'124-168' 

                        ELSE '0'

                    END

         )AS Available_Class

                FROM section_t AS s
                WHERE 
                    syear = %(year)s 
                    AND session_name = %(session)s
                
        ) M
        """ 
       
    val={
        "year" : str(year),
        "session" : session,
    }
    
    with connection.cursor() as cursor:
        cursor.execute( query , val)
       
    header = [ col[0] for col in cursor.description ]
    data = cursor.fetchall()  
    context = {
        'tableHeaders': header,
        'tableData'   : data,
        'years'       : years,
        'sessions'    : sessions,
        'selectedSession' : session,
        'selectedYear'    : year,
    }

    return render(request, 'Classroom_Requirement_Summary.html', context)
