import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl


age=ctrl.Antecedent(np.arange(10,71,1),'age') 
m_age=ctrl.Antecedent(np.arange(10,15,1),'m_age')
invaded_n=ctrl.Antecedent(np.arange(0,15,1),'invaded_n')
birads=ctrl.Antecedent(np.arange(0,5,1),'birads') 
bcrisk=ctrl.Consequent(np.arange(0,101,1),'bcrisk') 

age['l']=fuzzy.trimf(age.universe,[0,15,20]) 
age['m']=fuzzy.trimf(age.universe,[20,45,45])
age['h']=fuzzy.trimf(age.universe,[45,70,70])

birads['l']=fuzzy.trimf(birads.universe,[0,1.25,2.5])
birads['m']=fuzzy.trimf(birads.universe,[2,3,3.5])
birads['h']=fuzzy.trimf(birads.universe,[3.25,4.2,5])

bcrisk['l']=fuzzy.trimf(bcrisk.universe,[0,16,33.3])
bcrisk['m']=fuzzy.trimf(bcrisk.universe,[25,49,66.6])
bcrisk['h']=fuzzy.trimf(bcrisk.universe,[60,82,100])

m_age['l']=fuzzy.trimf(m_age.universe,[10,10.75,11.75]) 
m_age['m']=fuzzy.trimf(m_age.universe,[11.5,12.5,13.25])
m_age['h']=fuzzy.trimf(m_age.universe,[13,15,15])

invaded_n['l']=fuzzy.trimf(invaded_n.universe,[0,3,5])
invaded_n['m']=fuzzy.trimf(invaded_n.universe,[4,8,11])
invaded_n['h']=fuzzy.trimf(invaded_n.universe,[10,15,15])


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

cg_calc=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10])
cgpaa=ctrl.ControlSystemSimulation(cg_calc)

rule11=ctrl.Rule(m_age['l'] & birads['l'],bcrisk['l'])
rule12=ctrl.Rule(m_age['m'] & birads['m'],bcrisk['m'])
rule13=ctrl.Rule(m_age['h'] & birads['h'],bcrisk['h'])
rule14=ctrl.Rule(m_age['l']  & birads['h'],bcrisk['h'])
rule15=ctrl.Rule(m_age['h']  & birads['m'],bcrisk['m'])
rule16=ctrl.Rule(m_age['h'] & birads['h'],bcrisk['h'])
rule17=ctrl.Rule(m_age['l'] & birads['m'],bcrisk['m'])
rule18=ctrl.Rule(m_age['m'] & birads['l'],bcrisk['l'])
rule19=ctrl.Rule(m_age['m']  & birads['h'],bcrisk['h'])
rule20=ctrl.Rule(m_age['h'] & birads['l'],bcrisk['l'])

cg_calc1=ctrl.ControlSystem([rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20])
cgpaa1=ctrl.ControlSystemSimulation(cg_calc1)

rule21=ctrl.Rule(invaded_n['l'] & birads['l'],bcrisk['l'])
rule22=ctrl.Rule(invaded_n['m'] & birads['m'],bcrisk['m'])
rule23=ctrl.Rule(invaded_n['h'] & birads['h'],bcrisk['h'])
rule24=ctrl.Rule(invaded_n['l']  & birads['h'],bcrisk['h'])
rule25=ctrl.Rule(invaded_n['l']  & birads['m'],bcrisk['l'])
rule26=ctrl.Rule(invaded_n['m'] & birads['l'],bcrisk['l'])
rule27=ctrl.Rule(invaded_n['m'] & birads['h'],bcrisk['h'])
rule28=ctrl.Rule(invaded_n['h'] & birads['l'],bcrisk['l'])
rule29=ctrl.Rule(invaded_n['h']  & birads['m'],bcrisk['h'])
rule30=ctrl.Rule(invaded_n['h'] & birads['l'],bcrisk['l'])

cg_calc2=ctrl.ControlSystem([rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30])
cgpaa2=ctrl.ControlSystemSimulation(cg_calc2)



patient1 = {'age':30, 'birads':4, "m_age":11, 'invaded_n':7}
patient2 = {'age':25, 'birads':3, "m_age":12, 'invaded_n':12}
patient3 = {'age':77, 'birads':1.2, "m_age":12.5, 'invaded_n':9}
patient4 = {'age':36, 'birads':4.5, "m_age":13, 'invaded_n':4}
patient5 = {'age':51, 'birads':3.5, "m_age":10.5, 'invaded_n':6}
patient6 = {'age':14, 'birads':2.7, "m_age":14, 'invaded_n':14}
patient7 = {'age':19, 'birads':1.9, "m_age":13, 'invaded_n':11}
patient8 = {'age':42, 'birads':1.5, "m_age":15, 'invaded_n':8}
patient9 = {'age':67, 'birads':5, "m_age":11.5, 'invaded_n':9}
patient10 = {'age':55, 'birads':2.5, "m_age":12, 'invaded_n':10}

patients = [patient1,patient2,patient3,patient4,patient5,patient6,patient7,patient8,patient9,patient10]

for patient in patients:

    cgpaa.input['age']=patient['age']
    cgpaa.input['birads']=cgpaa1.input['birads']=cgpaa.input['birads']= patient['birads']
    cgpaa1.input['m_age']=patient['m_age']
    cgpaa2.input['invaded_n']=patient['invaded_n']
    
    cgpaa.compute()
    cgpaa1.compute()
    cgpaa2.compute()
    
    stat1=cgpaa.output['bcrisk']
    stat2=cgpaa1.output['bcrisk']
    stat3=cgpaa2.output['bcrisk']
    
    result = ((stat1+stat2+stat3))/3
