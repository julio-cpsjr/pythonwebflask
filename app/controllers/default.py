from flask import render_template, flash, redirect, url_for
from app import app, db, lm
from app.models.tables import User, SkapAut, SkapElemec,SkapElet,SkapMec
from app.models.forms import SkapAutForm,SkapElemecForm,SkapEletForm,SkapMecForm,LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user
from app.controllers.team import Aut,Elet,Elemec,Mec, Pontuacao
import pandas as pd
import numpy as np
import json

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

#Route Index
@app.route('/')
@app.route('/index')
def index():
    if current_user.is_authenticated:
        info = current_user.username
        info_cargo = current_user.cargo
        try:
            if info_cargo == "Automacao":
                nota = SkapAut.query.filter_by(username=current_user.name).first()
            if info_cargo == "Eletrica":
                nota = SkapElet.query.filter_by(username=current_user.name).first()
                info_nota = nota.resultado
            if info_cargo == "Eletromecanica":
                nota = SkapElemec.query.filter_by(username=current_user.name).first()
            if info_cargo == "Mecanica":
                nota = SkapMec.query.filter_by(username=current_user.name).first()
            if info_cargo == "Lideranca":
                info_nota = -1
            else:
                info_nota = nota.resultado
        except:
            info_nota = 0
    else:
        info = "Técnico(a)"
        info_nota = 0
        info_cargo = ""
    return render_template('index.html', info=info, info_nota = info_nota, info_cargo = info_cargo)

