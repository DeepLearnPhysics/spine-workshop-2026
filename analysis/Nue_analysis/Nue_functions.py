import math
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

import os
from plotly.subplots import make_subplots
from plotly import tools
import plotly.offline as pyo
import sys
from tqdm import tqdm
import re
def pur_plot(df_pur,df_eff,metric, bounds,bin_size, xaxis_name, Plot_title, selection,cut,flip=False):
    fig = make_subplots(rows=1,cols=1,subplot_titles = (Plot_title,))


    energy_limit = bounds[1]
    accuracy_sel,accuracy_1eNp,accuracy_nue=[],[],[]
    eff_sel,eff_1eNp,eff_nue=[],[],[]
    counts=[]
    energy_bin,eff_bin = [],[]
        
    total_num = (df_pur['true_category'] == '0') | (df_pur['true_category'] == '1')
    b=cut[0]
    while b <  cut[1]:
        if flip is True:
            low_bin = (df_pur[metric] <=cut[1]) &(df_pur[metric] >b)
        else:
            low_bin = (df_pur[metric] >=cut[0]) &(df_pur[metric] <b)
        inter = df_pur[low_bin]
        b+=cut[2]
        if len(inter) == 0:
            accuracy_sel.append(0)   
        else:
            mask_signal = (inter['true_category'] == 0) | (inter['true_category'] == 1)
            accuracy_sel.append(sum(mask_signal)/len(inter))
                
            
        energy_bin.append(b)

    d=cut[0]
    while d <  cut[1]:
        if flip is True:
            low_bin = (df_eff[metric] <=cut[1]) &(df_eff[metric] >d)
        else:
            low_bin = (df_eff[metric] >=cut[0]) &(df_eff[metric] <d)
        inter = df_eff[low_bin]
        d+=cut[2]
        if len(inter) == 0:
            eff_sel.append(0)    
        else:
            #mask_signal = (df_eff[metric]>= cut[0]) | (df_eff[metric]< cut[1])
            eff_sel.append(len(inter)/len(df_eff))            
        eff_bin.append(d)
    #Create the masks for histograms
    fig.add_trace(go.Scatter(x=energy_bin, y=accuracy_sel,marker_color = 'blue',name = 'Purity',mode='markers'),row = 1, col =1)
    fig.add_trace(go.Scatter(x=eff_bin, y=eff_sel,marker_color = 'red',name = 'Efficiency',mode='markers'),row = 1, col =1)
    F1 = np.multiply(eff_sel,accuracy_sel)
    print(f"Efficiency: {int(eff_sel[np.argmax(F1)]*100)}%")
    print(f"Purity: {int(accuracy_sel[np.argmax(F1)]*100)}%")
    fig.add_trace(go.Scatter(x=eff_bin, y=F1,marker_color = 'purple',name = f'F1:{energy_bin[np.argmax(F1)]:.2f}',mode='markers',),row = 1, col =1)
    print("Max F1 Score:",np.max(F1))
    fig.add_trace(go.Scatter(x=[energy_bin[np.argmax(F1)],energy_bin[np.argmax(F1)]], y=[0,1],
                    mode='lines',
                    name='lines',showlegend = False))
    
    fig.update_layout(font = dict(size=20),legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=1.05,
        bgcolor="LightSteelBlue",
            bordercolor="Black",
    ))
    
    fig.update_xaxes(title_text = xaxis_name,row = 1, col = 1)
    fig.update_annotations(font_size=36)
    fig.update_yaxes(title_text = "Performance ",row = 1, col = 1)
    fig.update_layout(barmode='stack')
    fig.update_layout(xaxis = dict(range = [bounds[0],bounds[1]]))
    fig.update_layout(yaxis = dict(range = [0,1]))
    fig.update_layout(height = 700, width = 1200,showlegend = True)
    fig.show()
                  
def print_toml_line(cfg_path, line = None):
    i=0
    if line is None:
        print("No Line input. Have fun with your toml file")
    else:
        with open(cfg_path, 'r') as f:
            line_num = line
            for l in f:
                i+=1
                if i < (line_num+3) and i > line_num-3:
                    print("Line",i,":",l)

def background_breakdown(df,category,background_output = 'true', print_energy = False):
    gamma,electron,muon,pion, proton = None,None,None,None,None
    true_list = []
    reco_list = []
    true_events = []
    reco_events = []
    df = df[df['true_category'] == category]
    energy_list = df['true_visible_energy'].values
    for index, event in df.iterrows():
        true_events.append([int(event['true_photon_multiplicity']), int(event['true_electron_multiplicity']),int(event['true_muon_multiplicity']), int(event['true_pion_multiplicity']), int(event['true_proton_multiplicity'])])
        reco_events.append([int(event['reco_photon_multiplicity']), int(event['reco_electron_multiplicity']), int(event['reco_muon_multiplicity']), int(event['reco_pion_multiplicity']), int(event['reco_proton_multiplicity'])])
    for true_event, reco_event in zip(true_events,reco_events):
        true_topo = ""
        reco_topo = ""
        for i,t in enumerate(true_event):
            if t != "0":
                if i == 4:
                    proton = f"{t}p"
                    true_topo+=f"{t}p"
                elif i == 3:
                    pion = f"{t}pi"
                    true_topo+=f"{t}pi"
                elif i == 2:
                    muon = f"{t}m"
                    true_topo+=f"{t}m"
                elif i == 1:
                    electron = f"{t}e"
                    true_topo+=f"{t}e"
                elif i == 0:
                    gamma = f"{t}g"
                    true_topo+=f"{t}g"
        for i,t in enumerate(reco_event):
            if t != "0":
                if i == 4:
                    proton = f"{t}p"
                    reco_topo+=f"{t}p"
                elif i == 3:
                    pion = f"{t}pi"
                    reco_topo+=f"{t}pi"
                elif i == 2:
                    muon = f"{t}m"
                    reco_topo+=f"{t}m"
                elif i == 1:
                    electron = f"{t}e"
                    reco_topo+=f"{t}e"
                elif i == 0:
                    gamma = f"{t}g"
                    reco_topo+=f"{t}g"
        
        true_list.append(true_topo)
        reco_list.append(reco_topo)
                
    df_topo = {}
    if background_output == 'true':
        for t, r in zip(true_list,reco_list):
            if t not in df_topo.keys():
                df_topo[t] =1
            else:
                df_topo[t]+=1
        df_topo = dict(sorted(df_topo.items(), key=lambda item: item[1]))
        print(df_topo)
        print(len(true_list))
    elif  background_output == 'reco':
        for t, r in zip(true_list,reco_list):
            if r not in df_topo.keys():
                df_topo[r] =1
            else:
                df_topo[r]+=1
        df_topo = dict(sorted(df_topo.items(), key=lambda item: item[1]))
        print(df_topo)
        print(len(reco_list))
    if print_energy is True:
        with open("Background_energy.txt", "w") as file:
            for item in energy_list:
                file.write(f"{item}\n")
