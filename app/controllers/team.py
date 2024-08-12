from app.models.tables import User, SkapAut, SkapElemec,SkapElet,SkapMec
from app.models.forms import SkapAutForm,SkapElemecForm,SkapEletForm,SkapMecForm,LoginForm, RegisterForm
import numpy as np
import pandas as pd
import json

def correcao(item,dataframe):
        dataframe = dataframe.get(item)
        resultado = dataframe.value_counts() 
        resultado = resultado.to_json(default_handler=str)
        resultado = resultado.replace("'", "\"")
        resultado = json.loads(resultado)
        try:
            if  resultado['0'] and resultado['1']:
                len_test = resultado['0'] + resultado['1']
                percent_zero = float(resultado['0'] / len_test)
                percent_zero = "{:.1f}".format(percent_zero*100)
                percent_um = float(resultado['1'] / len_test)
                percent_um = "{:.1f}".format(percent_um*100)
                return [percent_zero, percent_um]
        except:
                if not '0' in resultado:
                    percent_um = float(resultado['1']/resultado['1']*100)
                    percent_um = "{:.1f}".format(percent_um)
                    return [0, percent_um]
                if not '1' in resultado:
                    percent_zero = float(resultado['0']/resultado['0']*100)
                    percent_zero = "{:.1f}".format(percent_zero)
                    return [percent_zero, 0]
        else:
            return None

