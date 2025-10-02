import numpy as np
import pandas as pd
from tqdm import tqdm

import uproot
from ROOT import TFile, TEfficiency, TH1D, TGraphAsymmErrors, RDataFrame, TCanvas
import ROOT
from array import array
import ROOT, json
from math import nan

file_nu = uproot.open('icarus_numi_nue_mc_onbeam_offbeam_syst.root')
file_flux = uproot.open('2025-04-08_out_450.37_7991.98_79512.66.root')


flux_g4numi = file_flux['g4numi_reweight_v03_01-->v03_02;1/fhc;1']
flux_beam_focus = file_flux['beam_focusing_uncertainties;1/fhc;1']
flux_pca = file_flux['pca;1/principal_components;1']

nu_df = file_nu['events/full/selected;1']
nu_df=nu_df.arrays(library='pd')

hysyst_beam_horn_2kA = []
hysyst_beam_horn_m2kA = []
hysyst_beam_horn1_x_3mm = []
hysyst_beam_horn1_x_m3mm = []
hysyst_beam_horn1_y_3mm = []
hysyst_beam_horn1_y_m3mm = []
hysyst_beam_spot_1_3mm = []
hysyst_beam_spot_1_7mm = []
hysyst_beam_horn2_x_3mm = []
hysyst_beam_horn2_x_m3mm = []
hysyst_beam_horn2_y_3mm = []
hysyst_beam_horn2_y_3mm = []
hysyst_beam_horns_0mm_water = []
hysyst_beam_horns_2mm_water = []
hysyst_beam_Beam_shift_x_1mm = []
hysyst_beam_Beam_shift_x_m1mm = []
hysyst_beam_Beam_shift_y_1mm = []
hysyst_beam_Beam_shift_y_1mm = []
hysyst_beam_Target_z_7mm = []
hysyst_beam_Target_z_7mm = []
hpc_0 = []
hpc_1 = []
hpc_2 = []
hpc_3 = []
hpc_4 = []
hpc_5 = []
hpc_6 = []
hpc_7 = []
hpc_8 = []
hpc_9 = []
hpc_10 = []
hpc_11 = []
hpc_12 = []
hpc_13 = []
hpc_14 = []
hnom_k0l_weights = []
hnom_kpm_weights = []
hnom_pipm_weights = []
hnom_mu_weights = []
run = []
events =[]
subrun = []

sigma = np.array([3,2,1,0,-1,-2,-3])
abs_sigma = np.array([3,2,1,0,1,2,3])

