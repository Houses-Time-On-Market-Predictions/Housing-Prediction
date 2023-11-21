#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:46:31 2023

@author: dsgiraldo
"""

#IMPORTAR LIBRERIAS
pip install scipy
import streamlit as st
import numpy as np
import pickle 
import scipy.stats as stats
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import GradientBoostingRegressor
import sklearn
from pathlib import Path
import base64
from PIL import Image
import os
import pandas as pd
import io

loaded_model_inter = pickle.load(open("/Users/dsgiraldo/Desktop/Modelo_Ventas.sav","rb"))
bagging_model_arriendo = pickle.load(open("/Users/dsgiraldo/Desktop/Modelo_Arriendo.sav","rb"))
ST=[0,0,0]
VTIPO=[0,0]
LOC=[0,0,0,0,0,0,0,0,0]
TIPO2=0
ADMIN2=0
descarga="/Users/dsgiraldo/Desktop/Modelo_Ventas.sav"

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-color: #ffffff;
opacity: 1;
background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #ffffff 27px ), repeating-linear-gradient( #67aef655, #67aef6 );
        }
    </style>
    """
st.markdown(page_bg_img, unsafe_allow_html=True)

def intervals_loaded(newdata2):
  i=0
  predictions=[]
  newdataarray=np.asarray(newdata2)
  newdatarepshape=newdataarray.reshape(1,-1)
  while i<=9:
    pred=bagging_model_arriendo.estimators_[i].predict(newdatarepshape)
    outarray=pred[0]
    predictions.append(outarray)
    i=i+1
  margin_of_error = stats.t.ppf((1 + 0.99) / 2, df=len(predictions)-1) * (np.std(predictions, ddof=1) / np.sqrt(len(predictions)))
  sample_mean2 = np.mean(predictions)
  sample_std = np.std(predictions, ddof=1)
  lower_bound2 = np.mean(predictions) - margin_of_error
  upper_bound2 = np.mean(predictions) + margin_of_error

  return(sample_mean2,lower_bound2,upper_bound2)

def housing_prediction(newdata):
      i=0
      predictions=[]
      newdataarray=np.asarray(newdata)
      newdatarepshape=newdataarray.reshape(1,-1)
      while i<=9:
        pred=loaded_model_inter.estimators_[i].predict(newdatarepshape)
        outarray=pred[0]
        predictions.append(outarray)
        i=i+1
      margin_of_error = stats.t.ppf((1 + 0.99) / 2, df=len(predictions)-1) * (np.std(predictions, ddof=1) / np.sqrt(len(predictions)))
      sample_mean3 = np.mean(predictions)
      sample_std = np.std(predictions, ddof=1)
      lower_bound3 = np.mean(predictions) - margin_of_error
      upper_bound3 = np.mean(predictions) + margin_of_error

      return(sample_mean3,lower_bound3,upper_bound3)

