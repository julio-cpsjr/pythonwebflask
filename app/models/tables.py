from app import db, lm
from flask_login import UserMixin
import json
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String,unique=True)
    email = db.Column(db.String, unique=True)
    cargo = db.Column(db.String)
    area = db.Column(db.String)
    turno = db.Column(db.String)
    number_id = db.Column(db.Integer,unique=True)
    
    
    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    @lm.user_loader
    def get_id(self):
        return str(self.id)


    def __init__(self, username, password, name, email,cargo,area,turno, number_id):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.cargo = cargo
        self.area = area
        self.turno = turno
        self.number_id = number_id
    
    def __repr__(self):
        return f'{self.username},{self.cargo}' 
    # basta criar uma representação em formato de dicionário para pegar todas as informações que precisar


class SkapAut(db.Model):
    __tablename__ = "skapaut"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    number_id = db.Column(db.Integer,unique=True) 
    area = db.Column(db.String)
    turno = db.Column(db.String)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)
    q6 = db.Column(db.Integer)
    q7 = db.Column(db.Integer)
    q8 = db.Column(db.Integer)
    q9 = db.Column(db.Integer)
    q10 = db.Column(db.Integer)
    q11 = db.Column(db.Integer)
    q12 = db.Column(db.Integer)
    q13 = db.Column(db.Integer)
    q14 = db.Column(db.Integer)
    q15 = db.Column(db.Integer)
    q16 = db.Column(db.Integer)
    q17 = db.Column(db.Integer)
    q18 = db.Column(db.Integer)
    q19 = db.Column(db.Integer)
    q20 = db.Column(db.Integer)
    q21 = db.Column(db.Integer)
    q22 = db.Column(db.Integer)
    q23 = db.Column(db.Integer)
    q24 = db.Column(db.Integer)
    q25 = db.Column(db.Integer)
    q26 = db.Column(db.Integer)
    q27 = db.Column(db.Integer)
    q28 = db.Column(db.Integer)
    q29 = db.Column(db.Integer)
    q30 = db.Column(db.Integer)
    q31 = db.Column(db.Integer)
    q32 = db.Column(db.Integer)
    q33 = db.Column(db.Integer)
    q34 = db.Column(db.Integer)
    q35 = db.Column(db.Integer)
    q36 = db.Column(db.Integer)
    q37 = db.Column(db.Integer)
    q38 = db.Column(db.Integer)
    q39 = db.Column(db.Integer)
    q40 = db.Column(db.Integer)
    q41 = db.Column(db.Integer)
    q42 = db.Column(db.Integer)
    q43 = db.Column(db.Integer)
    q44 = db.Column(db.Integer)
    q45 = db.Column(db.Integer)
    q46 = db.Column(db.Integer)
    q47 = db.Column(db.Integer)
    q48 = db.Column(db.Integer)
    q49 = db.Column(db.Integer)
    q50 = db.Column(db.Integer)
    q51 = db.Column(db.Integer)
    q52 = db.Column(db.Integer)
    q53 = db.Column(db.Integer)
    q54 = db.Column(db.Integer)
    q55 = db.Column(db.Integer)
    q56 = db.Column(db.Integer)
    q57 = db.Column(db.Integer)
    q58 = db.Column(db.Integer)
    q59 = db.Column(db.Integer)
    q60 = db.Column(db.Integer)
    q61 = db.Column(db.Integer)
    q62 = db.Column(db.Integer)
    q63 = db.Column(db.Integer)
    q64 = db.Column(db.Integer)
    q65 = db.Column(db.Integer)
    q66 = db.Column(db.Integer)
    q67 = db.Column(db.Integer)
    q68 = db.Column(db.Integer)
    q69 = db.Column(db.Integer)
    q70 = db.Column(db.Integer)
    q71 = db.Column(db.Integer)
    q72 = db.Column(db.Integer)
    q73 = db.Column(db.Integer)
    q74 = db.Column(db.Integer)
    q75 = db.Column(db.Integer)
    q76 = db.Column(db.Integer)
    q77 = db.Column(db.Integer)
    q78 = db.Column(db.Integer)
    q79 = db.Column(db.Integer)
    q80 = db.Column(db.Integer)
    q81 = db.Column(db.Integer)
    q82 = db.Column(db.Integer)
    q83 = db.Column(db.Integer)
    q84 = db.Column(db.Integer)
    q85 = db.Column(db.Integer)
    q86 = db.Column(db.Integer)
    q87 = db.Column(db.Integer)
    q88 = db.Column(db.Integer)
    q89 = db.Column(db.Integer)
    q90 = db.Column(db.Integer)
    q91 = db.Column(db.Integer)
    q92 = db.Column(db.Integer)
    q93 = db.Column(db.Integer)
    q94 = db.Column(db.Integer)
    q95 = db.Column(db.Integer)
    q96 = db.Column(db.Integer)
    q97 = db.Column(db.Integer)
    q98 = db.Column(db.Integer)
    q99 = db.Column(db.Integer)
    q100 = db.Column(db.Integer)
    q101 = db.Column(db.Integer)
    q102 = db.Column(db.Integer)
    q103 = db.Column(db.Integer)
    q104 = db.Column(db.Integer)
    q105 = db.Column(db.Integer)
    q106 = db.Column(db.Integer)
    q107 = db.Column(db.Integer)
    q108 = db.Column(db.Integer)
    q109 = db.Column(db.Integer)
    q110 = db.Column(db.Integer)
    resultado = db.Column(db.Integer)

    def __init__(self, username, number_id, area, turno,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33,q34,q35,q36,q37,q38,q39,q40,q41,q42,q43,q44,q45,q46,q47,q48,q49,q50,q51,q52,q53,q54,q55,q56,q57,q58,q59,q60,q61,q62,q63,q64,q65,q66,q67,q68,q69,q70,q71,q72,q73,q74,q75,q76,q77,q78,q79,q80,q81,q82,q83,q84,q85,q86,q87,q88,q89,q90,q91,q92,q93,q94,q95,q96,q97,q98,q99,q100,q101,q102,q103,q104,q105,q106,q107,q108,q109,q110, resultado):
        self.username = username
        self.number_id = number_id
        self.area = area
        self.turno = turno
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10
        self.q11 = q11
        self.q12 = q12
        self.q13 = q13
        self.q14 = q14
        self.q15 = q15
        self.q16 = q16
        self.q17 = q17
        self.q18 = q18
        self.q19 = q19
        self.q20 = q20
        self.q21 = q21
        self.q22 = q22
        self.q23 = q23
        self.q24 = q24
        self.q25 = q25
        self.q26 = q26
        self.q27 = q27
        self.q28 = q28
        self.q29 = q29
        self.q30 = q30
        self.q31 = q31
        self.q32 = q32
        self.q33 = q33
        self.q34 = q34
        self.q35 = q35
        self.q36 = q36
        self.q37 = q37
        self.q38 = q38
        self.q39 = q39
        self.q40 = q40
        self.q41 = q41
        self.q42 = q42
        self.q43 = q43
        self.q44 = q44
        self.q45 = q45
        self.q46 = q46
        self.q47 = q47
        self.q48 = q48
        self.q49 = q49
        self.q50 = q50
        self.q51 = q51
        self.q52 = q52
        self.q53 = q53
        self.q54 = q54
        self.q55 = q55
        self.q56 = q56
        self.q57 = q57
        self.q58 = q58
        self.q59 = q59
        self.q60 = q60
        self.q61 = q61
        self.q62 = q62
        self.q63 = q63
        self.q64 = q64
        self.q65 = q65
        self.q66 = q66
        self.q67 = q67
        self.q68 = q68
        self.q69 = q69
        self.q70 = q70
        self.q71 = q71
        self.q72 = q72
        self.q73 = q73
        self.q74 = q74
        self.q75 = q75
        self.q76 = q76
        self.q77 = q77
        self.q78 = q78
        self.q79 = q79
        self.q80 = q80
        self.q81 = q81
        self.q82 = q82
        self.q83 = q83
        self.q84 = q84
        self.q85 = q85
        self.q86 = q86
        self.q87 = q87
        self.q88 = q88
        self.q89 = q89
        self.q90 = q90
        self.q91 = q91
        self.q92 = q92
        self.q93 = q93
        self.q94 = q94
        self.q95 = q95
        self.q96 = q96
        self.q97 = q97
        self.q98 = q98
        self.q99 = q99
        self.q100 = q100
        self.q101 = q101
        self.q102 = q102
        self.q103 = q103
        self.q104 = q104
        self.q105 = q105
        self.q106 = q106
        self.q107 = q107
        self.q108 = q108
        self.q109 = q109
        self.q110 = q110
        self.resultado = resultado
        
    def __str__(self):
        return f'{self.username},{self.number_id},{self.area},{self.turno},{self.q1},{self.q2},{self.q3},{self.q4},{self.q5},{self.q6},{self.q7},{self.q8},{self.q9},{self.q10},{self.q11},{self.q12},{self.q13},{self.q14},{self.q15},{self.q16},{self.q17},{self.q18},{self.q19},{self.q20},{self.q21},{self.q22},{self.q23},{self.q24},{self.q25},{self.q26},{self.q27},{self.q28},{self.q29},{self.q30},{self.q31},{self.q32},{self.q33},{self.q34},{self.q35},{self.q36},{self.q37},{self.q38},{self.q39},{self.q40},{self.q41},{self.q42},{self.q43},{self.q44},{self.q45},{self.q46},{self.q47},{self.q48},{self.q49},{self.q50},{self.q51},{self.q52},{self.q53},{self.q54},{self.q55},{self.q56},{self.q57},{self.q58},{self.q59},{self.q60},{self.q61},{self.q62},{self.q63},{self.q64},{self.q65},{self.q66},{self.q67},{self.q68},{self.q69},{self.q70},{self.q71},{self.q72},{self.q73},{self.q74},{self.q75},{self.q76},{self.q77},{self.q78},{self.q79},{self.q80},{self.q81},{self.q82},{self.q83},{self.q84},{self.q85},{self.q86},{self.q87},{self.q88},{self.q89},{self.q90},{self.q91},{self.q92},{self.q93},{self.q94},{self.q95},{self.q96},{self.q97},{self.q98},{self.q99},{self.q100},{self.q101},{self.q102},{self.q103},{self.q104},{self.q105},{self.q106},{self.q107},{self.q108},{self.q109},{self.q110},{self.resultado}'


