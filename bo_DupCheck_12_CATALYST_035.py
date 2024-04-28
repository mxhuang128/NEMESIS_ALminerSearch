"""
Duplication Check for ALMA Cycle 11 Large Program - NEMESIS
Software Required: 
Python 3.10.14 (on joppe, using conda environment)
ALminer (https://alminer.readthedocs.io/en/latest/)

* compared to originally shared DupCheck_12_CATALYST_*.py in slack channel, this version is tweaked to include all bonus lines
    - this is based on "Molecule List 2024"
    - include OCS and H2CS lines, and additional CCH line
by Monica Huang, April 2024
"""
# Import packages
import alminer
import numpy as np

# Read galaxies from target list, mainly for (z, beam_requested_in_LP, target_name)
Target_info = np.genfromtxt("ListTargets_12_CATALYST.txt",skip_header=1,skip_footer=2,dtype=['U10',float,float,float,float])
N_targets = len(Target_info)

# Loop over each target - 
#     in search for archival data meeting the duplicate criteria for all target molecular transitions in all SGs
#     then write them into output txt files for keyword search and compile - for sharing among collaborators (JM & EB)
for tg in range(N_targets):
    TG = Target_info[tg][0]
    Redshift = Target_info[tg][2]
    Beam_max = Target_info[tg][4] * 2.0 #twice the aimed beam for duplication search
    f = open("bo_035_"+TG+"_"+"DupliCheck.txt","a")
    print(TG,file=f)
    print('=========================================================',file=f)
    myquery = alminer.target([TG], public=None, point=False, search_radius=1.0)
    print('================B3a ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*375)]
    MOL = ["HCN", "HCOp", "HNC", "CH3CN", "H2CS", "H2CS"]
    List_Names = [" 1-0", " 1-0", " 1-0", " 5(0)-4(0)", " 3(1,3)-2(1,2)", " 3(0,3)-2(0,2)"]
    List_Lines = [88.632, 89.1885247, 90.664, 91.987, 101.477885, 103.040548]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)  
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)

    print('=========================================================',file=f)
    print('================B3b ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*650)]
    MOL = ["CH3OH", "SO", "SiO", "HNCO", "OCS", "CH3OH", "CS", "SO"]
    List_Names = [" 5(-1)-4(0)", " 2_2-1_1", " 2-1", " 4-3", " 8-7", " 2(1)-1(1)", " 2-1", " 3(2)-2(1)"]
    List_Lines = [84.521172, 86.09, 86.847, 87.9252, 97.301208, 97.582798, 97.981, 99.3]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)

    print('=========================================================',file=f)
    print('================B4a ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*1020)]
    MOL = ["CH3CN", "SO", "SiO", "HNCO"]
    List_Names = [" 7(0)-6(0)", " 3_3-2_2", " 3-2", " 6-5"]
    List_Lines = [128.779, 129.14, 130.269, 131.8857]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)

    print('=========================================================',file=f)
    print('================B4b ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*1540)]
    MOL = ["SO", "SO", "CS", "CH3CN", "H2CS"]
    List_Names = [" 6_5-5_5", "4(3)-3(2) ", " 3-2", " 8(0)-7(0)", " 4(0,4)-3(0,3)"]
    List_Lines = [136.63, 138.18, 146.969, 147.175, 137.371293]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)

    print('=========================================================',file=f)
    print('================B5a ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*1800)]
    MOL = ["CH3OH", "CH3CN", "HNCO", "HCN", "HCOp", "SO"]
    List_Names = [" 5(1)-5(0)", " 9(0)-8(0)", " 8-7", " 2-1", " 2-1", " 5(4)-4(3)"]
    List_Lines = [165.369341, 165.569, 175.8437, 177.26, 178.375,178.61 ]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)

    print('=========================================================',file=f)
    print('================B5b ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*1050)]
    MOL = ["H2CS", "CH3OH", "OCS", "SO", "HNC", "OCS", "CH3CN"]
    List_Names = [" 5(1,5)-4(1,4)", " 3(2)-2(1)", " 14-13", " 4(4)-3(3)", " 2-1", " 15-14", " 10(0)-9(0)"]
    List_Lines = [169.113529, 170.060581, 170.267, 172.18, 181.32, 182.427, 183.962]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)

    print('=========================================================',file=f)
    print('================B5c ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*2500)]
    MOL = ["CH3OH", "OCS", "CS", "SO", "OCS"]
    List_Names = [" 4(0,4)-3(0,3)", " 16-15", " 4-3", " 5_4-4_3", " 17-16"]
    List_Lines = [193.41, 194.586433, 195.954, 206.18, 206.7451558]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)

    print('=========================================================',file=f)
    print('================B5d ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*1400)]
    MOL = ["CCH", "SiO", "HNCO"]
    List_Names = [" 2-1", " 4-3", " 8-7"]
    List_Lines = [174.663222, 173.68831, 175.843695]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)

    print('=========================================================',file=f)
    print('================B6a ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*1400)]
    MOL = ["CS", "CH3CN", "SO", "SiO", "E-CH3OH", "SO"]
    List_Names = [" 5-4", " 14(0)-13(0)", " 6_6-5_5", " 6-5", " 2(-1)-1(0)", " 6_7-5_6"]
    List_Lines = [244.935, 257.527, 258.26, 260.518, 261.805675, 261.844]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)

    print('=========================================================',file=f)
    print('================B6b ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*2200)]
    MOL = ["SO", "HCN", "CH3OH", "HCOp"]
    List_Names = [" 5(6)-4(5)", " 3-2", " 5(2,3)-4(1,3)", " 3-2"]
    List_Lines = [251.825, 265.89, 266.838148, 267.558]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)

    print('=========================================================',file=f)
    print('================B6c ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*2700)]
    MOL = ["CH3CN", "SO", "HNC"]      
    List_Names = [" 14(0)-13(0)", " 6_6-5_5", " 3-2"]
    List_Lines = [257.527, 258.26, 271.98]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)

    print('=========================================================',file=f)
    print('================B6d ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*2400)]
    MOL = ["CCH", "SO", "HCN"]
    List_Names = [" 3-2", " 6_5-5_4", " 3-2"]
    List_Lines = [262.067469, 251.8, 265.9]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)

    print('=========================================================',file=f)
    print('================B7a ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*1300)]
    MOL = ["H2CO", "H2CO", "H2CO", "H2CO", "CS", "CH3OH", "SiO", "SO", "CH3OH"]
    List_Names = [" 4(2,3)-3(2,2)", " 4(3,2)-3(3,1)", " 4(3,1)-3(3,0)", " 4(2,2)-3(2,1)", " 6-5", " 1(1,0)-1(0,1)", " 7-6", " 8(7)-7(6)", " 3(1,2)-3(0,3)"]
    List_Lines = [291.237766, 291.380442, 291.384361, 291.948067, 293.912, 303.366921, 303.927, 304.08, 305.473491]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)

    print('=========================================================',file=f)
    print('================B7b ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*2100)]
    MOL = ["CS", "SO", "HCN", "HCOp"]   
    List_Names = [" 7-6", " 8_8-7_7", " 4-3", " 4-3"]
    List_Lines = [342.883, 344.31, 354.51, 356.734]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)

    print('=========================================================',file=f)
    print('================B7c ====================',file=f)
    selected = myquery[(myquery['ang_res_arcsec'] < Beam_max) & (myquery['vel_res_kms'] < 20.0) & (myquery['line_sens_10kms']<2.0*1000)]
    MOL = ["SiO", "CCH", "CH3CN", "HNC"]
    List_Names = [" 8-7", " 4-3", " 19(0)-18(0)", " 4-3"]
    List_Lines = [347.33, 349.35, 349.454, 362.63]
    N_lines = len(List_Lines)
    for n in range(N_lines):
        myline_obs_SPC = alminer.line_coverage(selected, line_freq=List_Lines[n], z=Redshift,line_name=MOL[n]+List_Names[n], print_targets=True, print_summary=True)
        print(MOL[n]+List_Names[n]+"--- --- ---",file=f)
        print(myline_obs_SPC['project_code'],file=f)
        print(myline_obs_SPC['ang_res_arcsec'],file=f)
        print(myline_obs_SPC['LAS_arcsec'],file=f)
        print(myline_obs_SPC['vel_res_kms'],file=f)
        print(myline_obs_SPC['line_sens_10kms'],file=f)
        print(myline_obs_SPC['min_freq_GHz'],file=f)
        print(myline_obs_SPC['max_freq_GHz'],file=f)
    print('======================== FIN =================================',file=f)

    f.close()
