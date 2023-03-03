import pickle 

student_names = ['a','b','c','d']

with open('student_file.pkl', 'wb') as f: 
    pickle.dump(student_names, f)# serialize the list
    f.close()
with open('student_file.pkl', 'rb') as f:

    student_names_loaded = pickle.load(f) # deserialize using load()
    print(student_names_loaded)