def Elet(i):
    if i:
        result_dict = [u.__dict__ for u in i]
        df_pie = pd.DataFrame(result_dict)
        df_pie= df_pie.drop(["_sa_instance_state","id","resultado","number_id","area","username","turno"], axis=1)
        q1 = correcao("q1",df_pie);q2 = correcao("q2",df_pie);q3 = correcao("q3",df_pie);q4 = correcao("q4",df_pie);q5 = correcao("q5",df_pie);q6 = correcao("q6",df_pie);q7 = correcao("q7",df_pie);q8 = correcao("q8",df_pie);q9 = correcao("q9",df_pie);q10 = correcao("q10",df_pie) 
        q11 = correcao("q11",df_pie);q12 = correcao("q12",df_pie);q13 = correcao("q13",df_pie);q14 = correcao("q14",df_pie);q15 = correcao("q15",df_pie);q16 = correcao("q16",df_pie);q17 = correcao("q17",df_pie);q18 = correcao("q18",df_pie);q19 = correcao("q19",df_pie);q20 = correcao("q20",df_pie) 
        q21 = correcao("q21",df_pie);q22 = correcao("q22",df_pie);q23 = correcao("q23",df_pie);q24 = correcao("q24",df_pie);q25 = correcao("q25",df_pie);q26 = correcao("q26",df_pie);q27 = correcao("q27",df_pie);q28 = correcao("q28",df_pie);q29 = correcao("q29",df_pie);q30 = correcao("q30",df_pie)
        q31 = correcao("q31",df_pie);q32 = correcao("q32",df_pie);q33 = correcao("q33",df_pie);q34 = correcao("q34",df_pie);q35 = correcao("q35",df_pie);q36 = correcao("q36",df_pie);q37 = correcao("q37",df_pie);q38 = correcao("q38",df_pie);q39 = correcao("q39",df_pie);q40 = correcao("q40",df_pie) 
        q41 = correcao("q41",df_pie);q42 = correcao("q42",df_pie);q43 = correcao("q43",df_pie);q44 = correcao("q44",df_pie);q45 = correcao("q45",df_pie);q46 = correcao("q46",df_pie);q47 = correcao("q47",df_pie);q48 = correcao("q48",df_pie);q49 = correcao("q49",df_pie);q50 = correcao("q50",df_pie) 
        q51 = correcao("q51",df_pie);q52 = correcao("q52",df_pie);q53 = correcao("q53",df_pie);q54 = correcao("q54",df_pie);q55 = correcao("q55",df_pie);q56 = correcao("q56",df_pie);q57 = correcao("q57",df_pie);q58 = correcao("q58",df_pie);q59 = correcao("q59",df_pie);q60 = correcao("q60",df_pie)
        q61 = correcao("q61",df_pie);q62 = correcao("q62",df_pie);q63 = correcao("q63",df_pie);q64 = correcao("q64",df_pie);q65 = correcao("q65",df_pie);q66 = correcao("q66",df_pie);q67 = correcao("q67",df_pie);q68 = correcao("q68",df_pie);q69 = correcao("q69",df_pie);q70 = correcao("q70",df_pie) 
        q71 = correcao("q71",df_pie);q72 = correcao("q72",df_pie);q73 = correcao("q73",df_pie);q74 = correcao("q74",df_pie);q75 = correcao("q75",df_pie);q76 = correcao("q76",df_pie);q77 = correcao("q77",df_pie);q78 = correcao("q78",df_pie);q79 = correcao("q79",df_pie);q80 = correcao("q80",df_pie) 
        q81 = correcao("q81",df_pie);q82 = correcao("q82",df_pie);q83 = correcao("q83",df_pie);q84 = correcao("q84",df_pie);q85 = correcao("q85",df_pie);q86 = correcao("q86",df_pie);q87 = correcao("q87",df_pie);q88 = correcao("q88",df_pie);q89 = correcao("q89",df_pie);q90 = correcao("q90",df_pie) 
        q91 = correcao("q91",df_pie);q92 = correcao("q92",df_pie);q93 = correcao("q93",df_pie);q94 = correcao("q94",df_pie);q95 = correcao("q95",df_pie);q96 = correcao("q96",df_pie);q97 = correcao("q97",df_pie);q98 = correcao("q98",df_pie);q99 = correcao("q99",df_pie);q100 = correcao("q100",df_pie)
        q101 = correcao("q101",df_pie);q102 = correcao("q102",df_pie);q103 = correcao("q103",df_pie);q104 = correcao("q104",df_pie);q105 = correcao("q105",df_pie);q106 = correcao("q106",df_pie);q107 = correcao("q107",df_pie);q108 = correcao("q108",df_pie);q109 = correcao("q109",df_pie);q110 = correcao("q110",df_pie)
        q111 = correcao("q111",df_pie);q112 = correcao("q112",df_pie)
        list_question = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33,q34,q35,q36,q37,q38,q39,q40,q41,q42,q43,q44,q45,q46,q47,q48,q49,q50,q51,q52,q53,q54,q55,q56,q57,q58,q59,q60,q61,q62,q63,q64,q65,q66,q67,q68,q69,q70,q71,q72,q73,q74,q75,q76,q77,q78,q79,q80,q81,q82,q83,q84,q85,q86,q87,q88,q89,q90,q91,q92,q93,q94,q95,q96,q97,q98,q99,q100,q101,q102,q103,q104,q105,q106,q107,q108,q109,q110,q111,q112]
        df_skap = pd.DataFrame(result_dict)
        df_skap_correct = df_skap.drop(["_sa_instance_state","id",
                                    "q1","q2","q3","q4","q5","q6","q7","q8","q9","q10",                                  
                                    "q11","q12","q13","q14","q15","q16","q17","q18","q19","q20",                                 
                                    "q21","q22","q23","q24","q25","q26","q27","q28","q29","q30",                                 
                                    "q31","q32","q33","q34","q35","q36","q37","q38","q39","q40",                                
                                    "q41","q42","q43","q44","q45","q46","q47","q48","q49","q50",                                
                                    "q51","q52","q53","q54","q55","q56","q57","q58","q59","q60",                                 
                                    "q61","q62","q63","q64","q65","q66","q67","q68","q69","q70",                                 
                                    "q71","q72","q73","q74","q75","q76","q77","q78","q79","q80",                                 
                                    "q81","q82","q83","q84","q85","q86","q87","q88","q89","q90",                                 
                                    "q91","q92","q93","q94","q95","q96","q97","q98","q99","q100",                                
                                    "q101","q102","q103","q104","q105","q106","q107","q108","q109","q110",
                                    "q111","q112"                       
                                    ], axis=1)
    else:
       df_skap_correct = pd.DataFrame({"Sem":0,"SKAP":4,"Preenchida":0,"No banco":4}, index=[0]) 
    
    return ([list_question,df_skap_correct])

