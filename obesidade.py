import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl



#Variaveis de Entrada (Antecedent)
comer = ctrl.Antecedent(np.arange(0, 11, 1), 'comer') #Comer
exercicio = ctrl.Antecedent(np.arange(0, 11, 1), 'exercicio') #Tempo para Ex

#Variaveis de saída (Consequent)
peso = ctrl.Consequent(np.arange(0, 100, 1), 'peso')

comer.automf(names=['pouco','razoavel','muito'])
exercicio.automf(names=['pouco','medio','muito'])


# atribuicao sem o automf
peso['leve'] = fuzz.trapmf(peso.universe, [0,20,30,50])
peso['medio'] = fuzz.trapmf(peso.universe, [25,45,55,75])
peso['pesado'] = fuzz.trapmf(peso.universe, [50,70,80,100])


#Visualizando as variáveis

comer.view()
exercicio.view()
peso.view()

#Criando as regras
regra_1 = ctrl.Rule(comer['pouco'] & exercicio['muito'], peso['leve'])
regra_2 = ctrl.Rule(comer['pouco'] & exercicio['pouco'], peso['leve'])
regra_3 = ctrl.Rule(comer['razoavel'] & exercicio['muito'], peso['leve'])
regra_4 = ctrl.Rule(comer['muito'] & exercicio['muito'], peso['medio'])
regra_5 = ctrl.Rule(comer['muito'] & exercicio['pouco'], peso['pesado'])
regra_6 = ctrl.Rule(comer['razoavel'] & exercicio['medio'], peso['medio'])

controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3, regra_4, regra_5, regra_6])


#Simulando
CalculoPeso = ctrl.ControlSystemSimulation(controlador)

#notaComer = x
#notaexercicio= x
notaComer = int(input('Comer: '))
notaexercicio = int(input('exercicio: '))
CalculoPeso.input['comer'] = notaComer
CalculoPeso.input['exercicio'] = notaexercicio
CalculoPeso.compute()

valorPeso = CalculoPeso.output['peso']

print("\nComer %d \nexercicio: %d\nPeso de %5.2f" %(
        notaComer,
        notaexercicio,
        valorPeso))



comer.view(sim=CalculoPeso)
exercicio.view(sim=CalculoPeso)
peso.view(sim=CalculoPeso)

plt.show()