try:  
    d = 2
    a = d[1] 
    b = d.non_existing_field
        
except (KeyError, AttributeError) as e:   
    print("A KeyError or an AttributeError exception has been caught.")
    try:  
        d = {}
        a = d[1] 
        b = d.non_existing_field 
    except KeyError as e:
             print("A KeyError has occurred. Exception message:", e) 
    except AttributeError as e:   
             print("An AttributeError has occurred. Exception message:", e) 