def Aut(i):
    if i:
        result_dict = [u.__dict__ for u in i]
        df_pie = pd.DataFrame(result_dict)
        df_pie= df_pie.drop(["_sa_instance_state","id","resultado","number_id","area","username","turno"], axis=1)
        q1 = correcao("q1",df_pie);q2 = correcao("q2",df_pie);q3 = correcao("q3",df_pie);q4 = correcao("q4",df_pie);q5 = correcao("q5",df_pie);q6 = correcao("q6",df_pie);q7 = correcao("q7",df_pie);q8 = correcao("q8",df_pie);q9 = correcao("q9",df_pie);q10 = correcao("q10",df_pie) 
        q11 = correcao("q11",df_pie);q12 = correcao("q12",df_pie);q13 = correcao("q13",df_pie);q14 = correcao("q14",df_pie);q15 = correcao("q15",df_pie);q16 = correcao("q16",df_pie);q17 = correcao("q17",df_pie);q18 = correcao("q18",df_pie);q19 = correcao("q19",df_pie);q20 = correcao("q20",df_pie) 
        q21 = correcao("q21",df_pie);q22 = correcao("q22",df_pie);q23 = correcao("q23",df_pie);q24 = correcao("q24",df_pie);q25 = correcao("q25",df_pie);q26 = correcao("q26",df_pie);q27 = correcao("q27",df_pie);q28 = correcao("q28",df_pie);q29 = correcao("q29",df_pie);q30 = correcao("q30",df_pie)
        q31 = correcao("q31",df_pie);q32 = correcao("q32",df_pie);q33 = correcao("q33",df_pie);q34 = correcao("q34",df_pie);q35 = correcao("q35",df_pie);q36 = correcao("q36",df_pie);q37 = correcao("q37",df_pie);q38 = correcao("q38",df_pie);q39 = correcao("q39",df_pie);q40 = correcao("q40",df_pie) 
        q41 = correcao("q41",df_pie);q42 = correcao("q42",df_pie);q43 = correcao("q43",df_pie);q44 = correcao("q44",df_pie);q45 = correcao("q45",df_pie);q46 = correcao("q46",df_pie);q47 = correcao("q47",df_pie);q48 = correcao("q48",df_pie);q49 = correcao("q49",df_pie);q50 = correcao("q50",df_pie) 
        q51 = correcao("q51",df_pie);q52 = correcao("q52",df_pie);q53 = correcao("q53",df_pie);q54 = correcao("q54",df_pie);q55 = correcao("q55",df_pie);q56 = correcao("q56",df_pie);q57 = correcao("q57",df_pie);q58 = correcao("q58",df_pie);q59 = correcao("q59",df_pie);q60 = correcao("q60",df_pie)
        q61 = correcao("q61",df_pie);q62 = correcao("q62",df_pie);q63 = correcao("q63",df_pie);q64 = correcao("q64",df_pie);q65 = correcao("q65",df_pie);q66 = correcao("q66",df_pie);q67 = correcao("q67",df_pie);q68 = correcao("q68",df_pie);q69 = correcao("q69",df_pie);q70 = correcao("q70",df_pie) 
        q71 = correcao("q71",df_pie);q72 = correcao("q72",df_pie);q73 = correcao("q73",df_pie);q74 = correcao("q74",df_pie);q75 = correcao("q75",df_pie);q76 = correcao("q76",df_pie);q77 = correcao("q77",df_pie);q78 = correcao("q78",df_pie);q79 = correcao("q79",df_pie);q80 = correcao("q80",df_pie) 
        q81 = correcao("q81",df_pie);q82 = correcao("q82",df_pie);q83 = correcao("q83",df_pie);q84 = correcao("q84",df_pie);q85 = correcao("q85",df_pie);q86 = correcao("q86",df_pie);q87 = correcao("q87",df_pie);q88 = correcao("q88",df_pie);q89 = correcao("q89",df_pie);q90 = correcao("q90",df_pie) 
        q91 = correcao("q91",df_pie);q92 = correcao("q92",df_pie);q93 = correcao("q93",df_pie);q94 = correcao("q94",df_pie);q95 = correcao("q95",df_pie);q96 = correcao("q96",df_pie);q97 = correcao("q97",df_pie);q98 = correcao("q98",df_pie);q99 = correcao("q99",df_pie);q100 = correcao("q100",df_pie)
        q101 = correcao("q101",df_pie);q102 = correcao("q102",df_pie);q103 = correcao("q103",df_pie);q104 = correcao("q104",df_pie);q105 = correcao("q105",df_pie);q106 = correcao("q106",df_pie);q107 = correcao("q107",df_pie);q108 = correcao("q108",df_pie);q109 = correcao("q109",df_pie);q110 = correcao("q110",df_pie)
        list_question = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33,q34,q35,q36,q37,q38,q39,q40,q41,q42,q43,q44,q45,q46,q47,q48,q49,q50,q51,q52,q53,q54,q55,q56,q57,q58,q59,q60,q61,q62,q63,q64,q65,q66,q67,q68,q69,q70,q71,q72,q73,q74,q75,q76,q77,q78,q79,q80,q81,q82,q83,q84,q85,q86,q87,q88,q89,q90,q91,q92,q93,q94,q95,q96,q97,q98,q99,q100,q101,q102,q103,q104,q105,q106,q107,q108,q109,q110]
        df_skap = pd.DataFrame(result_dict)
        df_skap_correct = df_skap.drop(["_sa_instance_state","id",
                                    "q1","q2","q3","q4","q5","q6","q7","q8","q9","q10",                                  
                                    "q11","q12","q13","q14","q15","q16","q17","q18","q19","q20",                                 
                                    "q21","q22","q23","q24","q25","q26","q27","q28","q29","q30",                                 
                                    "q31","q32","q33","q34","q35","q36","q37","q38","q39","q40",                                
                                    "q41","q42","q43","q44","q45","q46","q47","q48","q49","q50",                                
                                    "q51","q52","q53","q54","q55","q56","q57","q58","q59","q60",                                 
                                    "q61","q62","q63","q64","q65","q66","q67","q68","q69","q70",                                 
                                    "q71","q72","q73","q74","q75","q76","q77","q78","q79","q80",                                 
                                    "q81","q82","q83","q84","q85","q86","q87","q88","q89","q90",                                 
                                    "q91","q92","q93","q94","q95","q96","q97","q98","q99","q100",                                
                                    "q101","q102","q103","q104","q105","q106","q107","q108","q109","q110"                       
                                    ], axis=1)
    else:
       df_skap_correct = pd.DataFrame({"Sem":0,"SKAP":4,"Preenchida":0,"No banco":4}, index=[0]) 
    
    return ([list_question,df_skap_correct])