#Route Form
@app.route('/form', methods=["GET","POST"])
def form():
    info = current_user.username
    count,div,mult=0,0,0
    if current_user.cargo == "Eletrica":
            form_skap = SkapEletForm()
    if current_user.cargo == "Automacao":
            form_skap = SkapAutForm()
    if current_user.cargo == "Mecanica":
            form_skap = SkapMecForm()
    if current_user.cargo == "Eletromecanica":
            form_skap = SkapElemecForm()

    if form_skap.validate_on_submit():
        if current_user.cargo == "Eletrica":
            hello = [form_skap.q1.data,form_skap.q2.data,form_skap.q3.data,form_skap.q4.data,form_skap.q5.data,form_skap.q6.data,form_skap.q7.data,form_skap.q8.data,form_skap.q9.data,form_skap.q10.data,form_skap.q11.data,form_skap.q12.data,form_skap.q13.data,form_skap.q14.data,form_skap.q15.data,form_skap.q16.data,form_skap.q17.data,form_skap.q18.data,form_skap.q19.data,form_skap.q20.data,form_skap.q21.data,form_skap.q22.data,form_skap.q23.data,form_skap.q24.data,form_skap.q25.data,form_skap.q26.data,form_skap.q27.data,form_skap.q28.data,form_skap.q29.data,form_skap.q30.data,form_skap.q31.data,form_skap.q32.data,form_skap.q33.data,form_skap.q34.data,form_skap.q35.data,form_skap.q36.data,form_skap.q37.data,form_skap.q38.data,form_skap.q39.data,form_skap.q40.data,form_skap.q41.data,form_skap.q42.data,form_skap.q43.data,form_skap.q44.data,form_skap.q45.data,form_skap.q46.data,form_skap.q47.data,form_skap.q48.data,form_skap.q49.data,form_skap.q50.data,form_skap.q51.data,form_skap.q52.data,form_skap.q53.data,form_skap.q54.data,form_skap.q55.data,form_skap.q56.data,form_skap.q57.data,form_skap.q58.data,form_skap.q59.data,form_skap.q60.data,form_skap.q61.data,form_skap.q62.data,form_skap.q63.data,form_skap.q64.data,form_skap.q65.data,form_skap.q66.data,form_skap.q67.data,form_skap.q68.data,form_skap.q69.data,form_skap.q70.data,form_skap.q71.data,form_skap.q72.data,form_skap.q73.data,form_skap.q74.data,form_skap.q75.data,form_skap.q76.data,form_skap.q77.data,form_skap.q78.data,form_skap.q79.data,form_skap.q80.data,form_skap.q81.data,form_skap.q82.data,form_skap.q83.data,form_skap.q84.data,form_skap.q85.data,form_skap.q86.data,form_skap.q87.data,form_skap.q88.data,form_skap.q89.data,form_skap.q90.data,form_skap.q91.data,form_skap.q92.data,form_skap.q93.data,form_skap.q94.data,form_skap.q95.data,form_skap.q96.data,form_skap.q97.data,form_skap.q98.data,form_skap.q99.data,form_skap.q100.data,form_skap.q101.data,form_skap.q102.data,form_skap.q103.data,form_skap.q104.data,form_skap.q105.data,form_skap.q106.data,form_skap.q107.data,form_skap.q108.data,form_skap.q109.data,form_skap.q110.data,form_skap.q111.data,form_skap.q112.data]
            for j in hello:
                if j ==1:
                 count+=1
            div = count/112
            mult = int(div * 100)
            try:
                i = SkapElet(current_user.name,current_user.number_id,current_user.area,current_user.turno,form_skap.q1.data,form_skap.q2.data,form_skap.q3.data,form_skap.q4.data,form_skap.q5.data,form_skap.q6.data,form_skap.q7.data,form_skap.q8.data,form_skap.q9.data,form_skap.q10.data,form_skap.q11.data,form_skap.q12.data,form_skap.q13.data,form_skap.q14.data,form_skap.q15.data,form_skap.q16.data,form_skap.q17.data,form_skap.q18.data,form_skap.q19.data,form_skap.q20.data,form_skap.q21.data,form_skap.q22.data,form_skap.q23.data,form_skap.q24.data,form_skap.q25.data,form_skap.q26.data,form_skap.q27.data,form_skap.q28.data,form_skap.q29.data,form_skap.q30.data,form_skap.q31.data,form_skap.q32.data,form_skap.q33.data,form_skap.q34.data,form_skap.q35.data,form_skap.q36.data,form_skap.q37.data,form_skap.q38.data,form_skap.q39.data,form_skap.q40.data,form_skap.q41.data,form_skap.q42.data,form_skap.q43.data,form_skap.q44.data,form_skap.q45.data,form_skap.q46.data,form_skap.q47.data,form_skap.q48.data,form_skap.q49.data,form_skap.q50.data,form_skap.q51.data,form_skap.q52.data,form_skap.q53.data,form_skap.q54.data,form_skap.q55.data,form_skap.q56.data,form_skap.q57.data,form_skap.q58.data,form_skap.q59.data,form_skap.q60.data,form_skap.q61.data,form_skap.q62.data,form_skap.q63.data,form_skap.q64.data,form_skap.q65.data,form_skap.q66.data,form_skap.q67.data,form_skap.q68.data,form_skap.q69.data,form_skap.q70.data,form_skap.q71.data,form_skap.q72.data,form_skap.q73.data,form_skap.q74.data,form_skap.q75.data,form_skap.q76.data,form_skap.q77.data,form_skap.q78.data,form_skap.q79.data,form_skap.q80.data,form_skap.q81.data,form_skap.q82.data,form_skap.q83.data,form_skap.q84.data,form_skap.q85.data,form_skap.q86.data,form_skap.q87.data,form_skap.q88.data,form_skap.q89.data,form_skap.q90.data,form_skap.q91.data,form_skap.q92.data,form_skap.q93.data,form_skap.q94.data,form_skap.q95.data,form_skap.q96.data,form_skap.q97.data,form_skap.q98.data,form_skap.q99.data,form_skap.q100.data,form_skap.q101.data,form_skap.q102.data,form_skap.q103.data,form_skap.q104.data,form_skap.q105.data,form_skap.q106.data,form_skap.q107.data,form_skap.q108.data,form_skap.q109.data,form_skap.q110.data,form_skap.q111.data,form_skap.q112.data,mult)
                db.create_all()
                db.session.add(i)
                db.session.commit()
                flash("Skap preenchida com sucesso! ")
                return redirect(url_for('index'))
            except:
                flash("Você já preencheu a SKAP")
                return redirect(url_for('index'))
            
        if current_user.cargo == "Automacao":
            hello = [form_skap.q1.data,form_skap.q2.data,form_skap.q3.data,form_skap.q4.data,form_skap.q5.data,form_skap.q6.data,form_skap.q7.data,form_skap.q8.data,form_skap.q9.data,form_skap.q10.data,form_skap.q11.data,form_skap.q12.data,form_skap.q13.data,form_skap.q14.data,form_skap.q15.data,form_skap.q16.data,form_skap.q17.data,form_skap.q18.data,form_skap.q19.data,form_skap.q20.data,form_skap.q21.data,form_skap.q22.data,form_skap.q23.data,form_skap.q24.data,form_skap.q25.data,form_skap.q26.data,form_skap.q27.data,form_skap.q28.data,form_skap.q29.data,form_skap.q30.data,form_skap.q31.data,form_skap.q32.data,form_skap.q33.data,form_skap.q34.data,form_skap.q35.data,form_skap.q36.data,form_skap.q37.data,form_skap.q38.data,form_skap.q39.data,form_skap.q40.data,form_skap.q41.data,form_skap.q42.data,form_skap.q43.data,form_skap.q44.data,form_skap.q45.data,form_skap.q46.data,form_skap.q47.data,form_skap.q48.data,form_skap.q49.data,form_skap.q50.data,form_skap.q51.data,form_skap.q52.data,form_skap.q53.data,form_skap.q54.data,form_skap.q55.data,form_skap.q56.data,form_skap.q57.data,form_skap.q58.data,form_skap.q59.data,form_skap.q60.data,form_skap.q61.data,form_skap.q62.data,form_skap.q63.data,form_skap.q64.data,form_skap.q65.data,form_skap.q66.data,form_skap.q67.data,form_skap.q68.data,form_skap.q69.data,form_skap.q70.data,form_skap.q71.data,form_skap.q72.data,form_skap.q73.data,form_skap.q74.data,form_skap.q75.data,form_skap.q76.data,form_skap.q77.data,form_skap.q78.data,form_skap.q79.data,form_skap.q80.data,form_skap.q81.data,form_skap.q82.data,form_skap.q83.data,form_skap.q84.data,form_skap.q85.data,form_skap.q86.data,form_skap.q87.data,form_skap.q88.data,form_skap.q89.data,form_skap.q90.data,form_skap.q91.data,form_skap.q92.data,form_skap.q93.data,form_skap.q94.data,form_skap.q95.data,form_skap.q96.data,form_skap.q97.data,form_skap.q98.data,form_skap.q99.data,form_skap.q100.data,form_skap.q101.data,form_skap.q102.data,form_skap.q103.data,form_skap.q104.data,form_skap.q105.data,form_skap.q106.data,form_skap.q107.data,form_skap.q108.data,form_skap.q109.data,form_skap.q110.data]
            for j in hello:
                if j ==1:
                 count+=1
            div = count/110
            mult = int(div * 100)
            try:
                i = SkapAut(current_user.name,current_user.number_id,current_user.area,current_user.turno,form_skap.q1.data,form_skap.q2.data,form_skap.q3.data,form_skap.q4.data,form_skap.q5.data,form_skap.q6.data,form_skap.q7.data,form_skap.q8.data,form_skap.q9.data,form_skap.q10.data,form_skap.q11.data,form_skap.q12.data,form_skap.q13.data,form_skap.q14.data,form_skap.q15.data,form_skap.q16.data,form_skap.q17.data,form_skap.q18.data,form_skap.q19.data,form_skap.q20.data,form_skap.q21.data,form_skap.q22.data,form_skap.q23.data,form_skap.q24.data,form_skap.q25.data,form_skap.q26.data,form_skap.q27.data,form_skap.q28.data,form_skap.q29.data,form_skap.q30.data,form_skap.q31.data,form_skap.q32.data,form_skap.q33.data,form_skap.q34.data,form_skap.q35.data,form_skap.q36.data,form_skap.q37.data,form_skap.q38.data,form_skap.q39.data,form_skap.q40.data,form_skap.q41.data,form_skap.q42.data,form_skap.q43.data,form_skap.q44.data,form_skap.q45.data,form_skap.q46.data,form_skap.q47.data,form_skap.q48.data,form_skap.q49.data,form_skap.q50.data,form_skap.q51.data,form_skap.q52.data,form_skap.q53.data,form_skap.q54.data,form_skap.q55.data,form_skap.q56.data,form_skap.q57.data,form_skap.q58.data,form_skap.q59.data,form_skap.q60.data,form_skap.q61.data,form_skap.q62.data,form_skap.q63.data,form_skap.q64.data,form_skap.q65.data,form_skap.q66.data,form_skap.q67.data,form_skap.q68.data,form_skap.q69.data,form_skap.q70.data,form_skap.q71.data,form_skap.q72.data,form_skap.q73.data,form_skap.q74.data,form_skap.q75.data,form_skap.q76.data,form_skap.q77.data,form_skap.q78.data,form_skap.q79.data,form_skap.q80.data,form_skap.q81.data,form_skap.q82.data,form_skap.q83.data,form_skap.q84.data,form_skap.q85.data,form_skap.q86.data,form_skap.q87.data,form_skap.q88.data,form_skap.q89.data,form_skap.q90.data,form_skap.q91.data,form_skap.q92.data,form_skap.q93.data,form_skap.q94.data,form_skap.q95.data,form_skap.q96.data,form_skap.q97.data,form_skap.q98.data,form_skap.q99.data,form_skap.q100.data,form_skap.q101.data,form_skap.q102.data,form_skap.q103.data,form_skap.q104.data,form_skap.q105.data,form_skap.q106.data,form_skap.q107.data,form_skap.q108.data,form_skap.q109.data,form_skap.q110.data,mult)
                db.create_all()
                db.session.add(i)
                db.session.commit()
                flash("Skap preenchida com sucesso! ")
                return redirect(url_for('index'))
            except:
                flash("Você já preencheu a SKAP")
                return redirect(url_for('index'))
            
        if current_user.cargo == "Mecanica":
            hello = [form_skap.q1.data,form_skap.q2.data,form_skap.q3.data,form_skap.q4.data,form_skap.q5.data,form_skap.q6.data,form_skap.q7.data,form_skap.q8.data,form_skap.q9.data,form_skap.q10.data,form_skap.q11.data,form_skap.q12.data,form_skap.q13.data,form_skap.q14.data,form_skap.q15.data,form_skap.q16.data,form_skap.q17.data,form_skap.q18.data,form_skap.q19.data,form_skap.q20.data,form_skap.q21.data,form_skap.q22.data,form_skap.q23.data,form_skap.q24.data,form_skap.q25.data,form_skap.q26.data,form_skap.q27.data,form_skap.q28.data,form_skap.q29.data,form_skap.q30.data,form_skap.q31.data,form_skap.q32.data,form_skap.q33.data,form_skap.q34.data,form_skap.q35.data,form_skap.q36.data,form_skap.q37.data,form_skap.q38.data,form_skap.q39.data,form_skap.q40.data,form_skap.q41.data,form_skap.q42.data,form_skap.q43.data,form_skap.q44.data,form_skap.q45.data,form_skap.q46.data,form_skap.q47.data,form_skap.q48.data,form_skap.q49.data,form_skap.q50.data,form_skap.q51.data,form_skap.q52.data,form_skap.q53.data,form_skap.q54.data,form_skap.q55.data,form_skap.q56.data,form_skap.q57.data,form_skap.q58.data,form_skap.q59.data,form_skap.q60.data,form_skap.q61.data,form_skap.q62.data,form_skap.q63.data,form_skap.q64.data,form_skap.q65.data,form_skap.q66.data,form_skap.q67.data,form_skap.q68.data,form_skap.q69.data,form_skap.q70.data,form_skap.q71.data,form_skap.q72.data,form_skap.q73.data,form_skap.q74.data,form_skap.q75.data,form_skap.q76.data,form_skap.q77.data,form_skap.q78.data,form_skap.q79.data,form_skap.q80.data,form_skap.q81.data,form_skap.q82.data,form_skap.q83.data,form_skap.q84.data,form_skap.q85.data,form_skap.q86.data,form_skap.q87.data,form_skap.q88.data,form_skap.q89.data,form_skap.q90.data,form_skap.q91.data,form_skap.q92.data,form_skap.q93.data,form_skap.q94.data,form_skap.q95.data,form_skap.q96.data,form_skap.q97.data,form_skap.q98.data,form_skap.q99.data,form_skap.q100.data,form_skap.q101.data,form_skap.q102.data,form_skap.q103.data,form_skap.q104.data,form_skap.q105.data,form_skap.q106.data]
            for j in hello:
                if j ==1:
                 count+=1
            div = count/106
            mult = int(div * 100)
            try:
                i = SkapMec(current_user.name,current_user.number_id,current_user.area,current_user.turno,form_skap.q1.data,form_skap.q2.data,form_skap.q3.data,form_skap.q4.data,form_skap.q5.data,form_skap.q6.data,form_skap.q7.data,form_skap.q8.data,form_skap.q9.data,form_skap.q10.data,form_skap.q11.data,form_skap.q12.data,form_skap.q13.data,form_skap.q14.data,form_skap.q15.data,form_skap.q16.data,form_skap.q17.data,form_skap.q18.data,form_skap.q19.data,form_skap.q20.data,form_skap.q21.data,form_skap.q22.data,form_skap.q23.data,form_skap.q24.data,form_skap.q25.data,form_skap.q26.data,form_skap.q27.data,form_skap.q28.data,form_skap.q29.data,form_skap.q30.data,form_skap.q31.data,form_skap.q32.data,form_skap.q33.data,form_skap.q34.data,form_skap.q35.data,form_skap.q36.data,form_skap.q37.data,form_skap.q38.data,form_skap.q39.data,form_skap.q40.data,form_skap.q41.data,form_skap.q42.data,form_skap.q43.data,form_skap.q44.data,form_skap.q45.data,form_skap.q46.data,form_skap.q47.data,form_skap.q48.data,form_skap.q49.data,form_skap.q50.data,form_skap.q51.data,form_skap.q52.data,form_skap.q53.data,form_skap.q54.data,form_skap.q55.data,form_skap.q56.data,form_skap.q57.data,form_skap.q58.data,form_skap.q59.data,form_skap.q60.data,form_skap.q61.data,form_skap.q62.data,form_skap.q63.data,form_skap.q64.data,form_skap.q65.data,form_skap.q66.data,form_skap.q67.data,form_skap.q68.data,form_skap.q69.data,form_skap.q70.data,form_skap.q71.data,form_skap.q72.data,form_skap.q73.data,form_skap.q74.data,form_skap.q75.data,form_skap.q76.data,form_skap.q77.data,form_skap.q78.data,form_skap.q79.data,form_skap.q80.data,form_skap.q81.data,form_skap.q82.data,form_skap.q83.data,form_skap.q84.data,form_skap.q85.data,form_skap.q86.data,form_skap.q87.data,form_skap.q88.data,form_skap.q89.data,form_skap.q90.data,form_skap.q91.data,form_skap.q92.data,form_skap.q93.data,form_skap.q94.data,form_skap.q95.data,form_skap.q96.data,form_skap.q97.data,form_skap.q98.data,form_skap.q99.data,form_skap.q100.data,form_skap.q101.data,form_skap.q102.data,form_skap.q103.data,form_skap.q104.data,form_skap.q105.data,form_skap.q106.data,mult)
                db.create_all()
                db.session.add(i)
                db.session.commit()
                flash("Skap preenchida com sucesso! ")
                return redirect(url_for('index'))
            except:
                flash("Você já preencheu a SKAP")
                return redirect(url_for('index'))
            
        if current_user.cargo == "Eletromecanica":
            hello = [form_skap.q1.data,form_skap.q2.data,form_skap.q3.data,form_skap.q4.data,form_skap.q5.data,form_skap.q6.data,form_skap.q7.data,form_skap.q8.data,form_skap.q9.data,form_skap.q10.data,form_skap.q11.data,form_skap.q12.data,form_skap.q13.data,form_skap.q14.data,form_skap.q15.data,form_skap.q16.data,form_skap.q17.data,form_skap.q18.data,form_skap.q19.data,form_skap.q20.data,form_skap.q21.data,form_skap.q22.data,form_skap.q23.data,form_skap.q24.data,form_skap.q25.data,form_skap.q26.data,form_skap.q27.data,form_skap.q28.data,form_skap.q29.data,form_skap.q30.data,form_skap.q31.data,form_skap.q32.data,form_skap.q33.data,form_skap.q34.data,form_skap.q35.data,form_skap.q36.data,form_skap.q37.data,form_skap.q38.data,form_skap.q39.data,form_skap.q40.data,form_skap.q41.data,form_skap.q42.data,form_skap.q43.data,form_skap.q44.data,form_skap.q45.data,form_skap.q46.data,form_skap.q47.data,form_skap.q48.data,form_skap.q49.data,form_skap.q50.data,form_skap.q51.data,form_skap.q52.data,form_skap.q53.data,form_skap.q54.data,form_skap.q55.data,form_skap.q56.data,form_skap.q57.data,form_skap.q58.data,form_skap.q59.data,form_skap.q60.data,form_skap.q61.data,form_skap.q62.data,form_skap.q63.data,form_skap.q64.data,form_skap.q65.data,form_skap.q66.data,form_skap.q67.data,form_skap.q68.data,form_skap.q69.data,form_skap.q70.data,form_skap.q71.data,form_skap.q72.data,form_skap.q73.data,form_skap.q74.data,form_skap.q75.data,form_skap.q76.data,form_skap.q77.data,form_skap.q78.data,form_skap.q79.data,form_skap.q80.data,form_skap.q81.data,form_skap.q82.data,form_skap.q83.data,form_skap.q84.data,form_skap.q85.data,form_skap.q86.data,form_skap.q87.data,form_skap.q88.data,form_skap.q89.data,form_skap.q90.data,form_skap.q91.data,form_skap.q92.data,form_skap.q93.data,form_skap.q94.data,form_skap.q95.data,form_skap.q96.data,form_skap.q97.data,form_skap.q98.data,form_skap.q99.data,form_skap.q100.data,form_skap.q101.data,form_skap.q102.data,form_skap.q103.data,form_skap.q104.data,form_skap.q105.data,form_skap.q106.data,form_skap.q107.data,form_skap.q108.data,form_skap.q109.data,form_skap.q110.data,form_skap.q111.data,form_skap.q112.data,form_skap.q113.data,form_skap.q114.data,form_skap.q115.data,form_skap.q116.data,form_skap.q117.data,form_skap.q118.data,form_skap.q119.data,form_skap.q120.data,form_skap.q121.data,form_skap.q122.data,form_skap.q123.data,form_skap.q124.data,form_skap.q125.data,form_skap.q126.data,form_skap.q127.data,form_skap.q128.data,form_skap.q129.data,form_skap.q130.data,form_skap.q131.data,form_skap.q132.data,form_skap.q133.data,form_skap.q134.data,form_skap.q135.data,form_skap.q136.data,form_skap.q137.data,form_skap.q138.data]
            for j in hello:
                if j ==1:
                 count+=1
            div = count/138
            mult = int(div * 100)
            try:
                i = SkapElemec(current_user.name,current_user.number_id,current_user.area,current_user.turno,form_skap.q1.data,form_skap.q2.data,form_skap.q3.data,form_skap.q4.data,form_skap.q5.data,form_skap.q6.data,form_skap.q7.data,form_skap.q8.data,form_skap.q9.data,form_skap.q10.data,form_skap.q11.data,form_skap.q12.data,form_skap.q13.data,form_skap.q14.data,form_skap.q15.data,form_skap.q16.data,form_skap.q17.data,form_skap.q18.data,form_skap.q19.data,form_skap.q20.data,form_skap.q21.data,form_skap.q22.data,form_skap.q23.data,form_skap.q24.data,form_skap.q25.data,form_skap.q26.data,form_skap.q27.data,form_skap.q28.data,form_skap.q29.data,form_skap.q30.data,form_skap.q31.data,form_skap.q32.data,form_skap.q33.data,form_skap.q34.data,form_skap.q35.data,form_skap.q36.data,form_skap.q37.data,form_skap.q38.data,form_skap.q39.data,form_skap.q40.data,form_skap.q41.data,form_skap.q42.data,form_skap.q43.data,form_skap.q44.data,form_skap.q45.data,form_skap.q46.data,form_skap.q47.data,form_skap.q48.data,form_skap.q49.data,form_skap.q50.data,form_skap.q51.data,form_skap.q52.data,form_skap.q53.data,form_skap.q54.data,form_skap.q55.data,form_skap.q56.data,form_skap.q57.data,form_skap.q58.data,form_skap.q59.data,form_skap.q60.data,form_skap.q61.data,form_skap.q62.data,form_skap.q63.data,form_skap.q64.data,form_skap.q65.data,form_skap.q66.data,form_skap.q67.data,form_skap.q68.data,form_skap.q69.data,form_skap.q70.data,form_skap.q71.data,form_skap.q72.data,form_skap.q73.data,form_skap.q74.data,form_skap.q75.data,form_skap.q76.data,form_skap.q77.data,form_skap.q78.data,form_skap.q79.data,form_skap.q80.data,form_skap.q81.data,form_skap.q82.data,form_skap.q83.data,form_skap.q84.data,form_skap.q85.data,form_skap.q86.data,form_skap.q87.data,form_skap.q88.data,form_skap.q89.data,form_skap.q90.data,form_skap.q91.data,form_skap.q92.data,form_skap.q93.data,form_skap.q94.data,form_skap.q95.data,form_skap.q96.data,form_skap.q97.data,form_skap.q98.data,form_skap.q99.data,form_skap.q100.data,form_skap.q101.data,form_skap.q102.data,form_skap.q103.data,form_skap.q104.data,form_skap.q105.data,form_skap.q106.data,form_skap.q107.data,form_skap.q108.data,form_skap.q109.data,form_skap.q110.data,form_skap.q111.data,form_skap.q112.data,form_skap.q113.data,form_skap.q114.data,form_skap.q115.data,form_skap.q116.data,form_skap.q117.data,form_skap.q118.data,form_skap.q119.data,form_skap.q120.data,form_skap.q121.data,form_skap.q122.data,form_skap.q123.data,form_skap.q124.data,form_skap.q125.data,form_skap.q126.data,form_skap.q127.data,form_skap.q128.data,form_skap.q129.data,form_skap.q130.data,form_skap.q131.data,form_skap.q132.data,form_skap.q133.data,form_skap.q134.data,form_skap.q135.data,form_skap.q136.data,form_skap.q137.data,form_skap.q138.data,mult)
                db.create_all()
                db.session.add(i)
                db.session.commit()
                flash("Skap preenchida com sucesso! ")
                return redirect(url_for('index'))
            except:
                flash("Você já preencheu a SKAP")
                return redirect(url_for('index'))
    return render_template('form.html', info=info, form=form_skap)