class SkapElet(db.Model):
    __tablename__ = "skapele"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    number_id = db.Column(db.Integer,unique=True) 
    area = db.Column(db.String)
    turno = db.Column(db.String)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)
    q6 = db.Column(db.Integer)
    q7 = db.Column(db.Integer)
    q8 = db.Column(db.Integer)
    q9 = db.Column(db.Integer)
    q10 = db.Column(db.Integer)
    q11 = db.Column(db.Integer)
    q12 = db.Column(db.Integer)
    q13 = db.Column(db.Integer)
    q14 = db.Column(db.Integer)
    q15 = db.Column(db.Integer)
    q16 = db.Column(db.Integer)
    q17 = db.Column(db.Integer)
    q18 = db.Column(db.Integer)
    q19 = db.Column(db.Integer)
    q20 = db.Column(db.Integer)
    q21 = db.Column(db.Integer)
    q22 = db.Column(db.Integer)
    q23 = db.Column(db.Integer)
    q24 = db.Column(db.Integer)
    q25 = db.Column(db.Integer)
    q26 = db.Column(db.Integer)
    q27 = db.Column(db.Integer)
    q28 = db.Column(db.Integer)
    q29 = db.Column(db.Integer)
    q30 = db.Column(db.Integer)
    q31 = db.Column(db.Integer)
    q32 = db.Column(db.Integer)
    q33 = db.Column(db.Integer)
    q34 = db.Column(db.Integer)
    q35 = db.Column(db.Integer)
    q36 = db.Column(db.Integer)
    q37 = db.Column(db.Integer)
    q38 = db.Column(db.Integer)
    q39 = db.Column(db.Integer)
    q40 = db.Column(db.Integer)
    q41 = db.Column(db.Integer)
    q42 = db.Column(db.Integer)
    q43 = db.Column(db.Integer)
    q44 = db.Column(db.Integer)
    q45 = db.Column(db.Integer)
    q46 = db.Column(db.Integer)
    q47 = db.Column(db.Integer)
    q48 = db.Column(db.Integer)
    q49 = db.Column(db.Integer)
    q50 = db.Column(db.Integer)
    q51 = db.Column(db.Integer)
    q52 = db.Column(db.Integer)
    q53 = db.Column(db.Integer)
    q54 = db.Column(db.Integer)
    q55 = db.Column(db.Integer)
    q56 = db.Column(db.Integer)
    q57 = db.Column(db.Integer)
    q58 = db.Column(db.Integer)
    q59 = db.Column(db.Integer)
    q60 = db.Column(db.Integer)
    q61 = db.Column(db.Integer)
    q62 = db.Column(db.Integer)
    q63 = db.Column(db.Integer)
    q64 = db.Column(db.Integer)
    q65 = db.Column(db.Integer)
    q66 = db.Column(db.Integer)
    q67 = db.Column(db.Integer)
    q68 = db.Column(db.Integer)
    q69 = db.Column(db.Integer)
    q70 = db.Column(db.Integer)
    q71 = db.Column(db.Integer)
    q72 = db.Column(db.Integer)
    q73 = db.Column(db.Integer)
    q74 = db.Column(db.Integer)
    q75 = db.Column(db.Integer)
    q76 = db.Column(db.Integer)
    q77 = db.Column(db.Integer)
    q78 = db.Column(db.Integer)
    q79 = db.Column(db.Integer)
    q80 = db.Column(db.Integer)
    q81 = db.Column(db.Integer)
    q82 = db.Column(db.Integer)
    q83 = db.Column(db.Integer)
    q84 = db.Column(db.Integer)
    q85 = db.Column(db.Integer)
    q86 = db.Column(db.Integer)
    q87 = db.Column(db.Integer)
    q88 = db.Column(db.Integer)
    q89 = db.Column(db.Integer)
    q90 = db.Column(db.Integer)
    q91 = db.Column(db.Integer)
    q92 = db.Column(db.Integer)
    q93 = db.Column(db.Integer)
    q94 = db.Column(db.Integer)
    q95 = db.Column(db.Integer)
    q96 = db.Column(db.Integer)
    q97 = db.Column(db.Integer)
    q98 = db.Column(db.Integer)
    q99 = db.Column(db.Integer)
    q100 = db.Column(db.Integer)
    q101 = db.Column(db.Integer)
    q102 = db.Column(db.Integer)
    q103 = db.Column(db.Integer)
    q104 = db.Column(db.Integer)
    q105 = db.Column(db.Integer)
    q106 = db.Column(db.Integer)
    q107 = db.Column(db.Integer)
    q108 = db.Column(db.Integer)
    q109 = db.Column(db.Integer)
    q110 = db.Column(db.Integer)
    q111 = db.Column(db.Integer)
    q112 = db.Column(db.Integer)
    resultado = db.Column(db.Integer)

    def __init__(self, username, number_id, area, turno,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33,q34,q35,q36,q37,q38,q39,q40,q41,q42,q43,q44,q45,q46,q47,q48,q49,q50,q51,q52,q53,q54,q55,q56,q57,q58,q59,q60,q61,q62,q63,q64,q65,q66,q67,q68,q69,q70,q71,q72,q73,q74,q75,q76,q77,q78,q79,q80,q81,q82,q83,q84,q85,q86,q87,q88,q89,q90,q91,q92,q93,q94,q95,q96,q97,q98,q99,q100,q101,q102,q103,q104,q105,q106,q107,q108,q109,q110,q111,q112,resultado):
        self.username = username
        self.number_id = number_id
        self.area = area
        self.turno = turno
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10
        self.q11 = q11
        self.q12 = q12
        self.q13 = q13
        self.q14 = q14
        self.q15 = q15
        self.q16 = q16
        self.q17 = q17
        self.q18 = q18
        self.q19 = q19
        self.q20 = q20
        self.q21 = q21
        self.q22 = q22
        self.q23 = q23
        self.q24 = q24
        self.q25 = q25
        self.q26 = q26
        self.q27 = q27
        self.q28 = q28
        self.q29 = q29
        self.q30 = q30
        self.q31 = q31
        self.q32 = q32
        self.q33 = q33
        self.q34 = q34
        self.q35 = q35
        self.q36 = q36
        self.q37 = q37
        self.q38 = q38
        self.q39 = q39
        self.q40 = q40
        self.q41 = q41
        self.q42 = q42
        self.q43 = q43
        self.q44 = q44
        self.q45 = q45
        self.q46 = q46
        self.q47 = q47
        self.q48 = q48
        self.q49 = q49
        self.q50 = q50
        self.q51 = q51
        self.q52 = q52
        self.q53 = q53
        self.q54 = q54
        self.q55 = q55
        self.q56 = q56
        self.q57 = q57
        self.q58 = q58
        self.q59 = q59
        self.q60 = q60
        self.q61 = q61
        self.q62 = q62
        self.q63 = q63
        self.q64 = q64
        self.q65 = q65
        self.q66 = q66
        self.q67 = q67
        self.q68 = q68
        self.q69 = q69
        self.q70 = q70
        self.q71 = q71
        self.q72 = q72
        self.q73 = q73
        self.q74 = q74
        self.q75 = q75
        self.q76 = q76
        self.q77 = q77
        self.q78 = q78
        self.q79 = q79
        self.q80 = q80
        self.q81 = q81
        self.q82 = q82
        self.q83 = q83
        self.q84 = q84
        self.q85 = q85
        self.q86 = q86
        self.q87 = q87
        self.q88 = q88
        self.q89 = q89
        self.q90 = q90
        self.q91 = q91
        self.q92 = q92
        self.q93 = q93
        self.q94 = q94
        self.q95 = q95
        self.q96 = q96
        self.q97 = q97
        self.q98 = q98
        self.q99 = q99
        self.q100 = q100
        self.q101 = q101
        self.q102 = q102
        self.q103 = q103
        self.q104 = q104
        self.q105 = q105
        self.q106 = q106
        self.q107 = q107
        self.q108 = q108
        self.q109 = q109
        self.q110 = q110
        self.q111 = q111
        self.q112 = q112
        self.resultado = resultado
        
    def __str__(self):
        return f'{self.username},{self.number_id},{self.area},{self.turno},{self.q1},{self.q2},{self.q3},{self.q4},{self.q5},{self.q6},{self.q7},{self.q8},{self.q9},{self.q10},{self.q11},{self.q12},{self.q13},{self.q14},{self.q15},{self.q16},{self.q17},{self.q18},{self.q19},{self.q20},{self.q21},{self.q22},{self.q23},{self.q24},{self.q25},{self.q26},{self.q27},{self.q28},{self.q29},{self.q30},{self.q31},{self.q32},{self.q33},{self.q34},{self.q35},{self.q36},{self.q37},{self.q38},{self.q39},{self.q40},{self.q41},{self.q42},{self.q43},{self.q44},{self.q45},{self.q46},{self.q47},{self.q48},{self.q49},{self.q50},{self.q51},{self.q52},{self.q53},{self.q54},{self.q55},{self.q56},{self.q57},{self.q58},{self.q59},{self.q60},{self.q61},{self.q62},{self.q63},{self.q64},{self.q65},{self.q66},{self.q67},{self.q68},{self.q69},{self.q70},{self.q71},{self.q72},{self.q73},{self.q74},{self.q75},{self.q76},{self.q77},{self.q78},{self.q79},{self.q80},{self.q81},{self.q82},{self.q83},{self.q84},{self.q85},{self.q86},{self.q87},{self.q88},{self.q89},{self.q90},{self.q91},{self.q92},{self.q93},{self.q94},{self.q95},{self.q96},{self.q97},{self.q98},{self.q99},{self.q100},{self.q101},{self.q102},{self.q103},{self.q104},{self.q105},{self.q106},{self.q107},{self.q108},{self.q109},{self.q110},{self.q111},{self.q112},{self.resultado}'