def Mec(i):
    if i:
        result_dict = [u.__dict__ for u in i]
        df_pie = pd.DataFrame(result_dict)
        df_pie= df_pie.drop(["_sa_instance_state","id","resultado","number_id","area","username","turno"], axis=1)
        q1 = correcao("q1",df_pie);q2 = correcao("q2",df_pie);q3 = correcao("q3",df_pie);q4 = correcao("q4",df_pie);q5 = correcao("q5",df_pie);q6 = correcao("q6",df_pie);q7 = correcao("q7",df_pie);q8 = correcao("q8",df_pie);q9 = correcao("q9",df_pie);q10 = correcao("q10",df_pie) 
        q11 = correcao("q11",df_pie);q12 = correcao("q12",df_pie);q13 = correcao("q13",df_pie);q14 = correcao("q14",df_pie);q15 = correcao("q15",df_pie);q16 = correcao("q16",df_pie);q17 = correcao("q17",df_pie);q18 = correcao("q18",df_pie);q19 = correcao("q19",df_pie);q20 = correcao("q20",df_pie) 
        q21 = correcao("q21",df_pie);q22 = correcao("q22",df_pie);q23 = correcao("q23",df_pie);q24 = correcao("q24",df_pie);q25 = correcao("q25",df_pie);q26 = correcao("q26",df_pie);q27 = correcao("q27",df_pie);q28 = correcao("q28",df_pie);q29 = correcao("q29",df_pie);q30 = correcao("q30",df_pie)
        q31 = correcao("q31",df_pie);q32 = correcao("q32",df_pie);q33 = correcao("q33",df_pie);q34 = correcao("q34",df_pie);q35 = correcao("q35",df_pie);q36 = correcao("q36",df_pie);q37 = correcao("q37",df_pie);q38 = correcao("q38",df_pie);q39 = correcao("q39",df_pie);q40 = correcao("q40",df_pie) 
        q41 = correcao("q41",df_pie);q42 = correcao("q42",df_pie);q43 = correcao("q43",df_pie);q44 = correcao("q44",df_pie);q45 = correcao("q45",df_pie);q46 = correcao("q46",df_pie);q47 = correcao("q47",df_pie);q48 = correcao("q48",df_pie);q49 = correcao("q49",df_pie);q50 = correcao("q50",df_pie) 
        q51 = correcao("q51",df_pie);q52 = correcao("q52",df_pie);q53 = correcao("q53",df_pie);q54 = correcao("q54",df_pie);q55 = correcao("q55",df_pie);q56 = correcao("q56",df_pie);q57 = correcao("q57",df_pie);q58 = correcao("q58",df_pie);q59 = correcao("q59",df_pie);q60 = correcao("q60",df_pie)
        q61 = correcao("q61",df_pie);q62 = correcao("q62",df_pie);q63 = correcao("q63",df_pie);q64 = correcao("q64",df_pie);q65 = correcao("q65",df_pie);q66 = correcao("q66",df_pie);q67 = correcao("q67",df_pie);q68 = correcao("q68",df_pie);q69 = correcao("q69",df_pie);q70 = correcao("q70",df_pie) 
        q71 = correcao("q71",df_pie);q72 = correcao("q72",df_pie);q73 = correcao("q73",df_pie);q74 = correcao("q74",df_pie);q75 = correcao("q75",df_pie);q76 = correcao("q76",df_pie);q77 = correcao("q77",df_pie);q78 = correcao("q78",df_pie);q79 = correcao("q79",df_pie);q80 = correcao("q80",df_pie) 
        q81 = correcao("q81",df_pie);q82 = correcao("q82",df_pie);q83 = correcao("q83",df_pie);q84 = correcao("q84",df_pie);q85 = correcao("q85",df_pie);q86 = correcao("q86",df_pie);q87 = correcao("q87",df_pie);q88 = correcao("q88",df_pie);q89 = correcao("q89",df_pie);q90 = correcao("q90",df_pie) 
        q91 = correcao("q91",df_pie);q92 = correcao("q92",df_pie);q93 = correcao("q93",df_pie);q94 = correcao("q94",df_pie);q95 = correcao("q95",df_pie);q96 = correcao("q96",df_pie);q97 = correcao("q97",df_pie);q98 = correcao("q98",df_pie);q99 = correcao("q99",df_pie);q100 = correcao("q100",df_pie)
        q101 = correcao("q101",df_pie);q102 = correcao("q102",df_pie);q103 = correcao("q103",df_pie);q104 = correcao("q104",df_pie);q105 = correcao("q105",df_pie);q106 = correcao("q106",df_pie)
        list_question = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33,q34,q35,q36,q37,q38,q39,q40,q41,q42,q43,q44,q45,q46,q47,q48,q49,q50,q51,q52,q53,q54,q55,q56,q57,q58,q59,q60,q61,q62,q63,q64,q65,q66,q67,q68,q69,q70,q71,q72,q73,q74,q75,q76,q77,q78,q79,q80,q81,q82,q83,q84,q85,q86,q87,q88,q89,q90,q91,q92,q93,q94,q95,q96,q97,q98,q99,q100,q101,q102,q103,q104,q105,q106]
        df_skap = pd.DataFrame(result_dict)
        df_skap_correct = df_skap.drop(["_sa_instance_state","id",
                                    "q1","q2","q3","q4","q5","q6","q7","q8","q9","q10",                                  
                                    "q11","q12","q13","q14","q15","q16","q17","q18","q19","q20",                                 
                                    "q21","q22","q23","q24","q25","q26","q27","q28","q29","q30",                                 
                                    "q31","q32","q33","q34","q35","q36","q37","q38","q39","q40",                                
                                    "q41","q42","q43","q44","q45","q46","q47","q48","q49","q50",                                
                                    "q51","q52","q53","q54","q55","q56","q57","q58","q59","q60",                                 
                                    "q61","q62","q63","q64","q65","q66","q67","q68","q69","q70",                                 
                                    "q71","q72","q73","q74","q75","q76","q77","q78","q79","q80",                                 
                                    "q81","q82","q83","q84","q85","q86","q87","q88","q89","q90",                                 
                                    "q91","q92","q93","q94","q95","q96","q97","q98","q99","q100",                                
                                    "q101","q102","q103","q104","q105","q106"                       
                                    ], axis=1)
    else:
       df_skap_correct = pd.DataFrame({"Sem":0,"SKAP":4,"Preenchida":0,"No banco":4}, index=[0]) 
    
    return ([list_question,df_skap_correct])