for e,event in tqdm(nue_df.iterrows()):
    run.append(event['Run'])
    subrun.append(event['Subrun'])
    events.append(event['Evt'])
    pdg = event['true_pdg']
    parent_pdg = event['true_parent_pdg']
    nu_e = event['true_neutrino_energy']
    if abs(int(parent_pdg)) == 311: #K0
        if int(pdg) == 12:
            hnom_k0l_weights.append(flux_g4numi['hnom_nue_k0l_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_nue_k0l_weights;1'].axes[0].edges(),nu_e)-1])
        elif int(pdg) == -12:
            hnom_k0l_weights.append(flux_g4numi['hnom_nuebar_k0l_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_nuebar_k0l_weights;1'].axes[0].edges(),nu_e)-1])
        elif int(pdg) == 14:
            hnom_k0l_weights.append(flux_g4numi['hnom_numu_k0l_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_numu_k0l_weights;1'].axes[0].edges(),nu_e)-1])
        elif int(pdg) == -14:
            hnom_k0l_weights.append(flux_g4numi['hnom_numubar_k0l_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_numubar_k0l_weights;1'].axes[0].edges(),nu_e)-1])
        else:
            hnom_k0l_weights.append(flux_g4numi['hnom_k0l_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_k0l_weights;1'].axes[0].edges(),nu_e)-1])
        hnom_mu_weights.append(float("nan"))
        hnom_pipm_weights.append(float("nan"))
        hnom_kpm_weights.append(float("nan"))
    elif abs(int(parent_pdg)) == 321: #Kpm
        if int(pdg) == 12:
            hnom_kpm_weights.append(flux_g4numi['hnom_nue_kpm_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_nue_kpm_weights;1'].axes[0].edges(),nu_e)-1])
        elif int(pdg) == -12:
            hnom_kpm_weights.append(flux_g4numi['hnom_nuebar_kpm_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_nuebar_kpm_weights;1'].axes[0].edges(),nu_e)-1])
        elif int(pdg) == 14:
            hnom_kpm_weights.append(flux_g4numi['hnom_numu_kpm_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_numu_kpm_weights;1'].axes[0].edges(),nu_e)-1])
        elif int(pdg) == -14:
            hnom_kpm_weights.append(flux_g4numi['hnom_numubar_kpm_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_numubar_kpm_weights;1'].axes[0].edges(),nu_e)-1])
        else:
            hnom_kpm_weights.append(flux_g4numi['hnom_kpm_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_kpm_weights;1'].axes[0].edges(),nu_e)-1])
        hnom_mu_weights.append(float("nan"))
        hnom_pipm_weights.append(float("nan"))
        hnom_k0l_weights.append(float("nan"))
    elif abs(int(parent_pdg)) == 211: #pipm
        if int(pdg) == 12:
            hnom_pipm_weights.append(flux_g4numi['hnom_nue_pipm_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_nue_pipm_weights;1'].axes[0].edges(),nu_e)-1])
        elif int(pdg) == -12:
            hnom_pipm_weights.append(flux_g4numi['hnom_nuebar_pipm_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_nuebar_pipm_weights;1'].axes[0].edges(),nu_e)-1])
        elif int(pdg) == 14:
            hnom_pipm_weights.append(flux_g4numi['hnom_numu_pipm_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_numu_pipm_weights;1'].axes[0].edges(),nu_e)-1])
        elif int(pdg) == -14:
            hnom_pipm_weights.append(flux_g4numi['hnom_numubar_pipm_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_numubar_pipm_weights;1'].axes[0].edges(),nu_e)-1])
        else:
            hnom_pipm_weights.append(flux_g4numi['hnom_pipm_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_pipm_weights;1'].axes[0].edges(),nu_e)-1])      
        hnom_mu_weights.append(float("nan"))
        hnom_kpm_weights.append(float("nan"))
        hnom_k0l_weights.append(float("nan"))
    elif abs(int(parent_pdg)) == 13: #mu
        if int(pdg) == 12:
            hnom_mu_weights.append(flux_g4numi['hnom_nue_mu_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_nue_mu_weights;1'].axes[0].edges(),nu_e)-1])
        elif int(pdg) == -12:
            hnom_mu_weights.append(flux_g4numi['hnom_nuebar_mu_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_nuebar_mu_weights;1'].axes[0].edges(),nu_e)-1])
        elif int(pdg) == 14:
            hnom_mu_weights.append(flux_g4numi['hnom_numu_mu_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_numu_mu_weights;1'].axes[0].edges(),nu_e)-1])
        elif int(pdg) == -14:
            hnom_mu_weights.append(flux_g4numi['hnom_numubar_mu_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_numubar_mu_weights;1'].axes[0].edges(),nu_e)-1])
        else:
            hnom_mu_weights.append(flux_g4numi['hnom_mu_weights;1'].values()[np.searchsorted(flux_g4numi['hnom_mu_weights;1'].axes[0].edges(),nu_e)-1])
        hnom_pipm_weights.append(float("nan"))
        hnom_kpm_weights.append(float("nan"))
        hnom_k0l_weights.append(float("nan"))
    else:
        hnom_mu_weights.append(float("nan"))
        hnom_pipm_weights.append(float("nan"))
        hnom_kpm_weights.append(float("nan"))
        hnom_k0l_weights.append(float("nan"))
    if int(pdg) ==12:
        repeat+=1
        hysyst_beam_horn_2kA.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn_p2kA_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn_p2kA_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn_2kA[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn_m2kA_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn_m2kA_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_x_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn1_x_p3mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_x_p3mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_x_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn1_x_m3mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_x_m3mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_y_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn1_y_p3mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_y_p3mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_y_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn1_y_m3mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_y_m3mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_spot_1_3mm.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Beam_spot_1_3mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_spot_1_3mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_spot_1_7mm.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Beam_spot_1_7mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_spot_1_7mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_x_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn2_x_p3mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_x_p3mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_x_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn2_x_m3mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_x_m3mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_y_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn2_y_p3mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_y_p3mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_y_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn2_y_m3mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_y_m3mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horns_0mm_water.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Horns_0mm_water_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horns_0mm_water_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horns_2mm_water.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Horns_2mm_water_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horns_2mm_water_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_x_1mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Beam_shift_x_p1mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_x_p1mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_x_1mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Beam_shift_x_m1mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_x_m1mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_y_1mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Beam_shift_y_p1mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_y_p1mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_y_1mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Beam_shift_y_m1mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_y_m1mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Target_z_7mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Target_z_p7mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Target_z_p7mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Target_z_7mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Target_z_m7mm_fhc_nue;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Target_z_m7mm_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_0.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_0_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_0_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_1.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_1_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_1_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_2.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_2_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_2_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_3.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_3_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_3_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_4.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_4_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_4_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_5.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_5_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_5_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_6.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_6_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_6_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_7.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_7_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_7_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_8.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_8_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_8_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_9.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_9_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_9_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_10.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_10_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_10_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_11.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_11_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_11_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_12.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_12_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_12_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_13.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_13_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_13_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        hpc_14.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_14_fhc_nue;1'].values()[np.searchsorted(flux_pca['hpc_14_fhc_nue;1'].axes[0].edges(),nu_e)-1])))
        
    elif int(pdg) == -12:
        repeat+=1
        hysyst_beam_horn_2kA.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn_p2kA_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn_p2kA_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn_2kA[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn_m2kA_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn_m2kA_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_x_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn1_x_p3mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_x_p3mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_x_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn1_x_m3mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_x_m3mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_y_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn1_y_p3mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_y_p3mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_y_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn1_y_m3mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_y_m3mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_spot_1_3mm.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Beam_spot_1_3mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_spot_1_3mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_spot_1_7mm.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Beam_spot_1_7mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_spot_1_7mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_x_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn2_x_p3mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_x_p3mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_x_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn2_x_m3mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_x_m3mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_y_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn2_y_p3mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_y_p3mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_y_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn2_y_m3mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_y_m3mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horns_0mm_water.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Horns_0mm_water_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horns_0mm_water_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horns_2mm_water.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Horns_2mm_water_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horns_2mm_water_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_x_1mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Beam_shift_x_p1mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_x_p1mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_x_1mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Beam_shift_x_m1mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_x_m1mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_y_1mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Beam_shift_y_p1mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_y_p1mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_y_1mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Beam_shift_y_m1mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_y_m1mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Target_z_7mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Target_z_p7mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Target_z_p7mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Target_z_7mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Target_z_m7mm_fhc_nuebar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Target_z_m7mm_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_0.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_0_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_0_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_1.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_1_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_1_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_2.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_2_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_2_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_3.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_3_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_3_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_4.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_4_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_4_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_5.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_5_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_5_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_6.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_6_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_6_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_7.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_7_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_7_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_8.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_8_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_8_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_9.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_9_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_9_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_10.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_10_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_10_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_11.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_11_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_11_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_12.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_12_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_12_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_13.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_13_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_13_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        hpc_14.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_14_fhc_nuebar;1'].values()[np.searchsorted(flux_pca['hpc_14_fhc_nuebar;1'].axes[0].edges(),nu_e)-1])))
        
    elif int(pdg) ==14:
        repeat+=1
        hysyst_beam_horn_2kA.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn_p2kA_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn_p2kA_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn_2kA[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn_m2kA_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn_m2kA_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_x_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn1_x_p3mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_x_p3mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_x_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn1_x_m3mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_x_m3mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_y_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn1_y_p3mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_y_p3mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_y_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn1_y_m3mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_y_m3mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_spot_1_3mm.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Beam_spot_1_3mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_spot_1_3mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_spot_1_7mm.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Beam_spot_1_7mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_spot_1_7mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_x_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn2_x_p3mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_x_p3mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_x_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn2_x_m3mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_x_m3mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_y_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn2_y_p3mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_y_p3mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_y_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn2_y_m3mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_y_m3mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horns_0mm_water.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Horns_0mm_water_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horns_0mm_water_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horns_2mm_water.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Horns_2mm_water_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horns_2mm_water_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_x_1mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Beam_shift_x_p1mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_x_p1mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_x_1mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Beam_shift_x_m1mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_x_m1mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_y_1mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Beam_shift_y_p1mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_y_p1mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_y_1mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Beam_shift_y_m1mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_y_m1mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Target_z_7mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Target_z_p7mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Target_z_p7mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Target_z_7mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Target_z_m7mm_fhc_numu;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Target_z_m7mm_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_0.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_0_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_0_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_1.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_1_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_1_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_2.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_2_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_2_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_3.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_3_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_3_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_4.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_4_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_4_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_5.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_5_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_5_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_6.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_6_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_6_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_7.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_7_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_7_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_8.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_8_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_8_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_9.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_9_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_9_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_10.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_10_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_10_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_11.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_11_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_11_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_12.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_12_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_12_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_13.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_13_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_13_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        hpc_14.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_14_fhc_numu;1'].values()[np.searchsorted(flux_pca['hpc_14_fhc_numu;1'].axes[0].edges(),nu_e)-1])))
        
    elif int(pdg) == -14:
        repeat+=1
        hysyst_beam_horn_2kA.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn_p2kA_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn_p2kA_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn_2kA[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn_m2kA_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn_m2kA_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_x_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn1_x_p3mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_x_p3mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_x_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn1_x_m3mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_x_m3mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_y_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn1_y_p3mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_y_p3mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn1_y_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn1_y_m3mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn1_y_m3mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_spot_1_3mm.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Beam_spot_1_3mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_spot_1_3mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_spot_1_7mm.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Beam_spot_1_7mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_spot_1_7mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_x_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn2_x_p3mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_x_p3mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_x_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn2_x_m3mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_x_m3mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_y_3mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Horn2_y_p3mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_y_p3mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horn2_y_3mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Horn2_y_m3mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horn2_y_m3mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horns_0mm_water.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Horns_0mm_water_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horns_0mm_water_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_horns_2mm_water.append(list(map(lambda x: x + 1, sigma*flux_beam_focus['hsyst_beam_Horns_2mm_water_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Horns_2mm_water_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_x_1mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Beam_shift_x_p1mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_x_p1mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_x_1mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Beam_shift_x_m1mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_x_m1mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_y_1mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Beam_shift_y_p1mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_y_p1mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Beam_shift_y_1mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Beam_shift_y_m1mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Beam_shift_y_m1mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Target_z_7mm.append(list(map(lambda x: x + 1, abs_sigma[0:4]*flux_beam_focus['hsyst_beam_Target_z_p7mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Target_z_p7mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hysyst_beam_Target_z_7mm[-1].extend(list(map(lambda x: x + 1, abs_sigma[4:]*flux_beam_focus['hsyst_beam_Target_z_m7mm_fhc_numubar;1'].values()[np.searchsorted(flux_beam_focus['hsyst_beam_Target_z_m7mm_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_0.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_0_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_0_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_1.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_1_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_1_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_2.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_2_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_2_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_3.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_3_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_3_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_4.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_4_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_4_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_5.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_5_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_5_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_6.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_6_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_6_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_7.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_7_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_7_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_8.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_8_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_8_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_9.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_9_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_9_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_10.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_10_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_10_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_11.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_11_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_11_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_12.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_12_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_12_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_13.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_13_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_13_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
        hpc_14.append(list(map(lambda x: x + 1, sigma*flux_pca['hpc_14_fhc_numubar;1'].values()[np.searchsorted(flux_pca['hpc_14_fhc_numubar;1'].axes[0].edges(),nu_e)-1])))
def ensure_dir(rootdir, path):
    cur = rootdir
    for part in path.strip("/").split("/"):
        d = cur.GetDirectory(part) or cur.mkdir(part)
        cur = d
    return cur

# Constructors & casters
CTOR_VEC = {
    "f": lambda: ROOT.std.vector('float')(),
    "d": lambda: ROOT.std.vector('double')(),
    "i": lambda: ROOT.std.vector('int')(),
    "l": lambda: ROOT.std.vector('long long')(),
}
CAST = {"f": float, "d": float, "i": int, "l": int}
LEAF = {"f": "F", "d": "D", "i": "I", "l": "L"}
INT_SENTINEL = -9999

f = ROOT.TFile('/Users/danielcarber/Documents/ICARUS/icarus_numi_nue_mc_onbeam_offbeam_syst.root', "UPDATE")

# -------- your existing spec (some keys might be 1D scalars, some 2D lists-of-7) --------
spec = {
    "Run": ("i", run),
    "Subrun": ("i", subrun),
    "Evt": ("i", events),
    "hysyst_beam_horn_2kA_v": ("f", hysyst_beam_horn_2kA),
    "hysyst_beam_horn1_x_3mm_v": ("f", hysyst_beam_horn1_x_3mm),
    "hysyst_beam_horn1_y_3mm_v": ("f", hysyst_beam_horn1_y_3mm),
    "hysyst_beam_spot_1_3mm_v": ("f", hysyst_beam_spot_1_3mm),
    "hysyst_beam_spot_1_7mm_v": ("f", hysyst_beam_spot_1_7mm),
    "hysyst_beam_horn2_x_3mm_v": ("f", hysyst_beam_horn2_x_3mm),
    "hysyst_beam_horn2_y_3mm_v": ("f", hysyst_beam_horn2_y_3mm),
    "hysyst_beam_horns_0mm_water_v": ("f", hysyst_beam_horns_0mm_water),
    "hysyst_beam_horns_2mm_water_v": ("f", hysyst_beam_horns_2mm_water),
    "hysyst_beam_Beam_shift_x_1mm_v": ("f", hysyst_beam_Beam_shift_x_1mm),
    "hysyst_beam_Beam_shift_y_1mm_v": ("f", hysyst_beam_Beam_shift_y_1mm),
    "hysyst_beam_Target_z_7mm_v": ("f", hysyst_beam_Target_z_7mm),
    "hysyst_hpc_0_v": ("f", hpc_0), "hysyst_hpc_1_v": ("f", hpc_1), "hysyst_hpc_2_v": ("f", hpc_2),
    "hysyst_hpc_3_v": ("f", hpc_3), "hysyst_hpc_4_v": ("f", hpc_4), "hysyst_hpc_5_v": ("f", hpc_5),
    "hysyst_hpc_6_v": ("f", hpc_6), "hysyst_hpc_7_v": ("f", hpc_7), "hysyst_hpc_8_v": ("f", hpc_8),
    "hysyst_hpc_9_v": ("f", hpc_9), "hysyst_hpc_10_v": ("f", hpc_10), "hysyst_hpc_11_v": ("f", hpc_11),
    "hysyst_hpc_12_v": ("f", hpc_12), "hysyst_hpc_13_v": ("f", hpc_13), "hysyst_hpc_14_v": ("f", hpc_14),
}

# ------------ helpers to detect 2D-of-7 vs 1D -------------
def is_2d_of_7(seq):
    # True if seq is list/tuple of rows and each row is length 7 (allow None rows gracefully)
    if not seq or not hasattr(seq, '__iter__'): return False
    first = seq[0]
    if not hasattr(first, '__iter__'): return False
    # tolerate ragged with Nones, but require length 7 when present
    return all((row is None) or (hasattr(row, '__iter__') and len(row) == 7) for row in seq)

def is_1d(seq):
    return not is_2d_of_7(seq)

# Partition keys
keys_2d7 = [k for k, (_, v) in spec.items() if is_2d_of_7(v)]
keys_1d  = [k for k, (_, v) in spec.items() if not is_2d_of_7(v)]

# Derive number of entries N from whichever group is present
if keys_2d7:
    N = len(spec[keys_2d7[0]][1])
elif keys_1d:
    N = len(spec[keys_1d[0]][1])
else:
    raise ValueError("spec is empty")

# Sanity: lengths consistent
for k in keys_2d7:
    if len(spec[k][1]) != N:
        raise ValueError(f"{k}: outer length {len(spec[k][1])} != {N}")
for k in keys_1d:
    if len(spec[k][1]) != N:
        raise ValueError(f"{k}: length {len(spec[k][1])} != {N}")

# ------------ build tree in the desired directory -------------
tdir = ensure_dir(f, "events/full")
tdir.cd()

t = ROOT.TTree("NuMIfluxsim", "per-entry vectors (len=7) plus scalars")
branch_order = list(spec.keys())
tdir.WriteObject(ROOT.TObjString(json.dumps(branch_order)), "branch_labels_json")

# Create branches
# A) 2D-of-7 branches -> std::vector per entry (length 7)
vec_br = {}  # name -> (vec, code, rows)
for name in keys_2d7:
    code, rows = spec[name]
    vec = CTOR_VEC[code]()  # pick float/double/int vector as requested
    t.Branch(name, vec)
    vec_br[name] = (vec, code, rows)

# B) 1D scalar branches -> scalar C buffers
sca_br = {}  # name -> (buf, code, seq)
for name in keys_1d:
    code, seq = spec[name]
    buf = array('f' if code in ('f','d') else 'i', [0.0] if code in ('f','d') else [0])
    t.Branch(name, buf, f"{name}/{LEAF[code]}")
    sca_br[name] = (buf, code, seq)

# ------------ fill: one entry per row; vectors length 7 -------------
for i in range(N):
    # fill 2D-of-7 vectors
    for name, (vec, code, rows) in vec_br.items():
        vec.clear()
        row = rows[i]
        if row is None:
            # push 7 NaNs (floats) / sentinels (ints)
            if code in ('f','d'):
                for _ in range(7): vec.push_back(nan)
            else:
                for _ in range(7): vec.push_back(INT_SENTINEL)
        else:
            for x in row:  # row length is 7 by construction
                if x is None:
                    vec.push_back(nan if code in ('f','d') else INT_SENTINEL)
                else:
                    vec.push_back(CAST[code](x))
    # fill 1D scalars
    for name, (buf, code, seq) in sca_br.items():
        x = seq[i]
        if x is None:
            buf[0] = (nan if code in ('f','d') else INT_SENTINEL)
        else:
            buf[0] = CAST[code](x)
    t.Fill()

tdir.WriteTObject(t, t.GetName(), "Overwrite")
f.Close()