class SkapMec(db.Model):
    __tablename__ = "skapmec"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    number_id = db.Column(db.Integer,unique=True) 
    area = db.Column(db.String)
    turno = db.Column(db.String)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)
    q6 = db.Column(db.Integer)
    q7 = db.Column(db.Integer)
    q8 = db.Column(db.Integer)
    q9 = db.Column(db.Integer)
    q10 = db.Column(db.Integer)
    q11 = db.Column(db.Integer)
    q12 = db.Column(db.Integer)
    q13 = db.Column(db.Integer)
    q14 = db.Column(db.Integer)
    q15 = db.Column(db.Integer)
    q16 = db.Column(db.Integer)
    q17 = db.Column(db.Integer)
    q18 = db.Column(db.Integer)
    q19 = db.Column(db.Integer)
    q20 = db.Column(db.Integer)
    q21 = db.Column(db.Integer)
    q22 = db.Column(db.Integer)
    q23 = db.Column(db.Integer)
    q24 = db.Column(db.Integer)
    q25 = db.Column(db.Integer)
    q26 = db.Column(db.Integer)
    q27 = db.Column(db.Integer)
    q28 = db.Column(db.Integer)
    q29 = db.Column(db.Integer)
    q30 = db.Column(db.Integer)
    q31 = db.Column(db.Integer)
    q32 = db.Column(db.Integer)
    q33 = db.Column(db.Integer)
    q34 = db.Column(db.Integer)
    q35 = db.Column(db.Integer)
    q36 = db.Column(db.Integer)
    q37 = db.Column(db.Integer)
    q38 = db.Column(db.Integer)
    q39 = db.Column(db.Integer)
    q40 = db.Column(db.Integer)
    q41 = db.Column(db.Integer)
    q42 = db.Column(db.Integer)
    q43 = db.Column(db.Integer)
    q44 = db.Column(db.Integer)
    q45 = db.Column(db.Integer)
    q46 = db.Column(db.Integer)
    q47 = db.Column(db.Integer)
    q48 = db.Column(db.Integer)
    q49 = db.Column(db.Integer)
    q50 = db.Column(db.Integer)
    q51 = db.Column(db.Integer)
    q52 = db.Column(db.Integer)
    q53 = db.Column(db.Integer)
    q54 = db.Column(db.Integer)
    q55 = db.Column(db.Integer)
    q56 = db.Column(db.Integer)
    q57 = db.Column(db.Integer)
    q58 = db.Column(db.Integer)
    q59 = db.Column(db.Integer)
    q60 = db.Column(db.Integer)
    q61 = db.Column(db.Integer)
    q62 = db.Column(db.Integer)
    q63 = db.Column(db.Integer)
    q64 = db.Column(db.Integer)
    q65 = db.Column(db.Integer)
    q66 = db.Column(db.Integer)
    q67 = db.Column(db.Integer)
    q68 = db.Column(db.Integer)
    q69 = db.Column(db.Integer)
    q70 = db.Column(db.Integer)
    q71 = db.Column(db.Integer)
    q72 = db.Column(db.Integer)
    q73 = db.Column(db.Integer)
    q74 = db.Column(db.Integer)
    q75 = db.Column(db.Integer)
    q76 = db.Column(db.Integer)
    q77 = db.Column(db.Integer)
    q78 = db.Column(db.Integer)
    q79 = db.Column(db.Integer)
    q80 = db.Column(db.Integer)
    q81 = db.Column(db.Integer)
    q82 = db.Column(db.Integer)
    q83 = db.Column(db.Integer)
    q84 = db.Column(db.Integer)
    q85 = db.Column(db.Integer)
    q86 = db.Column(db.Integer)
    q87 = db.Column(db.Integer)
    q88 = db.Column(db.Integer)
    q89 = db.Column(db.Integer)
    q90 = db.Column(db.Integer)
    q91 = db.Column(db.Integer)
    q92 = db.Column(db.Integer)
    q93 = db.Column(db.Integer)
    q94 = db.Column(db.Integer)
    q95 = db.Column(db.Integer)
    q96 = db.Column(db.Integer)
    q97 = db.Column(db.Integer)
    q98 = db.Column(db.Integer)
    q99 = db.Column(db.Integer)
    q100 = db.Column(db.Integer)
    q101 = db.Column(db.Integer)
    q102 = db.Column(db.Integer)
    q103 = db.Column(db.Integer)
    q104 = db.Column(db.Integer)
    q105 = db.Column(db.Integer)
    q106 = db.Column(db.Integer)
    resultado = db.Column(db.Integer)

    def __init__(self, username, number_id, area, turno,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33,q34,q35,q36,q37,q38,q39,q40,q41,q42,q43,q44,q45,q46,q47,q48,q49,q50,q51,q52,q53,q54,q55,q56,q57,q58,q59,q60,q61,q62,q63,q64,q65,q66,q67,q68,q69,q70,q71,q72,q73,q74,q75,q76,q77,q78,q79,q80,q81,q82,q83,q84,q85,q86,q87,q88,q89,q90,q91,q92,q93,q94,q95,q96,q97,q98,q99,q100,q101,q102,q103,q104,q105,q106,resultado):
        self.username = username
        self.number_id = number_id
        self.area = area
        self.turno = turno
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10
        self.q11 = q11
        self.q12 = q12
        self.q13 = q13
        self.q14 = q14
        self.q15 = q15
        self.q16 = q16
        self.q17 = q17
        self.q18 = q18
        self.q19 = q19
        self.q20 = q20
        self.q21 = q21
        self.q22 = q22
        self.q23 = q23
        self.q24 = q24
        self.q25 = q25
        self.q26 = q26
        self.q27 = q27
        self.q28 = q28
        self.q29 = q29
        self.q30 = q30
        self.q31 = q31
        self.q32 = q32
        self.q33 = q33
        self.q34 = q34
        self.q35 = q35
        self.q36 = q36
        self.q37 = q37
        self.q38 = q38
        self.q39 = q39
        self.q40 = q40
        self.q41 = q41
        self.q42 = q42
        self.q43 = q43
        self.q44 = q44
        self.q45 = q45
        self.q46 = q46
        self.q47 = q47
        self.q48 = q48
        self.q49 = q49
        self.q50 = q50
        self.q51 = q51
        self.q52 = q52
        self.q53 = q53
        self.q54 = q54
        self.q55 = q55
        self.q56 = q56
        self.q57 = q57
        self.q58 = q58
        self.q59 = q59
        self.q60 = q60
        self.q61 = q61
        self.q62 = q62
        self.q63 = q63
        self.q64 = q64
        self.q65 = q65
        self.q66 = q66
        self.q67 = q67
        self.q68 = q68
        self.q69 = q69
        self.q70 = q70
        self.q71 = q71
        self.q72 = q72
        self.q73 = q73
        self.q74 = q74
        self.q75 = q75
        self.q76 = q76
        self.q77 = q77
        self.q78 = q78
        self.q79 = q79
        self.q80 = q80
        self.q81 = q81
        self.q82 = q82
        self.q83 = q83
        self.q84 = q84
        self.q85 = q85
        self.q86 = q86
        self.q87 = q87
        self.q88 = q88
        self.q89 = q89
        self.q90 = q90
        self.q91 = q91
        self.q92 = q92
        self.q93 = q93
        self.q94 = q94
        self.q95 = q95
        self.q96 = q96
        self.q97 = q97
        self.q98 = q98
        self.q99 = q99
        self.q100 = q100
        self.q101 = q101
        self.q102 = q102
        self.q103 = q103
        self.q104 = q104
        self.q105 = q105
        self.q106 = q106
        self.resultado = resultado
        
    def __str__(self):
        return f'{self.username},{self.number_id},{self.area},{self.turno},{self.q1},{self.q2},{self.q3},{self.q4},{self.q5},{self.q6},{self.q7},{self.q8},{self.q9},{self.q10},{self.q11},{self.q12},{self.q13},{self.q14},{self.q15},{self.q16},{self.q17},{self.q18},{self.q19},{self.q20},{self.q21},{self.q22},{self.q23},{self.q24},{self.q25},{self.q26},{self.q27},{self.q28},{self.q29},{self.q30},{self.q31},{self.q32},{self.q33},{self.q34},{self.q35},{self.q36},{self.q37},{self.q38},{self.q39},{self.q40},{self.q41},{self.q42},{self.q43},{self.q44},{self.q45},{self.q46},{self.q47},{self.q48},{self.q49},{self.q50},{self.q51},{self.q52},{self.q53},{self.q54},{self.q55},{self.q56},{self.q57},{self.q58},{self.q59},{self.q60},{self.q61},{self.q62},{self.q63},{self.q64},{self.q65},{self.q66},{self.q67},{self.q68},{self.q69},{self.q70},{self.q71},{self.q72},{self.q73},{self.q74},{self.q75},{self.q76},{self.q77},{self.q78},{self.q79},{self.q80},{self.q81},{self.q82},{self.q83},{self.q84},{self.q85},{self.q86},{self.q87},{self.q88},{self.q89},{self.q90},{self.q91},{self.q92},{self.q93},{self.q94},{self.q95},{self.q96},{self.q97},{self.q98},{self.q99},{self.q100},{self.q101},{self.q102},{self.q103},{self.q104},{self.q105},{self.q106},{self.resultado}'