def Elemec(i):
    if i:
        result_dict = [u.__dict__ for u in i]
        df_pie = pd.DataFrame(result_dict)
        df_pie= df_pie.drop(["_sa_instance_state","id","resultado","number_id","area","username","turno"], axis=1)
        q1 = correcao("q1",df_pie);q2 = correcao("q2",df_pie);q3 = correcao("q3",df_pie);q4 = correcao("q4",df_pie);q5 = correcao("q5",df_pie);q6 = correcao("q6",df_pie);q7 = correcao("q7",df_pie);q8 = correcao("q8",df_pie);q9 = correcao("q9",df_pie);q10 = correcao("q10",df_pie) 
        q11 = correcao("q11",df_pie);q12 = correcao("q12",df_pie);q13 = correcao("q13",df_pie);q14 = correcao("q14",df_pie);q15 = correcao("q15",df_pie);q16 = correcao("q16",df_pie);q17 = correcao("q17",df_pie);q18 = correcao("q18",df_pie);q19 = correcao("q19",df_pie);q20 = correcao("q20",df_pie) 
        q21 = correcao("q21",df_pie);q22 = correcao("q22",df_pie);q23 = correcao("q23",df_pie);q24 = correcao("q24",df_pie);q25 = correcao("q25",df_pie);q26 = correcao("q26",df_pie);q27 = correcao("q27",df_pie);q28 = correcao("q28",df_pie);q29 = correcao("q29",df_pie);q30 = correcao("q30",df_pie)
        q31 = correcao("q31",df_pie);q32 = correcao("q32",df_pie);q33 = correcao("q33",df_pie);q34 = correcao("q34",df_pie);q35 = correcao("q35",df_pie);q36 = correcao("q36",df_pie);q37 = correcao("q37",df_pie);q38 = correcao("q38",df_pie);q39 = correcao("q39",df_pie);q40 = correcao("q40",df_pie) 
        q41 = correcao("q41",df_pie);q42 = correcao("q42",df_pie);q43 = correcao("q43",df_pie);q44 = correcao("q44",df_pie);q45 = correcao("q45",df_pie);q46 = correcao("q46",df_pie);q47 = correcao("q47",df_pie);q48 = correcao("q48",df_pie);q49 = correcao("q49",df_pie);q50 = correcao("q50",df_pie) 
        q51 = correcao("q51",df_pie);q52 = correcao("q52",df_pie);q53 = correcao("q53",df_pie);q54 = correcao("q54",df_pie);q55 = correcao("q55",df_pie);q56 = correcao("q56",df_pie);q57 = correcao("q57",df_pie);q58 = correcao("q58",df_pie);q59 = correcao("q59",df_pie);q60 = correcao("q60",df_pie)
        q61 = correcao("q61",df_pie);q62 = correcao("q62",df_pie);q63 = correcao("q63",df_pie);q64 = correcao("q64",df_pie);q65 = correcao("q65",df_pie);q66 = correcao("q66",df_pie);q67 = correcao("q67",df_pie);q68 = correcao("q68",df_pie);q69 = correcao("q69",df_pie);q70 = correcao("q70",df_pie) 
        q71 = correcao("q71",df_pie);q72 = correcao("q72",df_pie);q73 = correcao("q73",df_pie);q74 = correcao("q74",df_pie);q75 = correcao("q75",df_pie);q76 = correcao("q76",df_pie);q77 = correcao("q77",df_pie);q78 = correcao("q78",df_pie);q79 = correcao("q79",df_pie);q80 = correcao("q80",df_pie) 
        q81 = correcao("q81",df_pie);q82 = correcao("q82",df_pie);q83 = correcao("q83",df_pie);q84 = correcao("q84",df_pie);q85 = correcao("q85",df_pie);q86 = correcao("q86",df_pie);q87 = correcao("q87",df_pie);q88 = correcao("q88",df_pie);q89 = correcao("q89",df_pie);q90 = correcao("q90",df_pie) 
        q91 = correcao("q91",df_pie);q92 = correcao("q92",df_pie);q93 = correcao("q93",df_pie);q94 = correcao("q94",df_pie);q95 = correcao("q95",df_pie);q96 = correcao("q96",df_pie);q97 = correcao("q97",df_pie);q98 = correcao("q98",df_pie);q99 = correcao("q99",df_pie);q100 = correcao("q100",df_pie)
        q101 = correcao("q101",df_pie);q102 = correcao("q102",df_pie);q103 = correcao("q103",df_pie);q104 = correcao("q104",df_pie);q105 = correcao("q105",df_pie);q106 = correcao("q106",df_pie);q107 = correcao("q107",df_pie);q108 = correcao("q108",df_pie);q109 = correcao("q109",df_pie);q110 = correcao("q110",df_pie)
        q111 = correcao("q111",df_pie);q112 = correcao("q112",df_pie);q113 = correcao("q113",df_pie);q114 = correcao("q114",df_pie);q115 = correcao("q115",df_pie);q116 = correcao("q116",df_pie);q117 = correcao("q117",df_pie);q118 = correcao("q108",df_pie);q119 = correcao("q119",df_pie);q120 = correcao("q120",df_pie)
        q121 = correcao("q121",df_pie);q122 = correcao("q122",df_pie);q123 = correcao("q123",df_pie);q124 = correcao("q124",df_pie);q125 = correcao("q125",df_pie);q126 = correcao("q126",df_pie);q127 = correcao("q127",df_pie);q128 = correcao("q108",df_pie);q129 = correcao("q129",df_pie);q130 = correcao("q130",df_pie)
        q131 = correcao("q131",df_pie);q132 = correcao("q132",df_pie);q133 = correcao("q133",df_pie);q134 = correcao("q134",df_pie);q135 = correcao("q135",df_pie);q136 = correcao("q136",df_pie);q137 = correcao("q137",df_pie);q138 = correcao("q108",df_pie)
        list_question = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33,q34,q35,q36,q37,q38,q39,q40,q41,q42,q43,q44,q45,q46,q47,q48,q49,q50,q51,q52,q53,q54,q55,q56,q57,q58,q59,q60,q61,q62,q63,q64,q65,q66,q67,q68,q69,q70,q71,q72,q73,q74,q75,q76,q77,q78,q79,q80,q81,q82,q83,q84,q85,q86,q87,q88,q89,q90,q91,q92,q93,q94,q95,q96,q97,q98,q99,q100,q101,q102,q103,q104,q105,q106,q107,q108,q109,q110,q111,q112,q113,q114,q115,q116,q117,q118,q119,q120,q121,q122,q123,q124,q125,q126,q127,q128,q129,q130,q131,q132,q133,q134,q135,q136,q137,q138]
        df_skap = pd.DataFrame(result_dict)
        df_skap_correct = df_skap.drop(["_sa_instance_state","id",
                                    "q1","q2","q3","q4","q5","q6","q7","q8","q9","q10",                                  
                                    "q11","q12","q13","q14","q15","q16","q17","q18","q19","q20",                                 
                                    "q21","q22","q23","q24","q25","q26","q27","q28","q29","q30",                                 
                                    "q31","q32","q33","q34","q35","q36","q37","q38","q39","q40",                                
                                    "q41","q42","q43","q44","q45","q46","q47","q48","q49","q50",                                
                                    "q51","q52","q53","q54","q55","q56","q57","q58","q59","q60",                                 
                                    "q61","q62","q63","q64","q65","q66","q67","q68","q69","q70",                                 
                                    "q71","q72","q73","q74","q75","q76","q77","q78","q79","q80",                                 
                                    "q81","q82","q83","q84","q85","q86","q87","q88","q89","q90",                                 
                                    "q91","q92","q93","q94","q95","q96","q97","q98","q99","q100",                                
                                    "q101","q102","q103","q104","q105","q106","q107","q108","q109","q110",
                                    "q111","q112","q113","q114","q115","q116","q117","q118","q119","q120",
                                    "q121","q122","q123","q124","q125","q126","q127","q128","q129","q130",
                                    "q131","q132","q133","q134","q135","q136","q137","q138"                       
                                    ], axis=1)
    else:
       df_skap_correct = pd.DataFrame({"Sem":0,"SKAP":4,"Preenchida":0,"No banco":4}, index=[0]) 
    
    return ([list_question,df_skap_correct])

def Pontuacao(dataframe):

    try:
        pont = dataframe["resultado"].sum()
        pont_quant = len(dataframe["resultado"])
        pont_div = pont/pont_quant
        
    except:
        pont = 0
        pont_quant = 1
        pont_div = pont/pont_quant
    return pont_div