#Route Team
@app.route('/team')
def team():
    try:
        i = SkapAut.query.filter_by(area=current_user.area).all()
        df_Aut = Aut(i)
        list_Aut = df_Aut[0]
        df_Aut = df_Aut[1]
    
    except:
        df_Aut = {}
        list_Aut = []
        df_Aut = pd.DataFrame(df_Aut)

    try:
        j = SkapElet.query.filter_by(area=current_user.area).all()
        df_Elet = Elet(j)
        list_Elet = df_Elet[0]
        df_Elet = df_Elet[1]
    except:
        df_Elet = {}
        list_Elet = []
        df_Elet = pd.DataFrame(df_Elet)

    try:
        k = SkapMec.query.filter_by(area=current_user.area).all()
        df_Elemec = Elemec(k)
        list_Elemec = df_Elemec[0]
        df_Elemec = df_Elemec[1]
    except:
        df_Elemec = {}
        list_Elemec = []
        df_Elemec = pd.DataFrame(df_Elemec)

    try:
        l = SkapElemec.query.filter_by(area=current_user.area).all()
        df_Mec = Mec(l)
        list_Mec = df_Mec[0]
        df_Mec = df_Mec[1]
    except:
        df_Mec = {}
        list_Mec = []
        df_Mec = pd.DataFrame(df_Mec)
    

    pont_aut_div = Pontuacao(df_Aut)
    pont_elet_div = Pontuacao(df_Elet)
    pont_elemec_div = Pontuacao(df_Elemec)
    pont_mec_div = Pontuacao(df_Mec)
    
    graph_med = [pont_aut_div, pont_elet_div, pont_elemec_div, pont_mec_div]
    cont = 0
    for i in graph_med:
        if i > 0:
            cont+=1
    try:
        pontuacao_geral = (pont_aut_div + pont_elet_div + pont_elemec_div + pont_mec_div ) / cont
    except:
        pontuacao_geral = 0

    rest_aut = 100 - pont_aut_div
    rest_elet = 100 - pont_elet_div
    rest_elemec = 100 - pont_elemec_div
    rest_mec = 100 - pont_mec_div
    rest_ger = 100 - pontuacao_geral

    pont_aut_list = [rest_aut,pont_aut_div] 
    pont_elet_list = [rest_elet, pont_elet_div]
    pont_elemec_list = [rest_elemec, pont_elemec_div]
    pont_mec_list = [rest_mec,pont_mec_div]
    pont_ger_list = [rest_ger,pontuacao_geral]

    return render_template('team.html', df_Aut = df_Aut.to_json(default_handler=str), df_Elet =df_Elet.to_json(default_handler=str), df_Elemec =df_Elemec.to_json(default_handler=str), df_Mec=df_Mec.to_json(default_handler=str),\
                           lista_Aut=list_Aut, lista_Elet=list_Elet, lista_Elemec=list_Elemec, lista_Mec=list_Mec, pont_geral = pont_ger_list, pont_aut = pont_aut_list, pont_elemec = pont_elemec_list, pont_elet = pont_elet_list, pont_mec = pont_mec_list )