class SkapElemec(db.Model):
    __tablename__ = "skapelemec"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    number_id = db.Column(db.Integer,unique=True) 
    area = db.Column(db.String)
    turno = db.Column(db.String)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)
    q6 = db.Column(db.Integer)
    q7 = db.Column(db.Integer)
    q8 = db.Column(db.Integer)
    q9 = db.Column(db.Integer)
    q10 = db.Column(db.Integer)
    q11 = db.Column(db.Integer)
    q12 = db.Column(db.Integer)
    q13 = db.Column(db.Integer)
    q14 = db.Column(db.Integer)
    q15 = db.Column(db.Integer)
    q16 = db.Column(db.Integer)
    q17 = db.Column(db.Integer)
    q18 = db.Column(db.Integer)
    q19 = db.Column(db.Integer)
    q20 = db.Column(db.Integer)
    q21 = db.Column(db.Integer)
    q22 = db.Column(db.Integer)
    q23 = db.Column(db.Integer)
    q24 = db.Column(db.Integer)
    q25 = db.Column(db.Integer)
    q26 = db.Column(db.Integer)
    q27 = db.Column(db.Integer)
    q28 = db.Column(db.Integer)
    q29 = db.Column(db.Integer)
    q30 = db.Column(db.Integer)
    q31 = db.Column(db.Integer)
    q32 = db.Column(db.Integer)
    q33 = db.Column(db.Integer)
    q34 = db.Column(db.Integer)
    q35 = db.Column(db.Integer)
    q36 = db.Column(db.Integer)
    q37 = db.Column(db.Integer)
    q38 = db.Column(db.Integer)
    q39 = db.Column(db.Integer)
    q40 = db.Column(db.Integer)
    q41 = db.Column(db.Integer)
    q42 = db.Column(db.Integer)
    q43 = db.Column(db.Integer)
    q44 = db.Column(db.Integer)
    q45 = db.Column(db.Integer)
    q46 = db.Column(db.Integer)
    q47 = db.Column(db.Integer)
    q48 = db.Column(db.Integer)
    q49 = db.Column(db.Integer)
    q50 = db.Column(db.Integer)
    q51 = db.Column(db.Integer)
    q52 = db.Column(db.Integer)
    q53 = db.Column(db.Integer)
    q54 = db.Column(db.Integer)
    q55 = db.Column(db.Integer)
    q56 = db.Column(db.Integer)
    q57 = db.Column(db.Integer)
    q58 = db.Column(db.Integer)
    q59 = db.Column(db.Integer)
    q60 = db.Column(db.Integer)
    q61 = db.Column(db.Integer)
    q62 = db.Column(db.Integer)
    q63 = db.Column(db.Integer)
    q64 = db.Column(db.Integer)
    q65 = db.Column(db.Integer)
    q66 = db.Column(db.Integer)
    q67 = db.Column(db.Integer)
    q68 = db.Column(db.Integer)
    q69 = db.Column(db.Integer)
    q70 = db.Column(db.Integer)
    q71 = db.Column(db.Integer)
    q72 = db.Column(db.Integer)
    q73 = db.Column(db.Integer)
    q74 = db.Column(db.Integer)
    q75 = db.Column(db.Integer)
    q76 = db.Column(db.Integer)
    q77 = db.Column(db.Integer)
    q78 = db.Column(db.Integer)
    q79 = db.Column(db.Integer)
    q80 = db.Column(db.Integer)
    q81 = db.Column(db.Integer)
    q82 = db.Column(db.Integer)
    q83 = db.Column(db.Integer)
    q84 = db.Column(db.Integer)
    q85 = db.Column(db.Integer)
    q86 = db.Column(db.Integer)
    q87 = db.Column(db.Integer)
    q88 = db.Column(db.Integer)
    q89 = db.Column(db.Integer)
    q90 = db.Column(db.Integer)
    q91 = db.Column(db.Integer)
    q92 = db.Column(db.Integer)
    q93 = db.Column(db.Integer)
    q94 = db.Column(db.Integer)
    q95 = db.Column(db.Integer)
    q96 = db.Column(db.Integer)
    q97 = db.Column(db.Integer)
    q98 = db.Column(db.Integer)
    q99 = db.Column(db.Integer)
    q100 = db.Column(db.Integer)
    q101 = db.Column(db.Integer)
    q102 = db.Column(db.Integer)
    q103 = db.Column(db.Integer)
    q104 = db.Column(db.Integer)
    q105 = db.Column(db.Integer)
    q106 = db.Column(db.Integer)
    q107 = db.Column(db.Integer)
    q108 = db.Column(db.Integer)
    q109 = db.Column(db.Integer)
    q110 = db.Column(db.Integer)
    q111 = db.Column(db.Integer)
    q112 = db.Column(db.Integer)
    q113 = db.Column(db.Integer)
    q114 = db.Column(db.Integer)
    q115 = db.Column(db.Integer)
    q116 = db.Column(db.Integer)
    q117 = db.Column(db.Integer)
    q118 = db.Column(db.Integer)
    q119 = db.Column(db.Integer)
    q120 = db.Column(db.Integer)
    q121 = db.Column(db.Integer)
    q122 = db.Column(db.Integer)
    q123 = db.Column(db.Integer)
    q124 = db.Column(db.Integer)
    q125 = db.Column(db.Integer)
    q126 = db.Column(db.Integer)
    q127 = db.Column(db.Integer)
    q128 = db.Column(db.Integer)
    q129 = db.Column(db.Integer)
    q130 = db.Column(db.Integer)
    q131 = db.Column(db.Integer)
    q132 = db.Column(db.Integer)
    q133 = db.Column(db.Integer)
    q134 = db.Column(db.Integer)
    q135 = db.Column(db.Integer)
    q136 = db.Column(db.Integer)
    q137 = db.Column(db.Integer)
    q138 = db.Column(db.Integer)
    resultado = db.Column(db.Integer)

    def __init__(self, username, number_id, area, turno,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33,q34,q35,q36,q37,q38,q39,q40,q41,q42,q43,q44,q45,q46,q47,q48,q49,q50,q51,q52,q53,q54,q55,q56,q57,q58,q59,q60,q61,q62,q63,q64,q65,q66,q67,q68,q69,q70,q71,q72,q73,q74,q75,q76,q77,q78,q79,q80,q81,q82,q83,q84,q85,q86,q87,q88,q89,q90,q91,q92,q93,q94,q95,q96,q97,q98,q99,q100,q101,q102,q103,q104,q105,q106,q107,q108,q109,q110,q111,q112,q113,q114,q115,q116,q117,q118,q119,q120,q121,q122,q123,q124,q125,q126,q127,q128,q129,q130,q131,q132,q133,q134,q135,q136,q137,q138,resultado):
        self.username = username
        self.number_id = number_id
        self.area = area
        self.turno = turno
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10
        self.q11 = q11
        self.q12 = q12
        self.q13 = q13
        self.q14 = q14
        self.q15 = q15
        self.q16 = q16
        self.q17 = q17
        self.q18 = q18
        self.q19 = q19
        self.q20 = q20
        self.q21 = q21
        self.q22 = q22
        self.q23 = q23
        self.q24 = q24
        self.q25 = q25
        self.q26 = q26
        self.q27 = q27
        self.q28 = q28
        self.q29 = q29
        self.q30 = q30
        self.q31 = q31
        self.q32 = q32
        self.q33 = q33
        self.q34 = q34
        self.q35 = q35
        self.q36 = q36
        self.q37 = q37
        self.q38 = q38
        self.q39 = q39
        self.q40 = q40
        self.q41 = q41
        self.q42 = q42
        self.q43 = q43
        self.q44 = q44
        self.q45 = q45
        self.q46 = q46
        self.q47 = q47
        self.q48 = q48
        self.q49 = q49
        self.q50 = q50
        self.q51 = q51
        self.q52 = q52
        self.q53 = q53
        self.q54 = q54
        self.q55 = q55
        self.q56 = q56
        self.q57 = q57
        self.q58 = q58
        self.q59 = q59
        self.q60 = q60
        self.q61 = q61
        self.q62 = q62
        self.q63 = q63
        self.q64 = q64
        self.q65 = q65
        self.q66 = q66
        self.q67 = q67
        self.q68 = q68
        self.q69 = q69
        self.q70 = q70
        self.q71 = q71
        self.q72 = q72
        self.q73 = q73
        self.q74 = q74
        self.q75 = q75
        self.q76 = q76
        self.q77 = q77
        self.q78 = q78
        self.q79 = q79
        self.q80 = q80
        self.q81 = q81
        self.q82 = q82
        self.q83 = q83
        self.q84 = q84
        self.q85 = q85
        self.q86 = q86
        self.q87 = q87
        self.q88 = q88
        self.q89 = q89
        self.q90 = q90
        self.q91 = q91
        self.q92 = q92
        self.q93 = q93
        self.q94 = q94
        self.q95 = q95
        self.q96 = q96
        self.q97 = q97
        self.q98 = q98
        self.q99 = q99
        self.q100 = q100
        self.q101 = q101
        self.q102 = q102
        self.q103 = q103
        self.q104 = q104
        self.q105 = q105
        self.q106 = q106
        self.q107 = q107
        self.q108 = q108
        self.q109 = q109
        self.q110 = q110
        self.q111 = q111
        self.q112 = q112
        self.q113 = q113
        self.q114 = q114
        self.q115 = q115
        self.q116 = q116
        self.q117 = q117
        self.q118 = q118
        self.q119 = q119
        self.q120 = q120
        self.q121 = q121
        self.q122 = q122
        self.q123 = q123
        self.q124 = q124
        self.q125 = q125
        self.q126 = q126
        self.q127 = q127
        self.q128 = q128
        self.q129 = q129
        self.q130 = q130
        self.q131 = q131
        self.q132 = q132
        self.q133 = q133
        self.q134 = q134
        self.q135 = q135
        self.q136 = q136
        self.q137 = q137
        self.q138 = q138
        self.resultado = resultado
        
    def __str__(self):
        return f'{self.username},{self.number_id},{self.area},{self.turno},{self.q1},{self.q2},{self.q3},{self.q4},{self.q5},{self.q6},{self.q7},{self.q8},{self.q9},{self.q10},{self.q11},{self.q12},{self.q13},{self.q14},{self.q15},{self.q16},{self.q17},{self.q18},{self.q19},{self.q20},{self.q21},{self.q22},{self.q23},{self.q24},{self.q25},{self.q26},{self.q27},{self.q28},{self.q29},{self.q30},{self.q31},{self.q32},{self.q33},{self.q34},{self.q35},{self.q36},{self.q37},{self.q38},{self.q39},{self.q40},{self.q41},{self.q42},{self.q43},{self.q44},{self.q45},{self.q46},{self.q47},{self.q48},{self.q49},{self.q50},{self.q51},{self.q52},{self.q53},{self.q54},{self.q55},{self.q56},{self.q57},{self.q58},{self.q59},{self.q60},{self.q61},{self.q62},{self.q63},{self.q64},{self.q65},{self.q66},{self.q67},{self.q68},{self.q69},{self.q70},{self.q71},{self.q72},{self.q73},{self.q74},{self.q75},{self.q76},{self.q77},{self.q78},{self.q79},{self.q80},{self.q81},{self.q82},{self.q83},{self.q84},{self.q85},{self.q86},{self.q87},{self.q88},{self.q89},{self.q90},{self.q91},{self.q92},{self.q93},{self.q94},{self.q95},{self.q96},{self.q97},{self.q98},{self.q99},{self.q100},{self.q101},{self.q102},{self.q103},{self.q104},{self.q105},{self.q106},{self.q107},{self.q108},{self.q109},{self.q110},{self.q111},{self.q112},{self.q113},{self.q114},{self.q115},{self.q116},{self.q117},{self.q118},{self.q119},{self.q120},{self.q121},{self.q122},{self.q123},{self.q124},{self.q125},{self.q126},{self.q127},{self.q128},{self.q129},{self.q130},{self.q131},{self.q132},{self.q133},{self.q134},{self.q135},{self.q136},{self.q137},{self.q138},{self.resultado}'

