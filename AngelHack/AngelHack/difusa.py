
# coding: utf-8

# In[2]:

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# In[ ]:




# In[3]:

def fuzzy():
    horas = ctrl.Antecedent([0, 15, 25, 35, 45, 55, 65, 55, 75, 85, 100], 'horas')
    tareas = ctrl.Antecedent([0, 1, 2, 4, 5, 8, 9, 12, 13, 15], 'tareas')
    nivel = ctrl.Antecedent([0, 1.5, 2.5, 4.5, 5.5, 6.5, 7.5, 8.5, 10], 'nivel')
    # cambiar las entradas a interpolacion lineal
    multiplicador = ctrl.Consequent(np.arange(0, 11, 1), 'multiplicador')

    horas['a'] = fuzz.trapmf(horas.universe,
                                              [0, 0, 15, 25])
    horas['b'] = fuzz.trapmf(horas.universe,
                                                     [15, 25, 35, 45])
    horas['c'] = fuzz.trapmf(horas.universe,
                                                [35, 45, 55, 65])
    horas['d'] = fuzz.trapmf(horas.universe,
                                                [55, 65, 75, 85])
    horas['e'] = fuzz.trapmf(horas.universe,
                                                 [75, 85, 100, 100])

    tareas['a'] = fuzz.trapmf(tareas.universe, [0, 0, 1, 2])
    tareas['b'] = fuzz.trapmf(tareas.universe, [1, 2, 4, 5])
    tareas['c'] = fuzz.trapmf(tareas.universe, [4, 5, 8, 9])
    tareas['d'] = fuzz.trapmf(tareas.universe, [8, 9, 12, 13])
    tareas['e'] = fuzz.trapmf(tareas.universe, [12, 13, 15, 15]
                                         )

    nivel['a'] = fuzz.trapmf(nivel.universe, [0, 0, 1.5, 2.5])
    nivel['b'] = fuzz.trapmf(nivel.universe, [1.5, 2.5, 3.5, 4.5])
    nivel['c'] = fuzz.trapmf(nivel.universe, [3.5, 4.5, 5.5, 6.5])
    nivel['d'] = fuzz.trapmf(nivel.universe, [5.5, 6.5, 7.5, 8.5])
    nivel['e'] = fuzz.trapmf(nivel.universe, [7.5, 8.5, 10, 10])

    multiplicador['a'] = fuzz.trapmf(multiplicador.universe, [0, 0, 1, 1.5])
    multiplicador['b'] = fuzz.trapmf(multiplicador.universe, [1, 1.5, 2.5, 3])
    multiplicador['c'] = fuzz.trapmf(multiplicador.universe, [2.5, 3, 4, 4.5])
    multiplicador['d'] = fuzz.trapmf(multiplicador.universe, [4, 4.5, 5.5, 6])
    multiplicador['e'] = fuzz.trapmf(multiplicador.universe, [5.5, 6, 7, 7.5])
    multiplicador['f'] = fuzz.trapmf(multiplicador.universe, [7, 7.5, 8.5, 9])
    multiplicador['g'] = fuzz.trapmf(multiplicador.universe, [8.5, 9, 10, 10])


    ReglaNivel1 = ctrl.Rule(
        horas
    ['a'] & tareas['a'] & nivel['a'],
        multiplicador['a'])
    ReglaNivel2 = ctrl.Rule(
        horas
    ['a'] & tareas['a'] & nivel['b'],
        multiplicador['a'])
    ReglaNivel3 = ctrl.Rule(
        horas
    ['a'] & tareas['a'] & nivel['c'],
        multiplicador['a'])
    ReglaNivel4 = ctrl.Rule(
        horas
    ['a'] & tareas['a'] & nivel['d'],
        multiplicador['a'])
    ReglaNivel5 = ctrl.Rule(
        horas
    ['a'] & tareas['a'] & nivel['e'],
        multiplicador['a'])
    ReglaNivel6 = ctrl.Rule(
        horas
    ['a'] & tareas['b'] & nivel['a'],
        multiplicador['a'])
    ReglaNivel7 = ctrl.Rule(
        horas
    ['a'] & tareas['b'] & nivel['b'],
        multiplicador['a'])
    ReglaNivel8 = ctrl.Rule(
        horas
    ['a'] & tareas['b'] & nivel['c'],
        multiplicador['a'])
    ReglaNivel9 = ctrl.Rule(
        horas
    ['a'] & tareas['b'] & nivel['d'],
        multiplicador['a'])
    ReglaNivel10 = ctrl.Rule(
        horas
    ['a'] & tareas['b'] & nivel['e'],
        multiplicador['a'])
    ReglaNivel11 = ctrl.Rule(
        horas
    ['a'] & tareas['c'] & nivel['a'],
        multiplicador['a'])
    ReglaNivel12 = ctrl.Rule(
        horas
    ['a'] & tareas['c'] & nivel['b'],
        multiplicador['a'])
    ReglaNivel13 = ctrl.Rule(
        horas
    ['a'] & tareas['c'] & nivel['c'],
        multiplicador['a'])
    ReglaNivel14 = ctrl.Rule(
        horas
    ['a'] & tareas['c'] & nivel['d'],
        multiplicador['b'])
    ReglaNivel15 = ctrl.Rule(
        horas
    ['a'] & tareas['c'] & nivel['e'],
        multiplicador['b'])
    ReglaNivel16 = ctrl.Rule(
        horas
    ['a'] & tareas['d'] & nivel['a'],
        multiplicador['b'])
    ReglaNivel17 = ctrl.Rule(
        horas
    ['a'] & tareas['d'] & nivel['b'],
        multiplicador['b'])
    ReglaNivel18 = ctrl.Rule(
        horas
    ['a'] & tareas['d'] & nivel['c'],
        multiplicador['b'])
    ReglaNivel19 = ctrl.Rule(
        horas
    ['a'] & tareas['d'] & nivel['d'],
        multiplicador['b'])
    ReglaNivel20 = ctrl.Rule(
        horas
    ['a'] & tareas['d'] & nivel['e'],
        multiplicador['c'])
    ReglaNivel21 = ctrl.Rule(
        horas
    ['a'] & tareas['e'] & nivel['a'],
        multiplicador['b'])
    ReglaNivel22 = ctrl.Rule(
        horas
    ['a'] & tareas['e'] & nivel['b'],
        multiplicador['b'])
    ReglaNivel23 = ctrl.Rule(
        horas
    ['a'] & tareas['e'] & nivel['c'],
        multiplicador['c'])
    ReglaNivel24 = ctrl.Rule(
        horas
    ['a'] & tareas['e'] & nivel['d'],
        multiplicador['c'])
    ReglaNivel25 = ctrl.Rule(
        horas
    ['a'] & tareas['e'] & nivel['e'],
        multiplicador['c'])
    ReglaNivel26 = ctrl.Rule(
        horas
    ['b'] & tareas['a'] & nivel[
            'a'], multiplicador['a'])
    ReglaNivel27 = ctrl.Rule(
        horas
    ['b'] & tareas['a'] & nivel[
            'b'], multiplicador['a'])
    ReglaNivel28 = ctrl.Rule(
        horas
    ['b'] & tareas['a'] & nivel[
            'c'], multiplicador['a'])
    ReglaNivel29 = ctrl.Rule(
        horas
    ['b'] & tareas['a'] & nivel[
            'd'], multiplicador['b'])
    ReglaNivel30 = ctrl.Rule(
        horas
    ['b'] & tareas['a'] & nivel[
            'e'], multiplicador['b'])
    ReglaNivel31 = ctrl.Rule(
        horas
    ['b'] & tareas['b'] & nivel[
            'a'], multiplicador['b'])
    ReglaNivel32 = ctrl.Rule(
        horas
    ['b'] & tareas['b'] & nivel[
            'b'], multiplicador['b'])
    ReglaNivel33 = ctrl.Rule(
        horas
    ['b'] & tareas['b'] & nivel[
            'c'], multiplicador['b'])
    ReglaNivel34 = ctrl.Rule(
        horas
    ['b'] & tareas['b'] & nivel[
            'd'], multiplicador['b'])
    ReglaNivel35 = ctrl.Rule(
        horas
    ['b'] & tareas['b'] & nivel[
            'e'], multiplicador['c'])
    ReglaNivel36 = ctrl.Rule(
        horas
    ['b'] & tareas['c'] & nivel[
            'a'], multiplicador['b'])
    ReglaNivel37 = ctrl.Rule(
        horas
    ['b'] & tareas['c'] & nivel[
            'b'], multiplicador['b'])
    ReglaNivel38 = ctrl.Rule(
        horas
    ['b'] & tareas['c'] & nivel[
            'c'], multiplicador['c'])
    ReglaNivel39 = ctrl.Rule(
        horas
    ['b'] & tareas['c'] & nivel[
            'd'], multiplicador['c'])
    ReglaNivel40 = ctrl.Rule(
        horas
    ['b'] & tareas['c'] & nivel[
            'e'], multiplicador['c'])
    ReglaNivel41 = ctrl.Rule(
        horas
    ['b'] & tareas['d'] & nivel[
            'a'], multiplicador['c'])
    ReglaNivel42 = ctrl.Rule(
        horas
    ['b'] & tareas['d'] & nivel[
            'b'], multiplicador['c'])
    ReglaNivel43 = ctrl.Rule(
        horas
    ['b'] & tareas['d'] & nivel[
            'c'], multiplicador['c'])
    ReglaNivel44 = ctrl.Rule(
        horas
    ['b'] & tareas['d'] & nivel[
            'd'], multiplicador['c'])
    ReglaNivel45 = ctrl.Rule(
        horas
    ['b'] & tareas['d'] & nivel[
            'e'], multiplicador['d'])
    ReglaNivel46 = ctrl.Rule(
        horas
    ['b'] & tareas['e'] & nivel[
            'a'], multiplicador['c'])
    ReglaNivel47 = ctrl.Rule(
        horas
    ['b'] & tareas['e'] & nivel[
            'b'], multiplicador['d'])
    ReglaNivel48 = ctrl.Rule(
        horas
    ['b'] & tareas['e'] & nivel[
            'c'], multiplicador['d'])
    ReglaNivel49 = ctrl.Rule(
        horas
    ['b'] & tareas['e'] & nivel[
            'd'], multiplicador['d'])
    ReglaNivel50 = ctrl.Rule(
        horas
    ['b'] & tareas['e'] & nivel[
            'e'], multiplicador['d'])
    ReglaNivel51 = ctrl.Rule(
        horas
    ['c'] & tareas['a'] & nivel['a'],
        multiplicador['b'])
    ReglaNivel52 = ctrl.Rule(
        horas
    ['c'] & tareas['a'] & nivel['b'],
        multiplicador['b'])
    ReglaNivel53 = ctrl.Rule(
        horas
    ['c'] & tareas['a'] & nivel['c'],
        multiplicador['b'])
    ReglaNivel54 = ctrl.Rule(
        horas
    ['c'] & tareas['a'] & nivel['d'],
        multiplicador['b'])
    ReglaNivel55 = ctrl.Rule(
        horas
    ['c'] & tareas['a'] & nivel['e'],
        multiplicador['b'])
    ReglaNivel56 = ctrl.Rule(
        horas
    ['c'] & tareas['b'] & nivel['a'],
        multiplicador['b'])
    ReglaNivel57 = ctrl.Rule(
        horas
    ['c'] & tareas['b'] & nivel['b'],
        multiplicador['b'])
    ReglaNivel58 = ctrl.Rule(
        horas
    ['c'] & tareas['b'] & nivel['c'],
        multiplicador['b'])
    ReglaNivel59 = ctrl.Rule(
        horas
    ['c'] & tareas['b'] & nivel['d'],
        multiplicador['b'])
    ReglaNivel60 = ctrl.Rule(
        horas
    ['c'] & tareas['b'] & nivel['e'],
        multiplicador['c'])
    ReglaNivel61 = ctrl.Rule(
        horas
    ['c'] & tareas['c'] & nivel['a'],
        multiplicador['c'])
    ReglaNivel62 = ctrl.Rule(
        horas
    ['c'] & tareas['c'] & nivel['b'],
        multiplicador['c'])
    ReglaNivel63 = ctrl.Rule(
        horas
    ['c'] & tareas['c'] & nivel['c'],
        multiplicador['c'])
    ReglaNivel64 = ctrl.Rule(
        horas
    ['c'] & tareas['c'] & nivel['d'],
        multiplicador['d'])
    ReglaNivel65 = ctrl.Rule(
        horas
    ['c'] & tareas['c'] & nivel['e'],
        multiplicador['d'])
    ReglaNivel66 = ctrl.Rule(
        horas
    ['c'] & tareas['d'] & nivel['a'],
        multiplicador['d'])
    ReglaNivel67 = ctrl.Rule(
        horas
    ['c'] & tareas['d'] & nivel['b'],
        multiplicador['d'])
    ReglaNivel68 = ctrl.Rule(
        horas
    ['c'] & tareas['d'] & nivel['c'],
        multiplicador['d'])
    ReglaNivel69 = ctrl.Rule(
        horas
    ['c'] & tareas['d'] & nivel['d'],
        multiplicador['e'])
    ReglaNivel70 = ctrl.Rule(
        horas
    ['c'] & tareas['d'] & nivel['e'],
        multiplicador['e'])
    ReglaNivel71 = ctrl.Rule(
        horas
    ['c'] & tareas['e'] & nivel['a'],
        multiplicador['d'])
    ReglaNivel72 = ctrl.Rule(
        horas
    ['c'] & tareas['e'] & nivel['b'],
        multiplicador['e'])
    ReglaNivel73 = ctrl.Rule(
        horas
    ['c'] & tareas['e'] & nivel['c'],
        multiplicador['e'])
    ReglaNivel74 = ctrl.Rule(
        horas
    ['c'] & tareas['e'] & nivel['d'],
        multiplicador['e'])
    ReglaNivel75 = ctrl.Rule(
        horas
    ['c'] & tareas['e'] & nivel['e'],
        multiplicador['e'])
    ReglaNivel76 = ctrl.Rule(
        horas
    ['d'] & tareas['a'] & nivel['a'],
        multiplicador['b'])
    ReglaNivel77 = ctrl.Rule(
        horas
    ['d'] & tareas['a'] & nivel['b'],
        multiplicador['b'])
    ReglaNivel78 = ctrl.Rule(
        horas
    ['d'] & tareas['a'] & nivel['c'],
        multiplicador['b'])
    ReglaNivel79 = ctrl.Rule(
        horas
    ['d'] & tareas['a'] & nivel['d'],
        multiplicador['b'])
    ReglaNivel80 = ctrl.Rule(
        horas
    ['d'] & tareas['a'] & nivel['e'],
        multiplicador['b'])
    ReglaNivel81 = ctrl.Rule(
        horas
    ['d'] & tareas['b'] & nivel['a'],
        multiplicador['b'])
    ReglaNivel82 = ctrl.Rule(
        horas
    ['d'] & tareas['b'] & nivel['b'],
        multiplicador['c'])
    ReglaNivel83 = ctrl.Rule(
        horas
    ['d'] & tareas['b'] & nivel['c'],
        multiplicador['c'])
    ReglaNivel84 = ctrl.Rule(
        horas
    ['d'] & tareas['b'] & nivel['d'],
        multiplicador['c'])
    ReglaNivel85 = ctrl.Rule(
        horas
    ['d'] & tareas['b'] & nivel['e'],
        multiplicador['d'])
    ReglaNivel86 = ctrl.Rule(
        horas
    ['d'] & tareas['c'] & nivel['a'],
        multiplicador['d'])
    ReglaNivel87 = ctrl.Rule(
        horas
    ['d'] & tareas['c'] & nivel['b'],
        multiplicador['d'])
    ReglaNivel88 = ctrl.Rule(
        horas
    ['d'] & tareas['c'] & nivel['c'],
        multiplicador['e'])
    ReglaNivel89 = ctrl.Rule(
        horas
    ['d'] & tareas['c'] & nivel['d'],
        multiplicador['e'])
    ReglaNivel90 = ctrl.Rule(
        horas
    ['d'] & tareas['c'] & nivel['e'],
        multiplicador['e'])
    ReglaNivel91 = ctrl.Rule(
        horas
    ['d'] & tareas['d'] & nivel['a'],
        multiplicador['e'])
    ReglaNivel92 = ctrl.Rule(
        horas
    ['d'] & tareas['d'] & nivel['b'],
        multiplicador['e'])
    ReglaNivel93 = ctrl.Rule(
        horas
    ['d'] & tareas['d'] & nivel['c'],
        multiplicador['f'])
    ReglaNivel94 = ctrl.Rule(
        horas
    ['d'] & tareas['d'] & nivel['d'],
        multiplicador['f'])
    ReglaNivel95 = ctrl.Rule(
        horas
    ['d'] & tareas['d'] & nivel['e'],
        multiplicador['f'])
    ReglaNivel96 = ctrl.Rule(
        horas
    ['d'] & tareas['e'] & nivel['a'],
        multiplicador['f'])
    ReglaNivel97 = ctrl.Rule(
        horas
    ['d'] & tareas['e'] & nivel['b'],
        multiplicador['f'])
    ReglaNivel98 = ctrl.Rule(
        horas
    ['d'] & tareas['e'] & nivel['c'],
        multiplicador['g'])
    ReglaNivel99 = ctrl.Rule(
        horas
    ['d'] & tareas['e'] & nivel['d'],
        multiplicador['g'])
    ReglaNivel100 = ctrl.Rule(
        horas
    ['d'] & tareas['e'] & nivel['e'],
        multiplicador['g'])
    ReglaNivel101 = ctrl.Rule(
        horas
    ['e'] & tareas['a'] & nivel[
            'a'], multiplicador['b'])
    ReglaNivel102 = ctrl.Rule(
        horas
    ['e'] & tareas['a'] & nivel['b'],
        multiplicador['b'])
    ReglaNivel103 = ctrl.Rule(
        horas
    ['e'] & tareas['a'] & nivel['c'],
        multiplicador['b'])
    ReglaNivel104 = ctrl.Rule(
        horas
    ['e'] & tareas['a'] & nivel['d'],
        multiplicador['c'])
    ReglaNivel105 = ctrl.Rule(
        horas
    ['e'] & tareas['a'] & nivel[
            'e'], multiplicador['c'])
    ReglaNivel106 = ctrl.Rule(
        horas
    ['e'] & tareas['b'] & nivel['a'],
        multiplicador['b'])
    ReglaNivel107 = ctrl.Rule(
        horas
    ['e'] & tareas['b'] & nivel['b'],
        multiplicador['c'])
    ReglaNivel108 = ctrl.Rule(
        horas
    ['e'] & tareas['b'] & nivel['c'],
        multiplicador['c'])
    ReglaNivel109 = ctrl.Rule(
        horas
    ['e'] & tareas['b'] & nivel['d'],
        multiplicador['c'])
    ReglaNivel110 = ctrl.Rule(
        horas
    ['e'] & tareas['b'] & nivel['e'],
        multiplicador['d'])
    ReglaNivel111 = ctrl.Rule(
        horas
    ['e'] & tareas['c'] & nivel['a'],
        multiplicador['d'])
    ReglaNivel112 = ctrl.Rule(
        horas
    ['e'] & tareas['c'] & nivel['b'],
        multiplicador['e'])
    ReglaNivel113 = ctrl.Rule(
        horas
    ['e'] & tareas['c'] & nivel['c'],
        multiplicador['e'])
    ReglaNivel114 = ctrl.Rule(
        horas
    ['e'] & tareas['c'] & nivel['d'],
        multiplicador['e'])
    ReglaNivel115 = ctrl.Rule(
        horas
    ['e'] & tareas['c'] & nivel['e'],
        multiplicador['f'])
    ReglaNivel116 = ctrl.Rule(
        horas
    ['e'] & tareas['d'] & nivel['a'],
        multiplicador['e'])
    ReglaNivel117 = ctrl.Rule(
        horas
    ['e'] & tareas['d'] & nivel['b'],
        multiplicador['f'])
    ReglaNivel118 = ctrl.Rule(
        horas
    ['e'] & tareas['d'] & nivel['c'],
        multiplicador['f'])
    ReglaNivel119 = ctrl.Rule(
        horas
    ['e'] & tareas['d'] & nivel['d'],
        multiplicador['g'])
    ReglaNivel120 = ctrl.Rule(
        horas
    ['e'] & tareas['d'] & nivel['e'],
        multiplicador['g'])
    ReglaNivel121 = ctrl.Rule(
        horas
    ['e'] & tareas['e'] & nivel[
            'a'], multiplicador['f'])
    ReglaNivel122 = ctrl.Rule(
        horas
    ['e'] & tareas['e'] & nivel['b'],
        multiplicador['g'])
    ReglaNivel123 = ctrl.Rule(
        horas
    ['e'] & tareas['e'] & nivel['c'],
        multiplicador['g'])
    ReglaNivel124 = ctrl.Rule(
        horas
    ['e'] & tareas['e'] & nivel['d'],
        multiplicador['g'])
    ReglaNivel125 = ctrl.Rule(
        horas
    ['e'] & tareas['e'] & nivel[
            'e'], multiplicador['g'])

    ReglasNivel = ctrl.ControlSystem([ReglaNivel1, ReglaNivel2, ReglaNivel3, ReglaNivel4,
                   ReglaNivel5,
                   ReglaNivel6, ReglaNivel7, ReglaNivel8, ReglaNivel9,
                   ReglaNivel10,
                   ReglaNivel11, ReglaNivel12, ReglaNivel13, ReglaNivel14,
                   ReglaNivel15,
                   ReglaNivel16, ReglaNivel17, ReglaNivel18, ReglaNivel19,
                   ReglaNivel20,
                   ReglaNivel21, ReglaNivel22, ReglaNivel23, ReglaNivel24,
                   ReglaNivel25,
                   ReglaNivel26, ReglaNivel27, ReglaNivel28, ReglaNivel29,
                   ReglaNivel30,
                   ReglaNivel31, ReglaNivel32, ReglaNivel33, ReglaNivel34,
                   ReglaNivel35,
                   ReglaNivel36, ReglaNivel37, ReglaNivel38, ReglaNivel39,
                   ReglaNivel40,
                   ReglaNivel41, ReglaNivel42, ReglaNivel43, ReglaNivel44,
                   ReglaNivel45,
                   ReglaNivel46, ReglaNivel47, ReglaNivel48, ReglaNivel49,
                   ReglaNivel50,
                   ReglaNivel51, ReglaNivel52, ReglaNivel53, ReglaNivel54,
                   ReglaNivel55,
                   ReglaNivel56, ReglaNivel57, ReglaNivel58, ReglaNivel59,
                   ReglaNivel60,
                   ReglaNivel61, ReglaNivel62, ReglaNivel63, ReglaNivel64,
                   ReglaNivel65,
                   ReglaNivel66, ReglaNivel67, ReglaNivel68, ReglaNivel69,
                   ReglaNivel70,
                   ReglaNivel71, ReglaNivel72, ReglaNivel73, ReglaNivel74,
                   ReglaNivel75,
                   ReglaNivel76, ReglaNivel77, ReglaNivel78, ReglaNivel79,
                   ReglaNivel80,
                   ReglaNivel81, ReglaNivel82, ReglaNivel83, ReglaNivel84,
                   ReglaNivel85,
                   ReglaNivel86, ReglaNivel87, ReglaNivel88, ReglaNivel89,
                   ReglaNivel90,
                   ReglaNivel91, ReglaNivel92, ReglaNivel93, ReglaNivel94,
                   ReglaNivel95,
                   ReglaNivel96, ReglaNivel97, ReglaNivel98, ReglaNivel99,
                   ReglaNivel100,
                   ReglaNivel101, ReglaNivel102, ReglaNivel103, ReglaNivel104,
                   ReglaNivel105,
                   ReglaNivel106, ReglaNivel107, ReglaNivel108, ReglaNivel109,
                   ReglaNivel110,
                   ReglaNivel111, ReglaNivel112, ReglaNivel113, ReglaNivel114,
                   ReglaNivel115,
                   ReglaNivel116, ReglaNivel117, ReglaNivel118, ReglaNivel119,
                   ReglaNivel120,
                   ReglaNivel121, ReglaNivel122, ReglaNivel123, ReglaNivel124,
                   ReglaNivel125])

    return ctrl.ControlSystemSimulation(ReglasNivel)


# In[7]:

def calcula(horas, tareas, nivel, control):
    control.input['horas'] = horas
    control.input['tareas'] = tareas
    control.input['nivel'] = nivel
    control.compute()
    return control.output['multiplicador']


def cotizacion(c, t1, t2, t3, x, y, z, r):
    return (c*((t1*x)+(t2*y)+(t3*z))+r)*1000