#Route Login
@app.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in", category="sucess")
            print(user.username)
            info = current_user
            if info.cargo == "Lideranca":
                return redirect(url_for('team'))
            else:
                return redirect(url_for('form', info=info))
        else:
            flash("Invalid Login", category="error")
    return render_template('login.html', form=form)

#Route Logout
@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out", category="warning")
    return redirect(url_for("index"))

#Route Register
@app.route('/register',methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.is_submitted():
        try:
            i = User(form.username.data,form.password.data,form.name.data,form.email.data,form.cargo.data,form.area.data,form.turno.data,form.number_id.data)
            db.session.add(i)
            db.session.commit()
            flash("Usuário foi criado")
            return redirect(url_for("login"))
        except:
            flash("Usuário já está cadastrado")
    return render_template('register.html', form=form)

#Route Select User
@app.route('/select/<user>')
@app.route('/select', defaults={"user": "Selecione um usuário"})
def select(user):
    i = User.query.filter_by(username=user).all()
    if i :
        print(i)
        return "Ok"
    else:
        return "Table empty"

#Route Select All Users
@app.route('/select/users/all')
def select_users():
        i = User.query.all()
        if i :
            print(i)
            return "Ok"
        else:
            return "Table empty"

#Route Select All Skaps
@app.route('/select/skap/<cargo>')
def select_skap(cargo):
    if cargo == "Automacao":
        i = SkapAut.query.all()
        if i :
            print(i)
            return "Ok"
        else:
            print(i)
            return "Table empty"
    if cargo == "Mecanica":
        i = SkapMec.query.all()
        if i :
            print(i)
            return "Ok"
        else:
            print(i)
            return "Table empty"
    if cargo == "Eletrica":
        i = SkapElet.query.all()
        if i :
            print(i)
            return "Ok"
        else:
            print(i)
            return "Table empty"
    if cargo == "Eletromecanica":
        i = SkapElemec.query.all()
        if i :
            print(i)
            return "Ok"
        else:
            print(i)
            return "Table empty"

#Route Update User
@app.route('/update')
def update():
    i = User.query.filter_by(username="julio").first()
    i.name="Julio R."
    db.session.add(i)
    db.session.commit()
    print(i.name)
    return "Ok"


#Route Delete User
@app.route('/delete/user/<users>')
def delete_user(users):
    i = User.query.filter_by(username="%s" % (users)).first()
    db.session.delete(i)
    db.session.commit()
    return "Ok"

#Route Delete User
@app.route('/delete/users')
def delete_user_all():
    i = User.query.all()
    db.session.delete(i)
    db.session.commit()
    return "Ok"

@app.route('/createuser')
def createuser():
    i = User("Julio","1234","Julio Cesar","julio@ambev.com","Automacao","ITF","ADM",99807331)
    db.create_all()
    db.session.add(i)
    db.session.commit()
    return "Usuario criado"