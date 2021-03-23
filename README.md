# Fabric-test
    poll/ # GET, POST создать опросы
    GET{}
    POST{  
    "name": "name",
    "description": "description",
    "start_date": "2000-07-21T00:00",
    "end_date": "2045-07-21T00:00"
     }   

    poll/<int:pid>/ # PUT, DELETE, GET опрос
    GET{}
    DELETE{}
    PUT
    {   "name": "7",
    "description": "125",
    "end_date": "2044-07-21T00:00"
    } 
    

    poll/<int:pid>/question/  # POST Создать вопрос
    POST{   
    "text": "text"
    }   

    poll/<int:pid>/question/<int:qid>/  # GET PUT DELETE вопрос, # POST ответить на вопрос
    GET{}
    DELETE{}
    PUT{   
    "text": "text1"
    }   
    POST{   
    "choice_pk" : "1",
    "anon_id": 1234
     }   
                                                                                
    poll/<int:pid>/question/<int:qid>/post_choice/ # POST Создать ответ
    POST{   
    "text": "text2" 
    }
    answers/<int:anon_id>/  # GET узреть свои ответы
    anon_id Из эндпоинта выше

    api/token/ # POST simplejwt token
    POST{   
    "username": "YOURsuperuser",
    "password": "YOURpas"
    }   

    api/token/refresh/
    
