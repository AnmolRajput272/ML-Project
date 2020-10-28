import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl


#Antecedent is used for input parameters and Consequent is used for output. Here ca,mte,ete are input and cgpa is output.
age=ctrl.Antecedent(np.arange(10,71,1),'age') #ca marks range 0-25
m_age=ctrl.Antecedent(np.arange(10,15,1),'m_age')
invaded_n=ctrl.Antecedent(np.arange(0,15,1),'invaded_n')
birads=ctrl.Antecedent(np.arange(0,5,0.1),'birads') #ete marks range 0-50
bcrisk=ctrl.Consequent(np.arange(0,101,1),'bcrisk') #cgpa between 0-10

#now we consider bad ca when marks are between 0-10, average when marks between 9-20 and good when marks between 18-25.

age['l']=fuzzy.trimf(age.universe,[0,15,20]) 
age['m']=fuzzy.trimf(age.universe,[20,30,45])
age['h']=fuzzy.trimf(age.universe,[45,60,70])

#now we consider bad mte when marks are between 0-10, average when marks between 9-20 and good when marks between 18-25.


birads['l']=fuzzy.trimf(birads.universe,[0,0.75,1.3])
birads['m']=fuzzy.trimf(birads.universe,[1.3,2,2.8])
birads['h']=fuzzy.trimf(birads.universe,[2.8,4,5])

#now we consider bad cgpa when marks are between 0-5, average when marks between 4-7.5 and good when marks between 7-10.

bcrisk['l']=fuzzy.trimf(bcrisk.universe,[0,16,33.3])
bcrisk['m']=fuzzy.trimf(bcrisk.universe,[25,49,66.6])
bcrisk['h']=fuzzy.trimf(bcrisk.universe,[59,82,100])
#now we will decide rules based on creteria of ca, mte and ete.


m_age['l']=fuzzy.trimf(m_age.universe,[10,10.75,11.75]) 
m_age['m']=fuzzy.trimf(m_age.universe,[11.75,12.5,13.25])
m_age['h']=fuzzy.trimf(m_age.universe,[13.25,14,15])

invaded_n['l']=fuzzy.trimf(invaded_n.universe,[0,2.5,5])
invaded_n['m']=fuzzy.trimf(invaded_n.universe,[4,7.5,10])
invaded_n['h']=fuzzy.trimf(invaded_n.universe,[9,13.5,15])


rule1=ctrl.Rule(age['l'] & birads['l'],bcrisk['l'])
rule2=ctrl.Rule(age['m'] & birads['m'],bcrisk['m'])
rule3=ctrl.Rule(age['m'] & birads['h'],bcrisk['h'])
rule4=ctrl.Rule(age['l']  & birads['h'],bcrisk['h'])
rule5=ctrl.Rule(age['h']  & birads['h'],bcrisk['h'])
rule6=ctrl.Rule(age['h'] & birads['h'],bcrisk['h'])
rule7=ctrl.Rule(age['l'] & birads['h'],bcrisk['h'])
rule8=ctrl.Rule(age['m'] & birads['l'],bcrisk['l'])
rule9=ctrl.Rule(age['m']  & birads['h'],bcrisk['h'])
rule10=ctrl.Rule(age['h'] & birads['l'],bcrisk['l'])
#pass the value to ControlSystem and Simulate before calculating actual output.

cg_calc=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10])
cgpaa=ctrl.ControlSystemSimulation(cg_calc)

rule11=ctrl.Rule(m_age['l'] & birads['l'],bcrisk['l'])
rule12=ctrl.Rule(m_age['m'] & birads['m'],bcrisk['m'])
rule13=ctrl.Rule(m_age['m'] & birads['h'],bcrisk['h'])
rule14=ctrl.Rule(m_age['l']  & birads['h'],bcrisk['h'])
rule15=ctrl.Rule(m_age['h']  & birads['h'],bcrisk['m'])
rule16=ctrl.Rule(m_age['h'] & birads['h'],bcrisk['l'])
rule17=ctrl.Rule(m_age['l'] & birads['h'],bcrisk['l'])
rule18=ctrl.Rule(m_age['m'] & birads['l'],bcrisk['l'])
rule19=ctrl.Rule(m_age['m']  & birads['h'],bcrisk['h'])
rule20=ctrl.Rule(m_age['h'] & birads['l'],bcrisk['l'])
#pass the value to ControlSystem and Simulate before calculating actual output.

cg_calc1=ctrl.ControlSystem([rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20])
cgpaa1=ctrl.ControlSystemSimulation(cg_calc1)

rule21=ctrl.Rule(invaded_n['l'] & birads['l'],bcrisk['l'])
rule22=ctrl.Rule(invaded_n['m'] & birads['m'],bcrisk['m'])
rule23=ctrl.Rule(invaded_n['m'] & birads['h'],bcrisk['h'])
rule24=ctrl.Rule(invaded_n['l']  & birads['h'],bcrisk['h'])
rule25=ctrl.Rule(invaded_n['h']  & birads['h'],bcrisk['m'])
rule26=ctrl.Rule(invaded_n['h'] & birads['h'],bcrisk['l'])
rule27=ctrl.Rule(invaded_n['l'] & birads['h'],bcrisk['l'])
rule28=ctrl.Rule(invaded_n['h'] & birads['h'],bcrisk['h'])
rule29=ctrl.Rule(invaded_n['m']  & birads['h'],bcrisk['h'])
rule30=ctrl.Rule(invaded_n['h'] & birads['l'],bcrisk['l'])
#pass the value to ControlSystem and Simulate before calculating actual output.

cg_calc2=ctrl.ControlSystem([rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30])
cgpaa2=ctrl.ControlSystemSimulation(cg_calc2)

#Now pass input as 
cgpaa.input['age']=30
cgpaa.input['birads']=cgpaa1.input['birads']=cgpaa.input['birads']=1.2
cgpaa1.input['m_age']=11
cgpaa2.input['invaded_n']=12

cgpaa.compute() #calculate cgpa
