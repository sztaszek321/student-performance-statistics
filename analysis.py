from ucimlrepo import fetch_ucirepo

# fetch dataset 
student_performance = fetch_ucirepo(id=320)

# data (as pandas dataframes) 
X = student_performance.data.features #ATRIBUTES
y = student_performance.data.targets #GRADES(G1 - G3)

"""# metadata 
print(student_performance.metadata)

# variable information 
print(student_performance.variables)
"""

print(X.info())
print(y.info())