def intervals_loaded_fordataset(newdata3):
  i=0
  predictions=[]
  newdataarray=np.asarray(newdata3)
  newdatarepshape=newdataarray.reshape(1,-1)
  while i<=9:
    pred=loaded_model_inter.estimators_[i].predict(newdatarepshape)
    outarray=pred[0]
    predictions.append(outarray)
    i=i+1
  margin_of_error = stats.t.ppf((1 + 0.99) / 2, df=len(predictions)-1) * (np.std(predictions, ddof=1) / np.sqrt(len(predictions)))
  sample_mean = np.mean(predictions)
  sample_std = np.std(predictions, ddof=1)
  lower_bound = np.mean(predictions) - margin_of_error
  upper_bound = np.mean(predictions) + margin_of_error

  return(sample_mean,lower_bound,upper_bound)

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def main():
    
    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=256 height=86>](https://www.uninorte.edu.co)'''.format(img_to_bytes("/Users/dsgiraldo/Desktop/UNINORTE.png")), unsafe_allow_html=True)
    
    P1=0
    P2=0
    P3=0
    P4=0
    P5=0
    P6=0
    P7=0
    P8=[3,4,5,6]
    P9=["CASA","APARTAMENTO"]
    P10=["SI","NO"]
    P11=["BARRIOS UNIDOS","CANDELARIA","CHAPINERO","ENGATIVA","FONTIBON","KENNEDY","MARTIRES","SUBA","TEUSAQUILLO","USAQUEN"]
    
    
    menu = ["Home","Subir Archivo","Ayuda","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    st.sidebar.markdown("<h1 style='text-align: center; color: black;'>INMUEBLES DESTACADOS</h1>", unsafe_allow_html=True)
    st.sidebar.markdown('''<div style="display: flex; justify-content: center;">
                        <img src='data:image/png;base64,{}' class='img-fluid' width=290 height=256>'''.format(img_to_bytes("/Users/dsgiraldo/Desktop/APT1.jpeg")), unsafe_allow_html=True)
    
    if st.sidebar.button("INFORMACIÓN DEL APARTAMENTO"):
        st.sidebar.markdown("Precio de Arriendo: 0")
        st.sidebar.markdown("Precio de Venta: 465.000.000")
        st.sidebar.markdown("Area del Inmueble en Metros Cuadrados: 109")
        st.sidebar.markdown("Numero de Habitaciones: 3")
        st.sidebar.markdown("Numero de Baños: 4")
        st.sidebar.markdown("Numero de Parqueaderos: 2")
        st.sidebar.markdown("Antiguedad en Años: 10")
        st.sidebar.markdown("Estrato de la Vivienda: 5")
        st.sidebar.markdown("Tipo de Inmueble: APARTAMENTO")
        st.sidebar.markdown("¿Se Debe Pagar Administracion?: SI")
        st.sidebar.markdown("Localidad en la que se Encuentra: CHAPINEROS")
    
    st.sidebar.markdown('''<div style="display: flex; justify-content: center;">
                        <img src='data:image/png;base64,{}' class='img-fluid' width=290 height=256>'''.format(img_to_bytes("/Users/dsgiraldo/Desktop/APT2.jpeg")), unsafe_allow_html=True)
   
    if st.sidebar.button(" INFORMACIÓN DEL APARTAMENTO"):
        st.sidebar.markdown("Precio de Arriendo: 1.800.000")
        st.sidebar.markdown("Precio de Venta: 0")
        st.sidebar.markdown("Area del Inmueble en Metros Cuadrados: 82")
        st.sidebar.markdown("Numero de Habitaciones: 3")
        st.sidebar.markdown("Numero de Baños: 3")
        st.sidebar.markdown("Numero de Parqueaderos: 1")
        st.sidebar.markdown("Antiguedad en Años: 38")
        st.sidebar.markdown("Estrato de la Vivienda: 5")
        st.sidebar.markdown("Tipo de Inmueble: APARTAMENTO")
        st.sidebar.markdown("¿Se Debe Pagar Administracion?: SI")
        st.sidebar.markdown("Localidad en la que se Encuentra: USAQUEN")
    
    st.sidebar.markdown('''<div style="display: flex; justify-content: center;">
                        <img src='data:image/png;base64,{}' class='img-fluid' width=290 height=256>'''.format(img_to_bytes("/Users/dsgiraldo/Desktop/APT3.jpeg")), unsafe_allow_html=True)
                        
    if st.sidebar.button("  INFORMACIÓN DEL APARTAMENTO"):
         st.sidebar.markdown("Precio de Arriendo: 0")
         st.sidebar.markdown("Precio de Venta: 500.000.000")
         st.sidebar.markdown("Area del Inmueble en Metros Cuadrados: 119")
         st.sidebar.markdown("Numero de Habitaciones: 3")
         st.sidebar.markdown("Numero de Baños: 3")
         st.sidebar.markdown("Numero de Parqueaderos: 2")
         st.sidebar.markdown("Antiguedad en Años: 44")
         st.sidebar.markdown("Estrato de la Vivienda: 4")
         st.sidebar.markdown("Tipo de Inmueble: CASA")
         st.sidebar.markdown("¿Se Debe Pagar Administracion?: NO")
         st.sidebar.markdown("Localidad en la que se Encuentra: USAQUEN")
    
    
    if choice == "Home":
        
          st.title("PREDICCIONES DE TIEMPO PARA VENTAS Y ARRIENDOS")

          # GETTING THE INPUT DATA
          #['P/A', 'habitaciones', 'baños', 'Parquederos', 'Antigüedad_años','Estrato', 'Tipo_de_inmueble','valor_admin', 'Localidad']
          
          PRECIOA = st.number_input("**Precio De Arriendo**", step=1000000, min_value=0, value=P1)
          #PRECION=(PRECIOA-1767641)/1109204
          PRECIO = st.number_input("**Precio De Venta**", step=100000, min_value=0,value=P2)
          AREA = st.number_input("**Area Del Inmueble En Metros Cuadrados**", step=1, min_value=0,value=P3)
          PA=PRECIO/max(AREA,1)
          AREAN=(AREA-78.85)/46.81
          HABITACIONES = st.number_input("**Numero de Habitaciones**",step=1,min_value=0,value=P4)
          BAÑOS = st.number_input("**Numero de Baños**",step=1,min_value=0,value=P5)
          PARQUEADEROS = st.number_input("**Numero de Parqueaderos**",step=1,min_value=0,value=P6)
          ANTIGUEDAD = st.number_input("**Antiguedad en años**",step=1,min_value=0,value=P7)
          ANTIGUEDADN=(ANTIGUEDAD-20.99)/12.66
          ESTRATO = st.selectbox("**Estrato de la vivienda**",P8)
          if ESTRATO == 4:
              EST=[1,0,0]
          elif ESTRATO ==5:
              EST=[0,1,0]
          elif ESTRATO == 6:
              EST=[0,0,1]
          else:
              EST=[0,0,0]
          TIPO = st.selectbox("**Que tipo de vivienda se trata**",P9)

          if TIPO == "CASA":
           TIPO2 =1
          else:
              TIPO2 =0
                     
          ADMIN = st.selectbox("**¿Se debe pagar administracion?**",P10)
          if ADMIN == "SI":
            ADMIN2=0
            PrecioAdmin=st.number_input("**¿Cual es el precio de la administracion?**",step=100000, min_value=0, value=0)
          else:
              ADMIN2=1
              PrecioAdmin=0
          
          LOCALIDAD = st.selectbox("**Que Localidad Se Encuentra**",P11)
          if LOCALIDAD=="CANDELARIA":
              LOC[0]=1
              LOC[1]=0
              LOC[2]=0
              LOC[3]=0
              LOC[4]=0
              LOC[5]=0
              LOC[6]=0
              LOC[7]=0
              LOC[8]=0
          elif LOCALIDAD=="CHAPINERO":  
            LOC[0]=0
            LOC[1]=1
            LOC[2]=0
            LOC[3]=0
            LOC[4]=0
            LOC[5]=0
            LOC[6]=0
            LOC[7]=0
            LOC[8]=0
          elif LOCALIDAD=="ENGATIVA":
            LOC[0]=0
            LOC[1]=0
            LOC[2]=1
            LOC[3]=0
            LOC[4]=0
            LOC[5]=0
            LOC[6]=0
            LOC[7]=0
            LOC[8]=0
          elif LOCALIDAD=="FONTIBON":
            LOC[0]=0
            LOC[1]=0
            LOC[2]=0
            LOC[3]=1
            LOC[4]=0
            LOC[5]=0
            LOC[6]=0
            LOC[7]=0
            LOC[8]=0
          elif LOCALIDAD=="KENNEDY":
            LOC[0]=0
            LOC[1]=0
            LOC[2]=0
            LOC[3]=0
            LOC[4]=1
            LOC[5]=0
            LOC[6]=0
            LOC[7]=0
            LOC[8]=0
          elif LOCALIDAD=="MARTIRES":
            LOC[0]=0
            LOC[1]=0
            LOC[2]=0
            LOC[3]=0
            LOC[4]=0
            LOC[5]=1
            LOC[6]=0
            LOC[7]=0
            LOC[8]=0
          elif LOCALIDAD=="SUBA":
            LOC[0]=0
            LOC[1]=0
            LOC[2]=0
            LOC[3]=0
            LOC[4]=0
            LOC[5]=0
            LOC[6]=1
            LOC[7]=0
            LOC[8]=0
          elif LOCALIDAD=="TEUSAQUILLO":
            LOC[0]=0
            LOC[1]=0
            LOC[2]=0
            LOC[3]=0
            LOC[4]=0
            LOC[5]=0
            LOC[6]=0
            LOC[7]=1
            LOC[8]=0
          elif LOCALIDAD=="USAQUEN":
            LOC[0]=0
            LOC[1]=0
            LOC[2]=0
            LOC[3]=0
            LOC[4]=0
            LOC[5]=0
            LOC[6]=0
            LOC[7]=0
            LOC[8]=1
          else:
            LOC[0]=0
            LOC[1]=0
            LOC[2]=0
            LOC[3]=0
            LOC[4]=0
            LOC[5]=0
            LOC[6]=0
            LOC[7]=0
            LOC[8]=0
          #CODE FOR PREDICTION
          
          TIEMPOVENTA = ""
          TIEMPOARRIENDO = ""
          
          #CREATING A BUTTON FOR PREDICTION
          
          if st.button("Tiempo de Venta y/o Arriendo"):
              
              if PRECIO != 0 and PRECIOA !=0 and AREA != 0 and HABITACIONES !=0 and BAÑOS !=0 and PARQUEADEROS != 0 and ANTIGUEDAD != 0:
                 PRECION2=np.log(PRECIOA+PrecioAdmin)
                 PRECION=(PRECION2-14.54)/0.44
                 TIEMPOVENTA =[PA, HABITACIONES, BAÑOS, PARQUEADEROS, ANTIGUEDAD, EST[0], EST[1], EST[2], TIPO2, ADMIN2, LOC[0], LOC[1], LOC[2], LOC[3], LOC[4], LOC[5], LOC[6], LOC[7], LOC[8]] 
                 TIEMPOARRIENDO =[HABITACIONES, BAÑOS, PARQUEADEROS, PRECION, AREAN, ANTIGUEDADN, EST[0], EST[1], EST[2], TIPO2, LOC[0], LOC[1], LOC[2], LOC[3], LOC[4], LOC[5], LOC[6], LOC[7], LOC[8]]
                 #st.success(housing_prediction(TIEMPOVENTA))
                 variable=housing_prediction(TIEMPOVENTA)
                 variable2=intervals_loaded(TIEMPOARRIENDO)
                 st.markdown("Este inmueble se espera que se venda en un intervalo de tiempo de entre:")
                 st.markdown(f"Tiempo Minimo:{variable[1]}")
                 st.markdown(f"Tiempo Medio:{variable[0]}")
                 st.markdown(f"Tiempo Maximo:{variable[2]}")
                 #st.success(housing_prediction(TIEMPOVENTA))
                 #st.success(print("La medie es de: ",variable[0]))
                 #st.success(intervals_loaded(TIEMPOARRIENDO))
                 st.markdown("Este inmueble se espera que se arriende en un intervalo de tiempo de entre:")
                 st.markdown(f"Tiempo Minimo:{variable2[1]}")
                 st.markdown(f"Tiempo Medio:{variable2[0]}")
                 st.markdown(f"Tiempo Maximo:{variable2[2]}")
              elif PRECIO!=0 and PRECIOA ==0 and AREA != 0 and HABITACIONES !=0 and BAÑOS !=0 and PARQUEADEROS != 0 and ANTIGUEDAD != 0 :
                  TIEMPOVENTA =[PA, HABITACIONES, BAÑOS, PARQUEADEROS, ANTIGUEDAD, EST[0], EST[1], EST[2], TIPO2, ADMIN2, LOC[0], LOC[1], LOC[2], LOC[3], LOC[4], LOC[5], LOC[6], LOC[7], LOC[8]] 
                  variable=housing_prediction(TIEMPOVENTA)
                  st.markdown("Este inmueble se espera que se venda en un intervalo de tiempo de entre:")
                  st.markdown(f"Tiempo Minimo:{variable[1]}")
                  st.markdown(f"Tiempo Medio:{variable[0]}")
                  st.markdown(f"Tiempo Maximo:{variable[2]}")
                  st.markdown("Faltan datos para poder estimar el tiempo de arriendo")
                  
              elif PRECIO == 0 and PRECIOA != 0 and AREA != 0 and HABITACIONES !=0 and BAÑOS !=0 and PARQUEADEROS != 0 and ANTIGUEDAD != 0:
                  PRECION2=np.log(PRECIOA+PrecioAdmin)
                  PRECION=(PRECION2-14.54)/0.44
                  TIEMPOARRIENDO =[HABITACIONES, BAÑOS, PARQUEADEROS, PRECION, AREAN, ANTIGUEDADN, EST[0], EST[1], EST[2], TIPO2, LOC[0], LOC[1], LOC[2], LOC[3], LOC[4], LOC[5], LOC[6], LOC[7], LOC[8]]
                  variable2=intervals_loaded(TIEMPOARRIENDO)
                  st.markdown("Este inmueble se espera que se arriende en un intervalo de tiempo de entre:")
                  st.markdown(f"Tiempo Minimo:{variable2[1]}")
                  st.markdown(f"Tiempo Medio:{variable2[0]}")
                  st.markdown(f"Tiempo Maximo:{variable2[2]}")
                  st.markdown("Faltan datos para poder estimar el tiempo de venta")
              else:
                  st.markdown("Faltan datos para poder estimar el tiempo de venta y tiempo de arriendo")
              
             
              
              
          
            


    elif choice == "Subir Archivo":
		
            st.title("Sube Tu Archivo Para Ventas")
            uploaded_file = st.file_uploader("Upload Files",type=["xlsx"])
            
            if uploaded_file is not None:
             file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
             st.write(file_details)
             NEWPREDS = pd.read_excel(uploaded_file)
             NEWPREDS['Admin'] = (NEWPREDS['Valor_administración'] == 0).astype(int)
             NEWPREDS["Parquederos"]=NEWPREDS["Parqueaderos"]
             NEWPREDS=NEWPREDS.drop("Parqueaderos",axis=1)
             NEWPREDS=NEWPREDS.drop("Valor_administración",axis=1)
             NEWPREDS["P/A"]=NEWPREDS["Precio"]/NEWPREDS["Area"]
             NEWPREDS=NEWPREDS.drop("Precio",axis=1)
             NEWPREDS=NEWPREDS.drop("Area",axis=1)
             new_order=["P/A", 'Estrato', 'habitaciones',
                 'baños', 'Tipo_de_inmueble',
                  'Parquederos','Antigüedad_años',"Admin","Localidad"]
             NEWPREDS=NEWPREDS[new_order]
             NEWPREDS=pd.get_dummies(NEWPREDS,columns=["Estrato","Tipo_de_inmueble","Admin","Localidad"],drop_first=True)
             
         
             
             arraylow = np.array([])
             arraymean = np.array([])
             arrayupper = np.array([])

             for index, row in NEWPREDS.iterrows():
                mean,low,upper=intervals_loaded_fordataset(row)
                arraymean = np.append(arraymean, mean)
                arraylow = np.append(arraylow, low)
                arrayupper = np.append(arrayupper, upper)
                
             NEWPREDS["low"]=arraylow
             NEWPREDS["mean"]=arraymean
             NEWPREDS["upper"]=arrayupper
             #excel_file="excelfile.xlsx"
             #NEWPREDS.to_excel(excel_file,index=False)
             
             def convert_df(NEWPREDS):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
                 return NEWPREDS.to_csv().encode('utf-8')

             csv = convert_df(NEWPREDS)
             #excel_file = 'output.xlsx'
             #csv.to_excel(excel_file, index=False)
             csv_bytes = io.BytesIO(csv)
             df = pd.read_csv(csv_bytes)
             excel_file = io.BytesIO()
             df.to_excel(excel_file, index=False)
             excel_file.seek(0)

             st.download_button(
             label="Descargar excel con las predicciónes",
             data=excel_file,
             file_name='Predicciones_De_Venta.xlsx',
             mime='text/xlsx',
                 )
             
             #nombre_archivo = "datos.xlsx"  # Nombre del archivo Excel
             #with pd.ExcelWriter(nombre_archivo, engine='xlsxwriter') as writer:
                 #NEWPREDS.to_excel(writer, index=False, sheet_name='Hoja1')  # Guardar el DataFrame como archivo Excel
             #st.success(f"Archivo '{nombre_archivo}' guardado exitosamente.")
            
             
             #def descargar_csv():
                # descargar = NEWPREDS.to_excel(index=False)
                 #b64 = base64.b64encode(descargar.encode()).decode()
                # href = f'<a href="data:file/csv;base64,{b64}" download="Predicciones.xlsx">Descargar archivo XLSX</a>'
                # st.markdown(href, unsafe_allow_html=True)
                 
             #st.download_button(
             #label="Descarga tus pronosticos",
             #data="datos.xlsx",
             #mime="xlsx"
             #  )
            #if st.button("Descargar"):
                 # descargar_csv()
                
    elif choice == "Ayuda":
	       st.title("Documento") 
         
        
    elif choice == "About":
        
          st.markdown("<h1 style='text-align: center; color: black;'>SOBRE NOSOTROS</h1>", unsafe_allow_html=True)
          st.markdown("<h2 style='text-align: center; color: black;'>Daniel Giraldo</h2>", unsafe_allow_html=True)
          st.markdown('''<div style="display: flex; justify-content: center;">
                            <img src='data:image/png;base64,{}' class='img-fluid' width=148 height=256>'''.format(img_to_bytes("/Users/dsgiraldo/Desktop/FOTODANIEL.png")), unsafe_allow_html=True)
          st.markdown("")
          st.markdown("<h3 style='text-align: center; color: black;'>Ingeniero Industrial en formación, con énfasis en el campo de negocios y administración , alto dominio de Ingles, con certificaciones internacionales que lo verifican, con demostraciones de excelencia académica a lo largo de su vida bachiller y universitaria. Con habilidades en organización, gestión empresarial, liderazgo y trabajo en equipo; participación activa como líder en diversas actividades. Presenta una actitud ambiciosa y con cualidades aptas para lograr sus metas</h3>", unsafe_allow_html=True)
      
          st.markdown("<h2 style='text-align: center; color: black;'>Luigi Di Mare</h2>", unsafe_allow_html=True)
          st.markdown('''<div style="display: flex; justify-content: center;">
                        <img src='data:image/png;base64,{}' class='img-fluid' width=148 height=256>'''.format(img_to_bytes("/Users/dsgiraldo/Desktop/LUIGI.png")), unsafe_allow_html=True)
          st.markdown("")
          st.markdown("<h3 style='text-align: center; color: black;'>Me considero una persona responsable, creativa, empática y detallista. Tengo buenas habilidades para trabajar en equipo y estoy dispuesto a aprender cosas nuevas todos los días. Me gustan buscar soluciones, los nuevos retos y dar lo mejor de mí en todo momento.</h3>", unsafe_allow_html=True)
        



if __name__ == '__main__':
    main()
