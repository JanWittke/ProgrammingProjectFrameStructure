#Hello! This is your tool for a preselection of  a steel frame!
#First we have to enter the variabels

x = 1 #No other variants for static systems are available yet

V = input("Enter the needed Height, Wide and Length of your hall in [m]: (H,W,L): ")
V_einzeln = V.split(',')

H = V_einzeln[0]
W = V_einzeln[1]
L_total = V_einzeln[2]

H = float(H)
W = float(W)
L_total = float(L_total)

if H < 3 or W < 6 or L_total < 15:
    print("The Height should be between 3 and 20 [m].")
    print("The Wide should be between 6 and 30 [m].")
    print("The Length should be between 15 and 200 [m].")
    quit()
if H > 20 or W > 30 or L_total > 200:
    print("The Height should be between 3 and 20 [m].")
    print("The Wide should be between 6 and 30 [m].")
    print("The Length should be between 15 and 200 [m].")
    quit()


Load =  input("Enter the snow load s_k and the wind load w_k in [kN/m2]: (s_k,w_k): ")
Load_split = Load.split(',')

sk = Load_split[0]
wk = Load_split[1]

sk = float(sk)
wk = float(wk)

#=============================================================================================================

if L_total <= 20:
    X = L_total/5
    X = round(X)
    Q = L_total/X

elif L_total <= 40:
    X = L_total/6
    X = round(X)
    Q = L_total/X

elif L_total <= 60:
    X = L_total/7
    X = round(X)
    Q = L_total/X

elif L_total <= 80:
    X = L_total/8
    X = round(X)
    Q = L_total/X

elif L_total <= 100:
    X = L_total/10
    X = round(X)
    Q = L_total/X

elif L_total < 100:
    X = L_total/12
    X = round(X)
    Q = L_total/X

L_section = Q.__round__(2)


print("The hall is divided into",X,"sections with a distance of",L_section,"[m]. In total we have",X+1,"frames.")


sd = sk * 1.5 * L_section #kN/m
wd = wk * 1.5 * L_section #kN/m

sd = sd.__round__(2)
wd = wd.__round__(2)

print("This results in design line loads for the snow load of s_d =",sd,"[kN/m] and for the wind load of w_d =",wd,"[kN/m].")


#Calculation of the internal forces on a three hinged frame
#Snowload =======================================================================================================
# M = moment
# Q = shear force (Querkraft)
# N = axial force (Normalkraft)



Ma_sd = 0
Mb_sd = - sd * (W**2)/8
Mc_sd = Mb_sd
Md_sd = 0
Me_sd = Mb_sd
Mf_sd = Me_sd
Mg_sd = 0
Moment_P_sd = [Ma_sd,Mb_sd,Mc_sd,Md_sd,Me_sd,Mf_sd,Mg_sd] #P = point
round_Moment_P_sd = [round(num, 2) for num in Moment_P_sd]

M1_sd = Mb_sd
M2_sd = Mb_sd
M3_sd = Mb_sd
M4_sd = Mb_sd
Moment_E_sd = [M1_sd,M2_sd,M3_sd,M4_sd] #E = element
round_Moment_E_sd = [round(num, 2) for num in Moment_E_sd]

#print("M_sd: a,b,c,d,e,f,g :",round_Moment_P_sd,)
#print("M_sd: 1,2,3,4 :",round_Moment_E_sd,)
#print("                 linear, quadratic, quadratic, linear")

Qa_sd = Mb_sd/H
Qb_sd = Qa_sd
Qc_sd = sd * W/2
Qd_sd = 0
Qe_sd = - Qc_sd
Qf_sd = -Qa_sd
Qg_sd = Qf_sd
Shear_force_P_sd = [Qa_sd,Qb_sd,Qc_sd,Qd_sd,Qe_sd,Qf_sd,Qg_sd]
round_Shear_force_P_sd = [round(num, 2) for num in Shear_force_P_sd]

Q1_sd = Qa_sd
Q2_sd = Qc_sd
Q3_sd = Qe_sd
Q4_sd = Qf_sd
Shear_force_E_sd = [Q1_sd,Q2_sd,Q3_sd,Q4_sd]
round_Shear_force_E_sd = [round(num, 2) for num in Shear_force_E_sd]

#print("Q_sd: a,b,c,d,e,f,g :",round_Shear_force_P_sd,)
#print("Q_sd: 1,2,3,4 :",round_Shear_force_E_sd,)
#print("                 constant, linear, linear, constant")

Av_sd = sd * W/2
Gv_sd = Av_sd

N1_sd = - Av_sd
N2_sd = Q1_sd
N3_sd = N2_sd
N4_sd = N1_sd
Normal_force_sd = [N1_sd,N2_sd,N3_sd,N4_sd]
round_Normal_force_sd = [round(num, 2) for num in Normal_force_sd]

Normal_force_P_sd = [N1_sd,N1_sd,N2_sd,N2_sd,N3_sd,N4_sd,N4_sd]
round_Normal_force_P_sd = [round(num, 2) for num in Normal_force_P_sd]

#print("N_sd: a,b,c,d,e,f,g :",round_Normal_force_P_sd,)
#print("N_sd: 1,2,3,4 :",round_Normal_force_sd,)
#print("                 constant, constant, constant, constant")

#one-sided wind load =================================================================================

Gv_wd = (wd*H**2)/(2*W)
Av_wd = -Gv_wd

Gh_wd = (Gv_wd*W)/(2*H)
Qg_wd = Gh_wd

N4_wd = - Gv_wd
N1_wd = -Av_wd

Q3_wd = N4_wd
Md_wd = Q3_wd*W/2

Ma_wd = 0
Mb_wd = - Md_wd
Mc_wd = Mb_wd
Md_wd = 0
Me_wd = -Mb_wd
Mf_wd = Me_wd
Mg_wd = 0
Moment_P_wd = [Ma_wd,Mb_wd,Mc_wd,Md_wd,Me_wd,Mf_wd,Mg_wd] #P = point
round_Moment_P_wd = [round(num, 2) for num in Moment_P_wd]

M1_wd = Mb_wd*2/3 + (wd*(H**2))/9 # this formula is not fully correct but for the moments its ok because this value is not relevant
M2_wd = Mb_wd
M3_wd = Me_wd
M4_wd = Mf_wd
Moment_E_wd = [M1_wd,M2_wd,M3_wd,M4_wd] #E = element
round_Moment_E_wd = [round(num, 2) for num in Moment_E_wd]

#print("M_wd: a,b,c,d,e,f,g :",round_Moment_P_wd,)
#print("M_wd: 1,2,3,4 :",round_Moment_E_wd,)
#print("                 quadratic, linear, linear, linear")
M1_wd = Mb_wd #the moment is changed here again, so that the corner moment is decisive for M_ges.
Moment_E_wd = [M1_wd,M2_wd,M3_wd,M4_wd] #E = element #saved again


Qa_wd = -Qg_wd + wd*H
Qb_wd = -Qg_wd
Qc_wd = N4_wd
Qd_wd = N4_wd
Qe_wd = N4_wd
Qf_wd = Qg_wd
Qg_wd = Qg_wd
Shear_force_P_wd = [Qa_wd,Qb_wd,Qc_wd,Qd_wd,Qe_wd,Qf_wd,Qg_wd]
round_Shear_force_P_wd = [round(num, 2) for num in Shear_force_P_wd]

Q1_wd = Qa_wd
Q2_wd = Qc_wd
Q3_wd = Qe_wd
Q4_wd = Qf_wd
Shear_force_E_wd = [Q1_wd,Q2_wd,Q3_wd,Q4_wd]
round_Shear_force_E_wd = [round(num, 2) for num in Shear_force_E_wd]

#print("Q_wd: a,b,c,d,e,f,g :",round_Shear_force_P_wd,)
#print("Q_wd: 1,2,3,4 :",round_Shear_force_E_wd,)
#print("                 linear, constant, constant, constant")

N1_wd = -Av_wd
N2_wd = -Q4_wd
N3_wd = -Q4_wd
N4_wd = - Gv_wd
Normal_force_wd = [N1_wd,N2_wd,N3_wd,N4_wd]
round_Normal_force_wd = [round(num, 2) for num in Normal_force_wd]

Normal_force_P_wd = [N1_wd,N1_wd,N2_wd,N2_wd,N3_wd,N4_wd,N4_wd]
round_Normal_force_P_wd = [round(num, 2) for num in Normal_force_P_wd]

#print("N_wd: a,b,c,d,e,f,g :",round_Normal_force_P_wd,)
#print("N_wd: 1,2,3,4 :",round_Normal_force_wd,)
#print("                 constant, constant, constant, constant")

# We are looking for the maximal internal forces ==============================================================================================
# Load combination 1 -> Snow as relevant force
# Load combination 2 -> Wind as relevant force
# First for the moment =======================================================================================================================

round_Moment_P_wd_60 = [i * 0.6 for i in round_Moment_P_wd]
round_Moment_P_sd_50 = [i * 0.5 for i in round_Moment_P_sd]

total_Moment_LK1 = [i + j for i, j in zip(round_Moment_P_sd, round_Moment_P_wd_60)]
total_Moment_LK1 = [round(num, 2) for num in total_Moment_LK1]
#print("M_total_LK1: a,b,c,d,e,f,g:" ,total_Moment_LK1,)

total_Moment_LK2 = [i + j for i, j in zip(round_Moment_P_sd_50, round_Moment_P_wd)]
total_Moment_LK2 = [round(num, 2) for num in total_Moment_LK2]
#print("M_total_LK2: a,b,c,d,e,f,g:" ,total_Moment_LK2,)

# Now determine the largest loads in terms of amount

abs_total_Moment_LK1 = [-i if i <0 else i for i in total_Moment_LK1 ]
abs_total_Moment_LK2 = [-i if i <0 else i for i in total_Moment_LK2 ]

#print(abs_total_Moment_LK1)
#print(abs_total_Moment_LK2)

M_d = [0,0,0,0,0,0,0]
i = 0
for x in range(0, 7):
    if abs_total_Moment_LK1[i] >= abs_total_Moment_LK2[i]:
        M_d[i] = abs_total_Moment_LK1[i]
    else:
        M_d[i] = abs_total_Moment_LK2[i]
    i = i+1
#print("|M_d|: a,b,c,d,e,f,g",M_d,)

#There is a special feature with the moment
#The corner moment does not necessarily have to be decisive for the calculation, but theoretically it could also be the field moment
#This will be checked in the following step and taken into account if necessary

M_d_feld = M_d[1]*(2/3) + (wd*(H**2))/9 # The formula here is again not 100% correct but already relatively accurate
M_d_feld = round(M_d_feld, 2)

#print(M_d_feld)
if M_d[1] >= M_d_feld:
    M_d[1] = M_d[1]
else:
    M_d[0] = M_d_feld

# Shear force =========================================================================================================
round_Shear_force_P_wd_60 = [i * 0.6 for i in round_Shear_force_P_wd]
round_Shear_force_P_sd_50 = [i * 0.5 for i in round_Shear_force_P_sd]

total_Shear_force_LK1 = [i + j for i, j in zip(round_Shear_force_P_sd, round_Shear_force_P_wd_60)]
total_Shear_force_LK1 = [round(num, 2) for num in total_Shear_force_LK1]
#print("Q_total_LK1: a,b,c,d,e,f,g:" ,total_Shear_force_LK1,)

total_Shear_force_LK2 = [i + j for i, j in zip(round_Shear_force_P_sd_50, round_Shear_force_P_wd)]
total_Shear_force_LK2 = [round(num, 2) for num in total_Shear_force_LK2]
#print("Q_total_LK2: a,b,c,d,e,f,g:" ,total_Shear_force_LK2,)

# Now determine the largest loads in terms of amount

abs_total_Shear_force_LK1 = [-i if i <0 else i for i in total_Shear_force_LK1 ]
abs_total_Shear_force_LK2 = [-i if i <0 else i for i in total_Shear_force_LK2 ]

#print(abs_total_Shear_force_LK1)
#print(abs_total_Shear_force_LK2)

Q_d = [0,0,0,0,0,0,0]
i = 0
for x in range(0, 7):
    if abs_total_Shear_force_LK1[i] >= abs_total_Shear_force_LK2[i]:
        Q_d[i] = abs_total_Shear_force_LK1[i]
    else:
        Q_d[i] = abs_total_Shear_force_LK2[i]
    i = i+1
#print("|Q_d|: a,b,c,d,e,f,g",Q_d,)

# Axial force = normal force =========================================================================================================
round_Normal_force_P_wd_60 = [i * 0.6 for i in round_Normal_force_P_wd]
round_Normal_force_P_sd_50 = [i * 0.5 for i in round_Normal_force_P_sd]

total_Normal_force_LK1 = [i + j for i, j in zip(round_Normal_force_P_sd, round_Normal_force_P_wd_60)]
total_Normal_force_LK1 = [round(num, 2) for num in total_Normal_force_LK1]
#print("N_total_LK1: a,b,c,d,e,f,g:" ,total_Normal_force_LK1,)

total_Normal_force_LK2 = [i + j for i, j in zip(round_Normal_force_P_sd_50, round_Normal_force_P_wd)]
total_Normal_force_LK2 = [round(num, 2) for num in total_Normal_force_LK2]
#print("N_total_LK2: a,b,c,d,e,f,g:" ,total_Normal_force_LK2,)

# Now determine the largest loads in terms of amount

abs_total_Normal_force_LK1 = [-i if i <0 else i for i in total_Normal_force_LK1 ]
abs_total_Normal_force_LK2 = [-i if i <0 else i for i in total_Normal_force_LK2 ]

#print(abs_total_Normal_force_LK1)
#print(abs_total_Normal_force_LK2)

N_d = [0,0,0,0,0,0,0]
i = 0
for x in range(0, 7):
    if abs_total_Normal_force_LK1[i] >= abs_total_Normal_force_LK2[i]:
        N_d[i] = abs_total_Normal_force_LK1[i]
    else:
        N_d[i] = abs_total_Normal_force_LK2[i]
    i = i+1
#print("|N_d|: a,b,c,d,e,f,g",N_d,)

# Now the whole thing is brought to the component level
# First group M,Q,N for the column and the truss
# Then finally build a list, the M,Q,N for the column and the truss respectively. This list can be used later for the calculation

M_max_value_truss = max(M_d[2:5])
#print("M maximum value in the truss:", M_max_value_truss)

M_max_value_1 = max(M_d[0:2])
M_max_value_2 = max(M_d[5:7])
if M_max_value_1 >= M_max_value_2:
    M_max_value_pillar = M_max_value_1
else:
    M_max_value_pillar = M_max_value_2

#print("M maximum value in the pillar:", M_max_value_pillar)


Q_max_value_truss = max(Q_d[2:5])
#print("Q maximum value in the truss:", Q_max_value_truss)

Q_max_value_1 = max(Q_d[0:2])
Q_max_value_2 = max(Q_d[5:7])
if Q_max_value_1 >= Q_max_value_2:
    Q_max_value_pillar = Q_max_value_1
else:
    Q_max_value_pillar = Q_max_value_2

#print("Q maximum value in the pillar:", Q_max_value_pillar)


N_max_value_truss = max(N_d[2:5])
#print("N maximum value in the truss:", N_max_value_truss)

N_max_value_1 = max(N_d[0:2])
N_max_value_2 = max(N_d[5:7])
if N_max_value_1 >= N_max_value_2:
    N_max_value_pillar = N_max_value_1
else:
    N_max_value_pillar = N_max_value_2

#print("N maximum value in the pillar:", N_max_value_pillar)

# Finally, build a component array with the respective design internal forces

Internal_forces_truss = [M_max_value_truss,Q_max_value_truss,N_max_value_truss]
print("The internal forces in the truss are: M_max =",Internal_forces_truss[0],"kNm; Q_max =",Internal_forces_truss[1],"kN; N_max =",-Internal_forces_truss[2],"kN !")

Internal_forces_pillar = [M_max_value_pillar,Q_max_value_pillar,N_max_value_pillar]
print("The internal forces in the pillar are: M_max =",Internal_forces_pillar[0],"kNm; Q_max =",Internal_forces_pillar[1],"kN; N_max =",-Internal_forces_pillar[2],"kN !")

Truss_MQN = Internal_forces_truss
Pillar_MQN = Internal_forces_pillar

#================================================================================================================================================================================
#================================================================================================================================================================================
#================================================================================================================================================================================
# Import Profile list for the truss

gk =  input("Enter now the own weight of the roof g_k in [kN/m2]: (g_k): ")
gk = float(gk)
gk_roof = gk * L_section #kN/m
print(gk_roof)

import pandas



import numpy

IPE = []
IPE = pandas.read_excel(r"C:\Users\janib\Desktop\SemesterUoLJ\CP\PyCharm\IPE-profiles.xlsx")
HEA = []
HEA = pandas.read_excel(r"C:\Users\janib\Desktop\SemesterUoLJ\CP\PyCharm\HEA-profiles.xlsx")
HEB = []
HEB = pandas.read_excel(r"C:\Users\janib\Desktop\SemesterUoLJ\CP\PyCharm\HEB-profiles.xlsx")

#print(IPE)

# Starting with IPE =================================================================================================
# Zuerst wird das Eigengewicht ermittelt
# Dieses besteht aus dem Eigengewicht des Profils (gk_vektor_IPE) und der Dachkonstruktion (gk_vektor_roof)

mass_vektor_IPE = []
gk_vektor_roof = []
sd_vektor = []

num_rows_IPE = IPE.shape[0]
num_rows_IPE = int(num_rows_IPE)

for i in range(num_rows_IPE):
    mass = IPE.iat[i, 8]
    mass_vektor_IPE.append(mass)
    gk_vektor_roof.append(gk_roof)
    sd_vektor.append(sd)


gk_vektor_IPE = []
factor_gk = 9.81/1000

for value in mass_vektor_IPE:
    new_value = value * factor_gk
    gk_vektor_IPE.append(new_value)

gk_vektor_IPE = [round(num, 2) for num in gk_vektor_IPE]

gk_vektor = [a + b for a, b in zip(gk_vektor_IPE, gk_vektor_roof)]

gd_vektor = []
for value in gk_vektor:
    new_value = value * 1.35
    gd_vektor.append(new_value)
gd_vektor = [round(num, 2) for num in gd_vektor]

#print(gd_vektor)

num_factor_vektor = IPE.shape[0]

# Das Eigengewicht ist nun als Liste für alle Profile abgespeichert
# Im nächsten Schritt werden für alle Profile die neuen Schnittgrößen berechnet

factor_vektor = []
factor_vektor = [a / b for a, b in zip(gd_vektor, sd_vektor)]
factor_vektor = [round(num, 3) for num in factor_vektor]

#print(num_factor_vektor)
#print(len(factor_vektor))
#print(factor_vektor)

#print(factor_vektor)

# This is a lot of code, so I will store it in a function

def Internal_Forces_Matrix(factor_vektor,num_factor_vektor):
    # For the Moment===========================================================================================================================================================

    num_factor_vektor = int(num_factor_vektor)
    abs_Moment_P_gd_matrix = []
    M_d_matrix = []

    for i in range(num_factor_vektor):
        factor = factor_vektor[i]
        Moment_P_gd = [i * factor for i in Moment_P_sd]
        Moment_P_gd = [round(num, 2) for num in Moment_P_gd]
        abs_Moment_P_gd = [-i if i < 0 else i for i in Moment_P_gd]
        abs_Moment_P_gd_matrix.append(abs_Moment_P_gd)
        M_d_matrix.append(M_d)

    # print(abs_Moment_P_gd_matrix)
    # print(M_d_matrix)

    M_d_new_matrix = [[abs_Moment_P_gd_matrix[i][j] + M_d_matrix[i][j] for j in range(len(abs_Moment_P_gd_matrix[0]))]
                      for i in range(len(abs_Moment_P_gd_matrix))]

    # for row in M_d_new_matrix:
    #   print(row)
    # print(M_d_new_matrix)

    max_values = [max(row[2:5]) for row in M_d_new_matrix]
    m_max_values = [round(num, 3) for num in max_values]

    # print(m_max_values)

    # For the Shear Force===========================================================================================================================================================

    num_factor_vektor = int(num_factor_vektor)
    abs_Shear_force_P_gd_matrix = []
    Q_d_matrix = []

    for i in range(num_factor_vektor):
        factor = factor_vektor[i]
        Shear_force_P_gd = [i * factor for i in Shear_force_P_sd]
        Shear_force_P_gd = [round(num, 2) for num in Shear_force_P_gd]
        abs_Shear_force_P_gd = [-i if i < 0 else i for i in Shear_force_P_gd]
        abs_Shear_force_P_gd_matrix.append(abs_Shear_force_P_gd)
        Q_d_matrix.append(Q_d)

    # print(abs_Shear_force_P_gd_matrix)
    # print(Q_d_matrix)

    Q_d_new_matrix = [
        [abs_Shear_force_P_gd_matrix[i][j] + Q_d_matrix[i][j] for j in range(len(abs_Shear_force_P_gd_matrix[0]))] for i
        in range(len(abs_Shear_force_P_gd_matrix))]

    # for row in Q_d_new_matrix:
    #   print(row)
    # print(Q_d_new_matrix)

    max_values = [max(row[2:5]) for row in Q_d_new_matrix]
    q_max_values = [round(num, 3) for num in max_values]

    # print(m_max_values)

    # For the Axial Force===========================================================================================================================================================

    num_factor_vektor = int(num_factor_vektor)
    abs_Normal_force_P_gd_matrix = []
    N_d_matrix = []

    for i in range(num_factor_vektor):
        factor = factor_vektor[i]
        Normal_force_P_gd = [i * factor for i in Normal_force_P_sd]
        Normal_force_P_gd = [round(num, 2) for num in Normal_force_P_gd]
        abs_Normal_force_P_gd = [-i if i < 0 else i for i in Normal_force_P_gd]
        abs_Normal_force_P_gd_matrix.append(abs_Normal_force_P_gd)
        N_d_matrix.append(N_d)

    # print(abs_Normal_force_P_gd_matrix)
    # print(N_d_matrix)

    N_d_new_matrix = [
        [abs_Normal_force_P_gd_matrix[i][j] + N_d_matrix[i][j] for j in range(len(abs_Normal_force_P_gd_matrix[0]))] for
        i in range(len(abs_Normal_force_P_gd_matrix))]

    # for row in N_d_new_matrix:
    #   print(row)
    # print(n_d_new_matrix)

    max_values = [max(row[2:5]) for row in N_d_new_matrix]
    n_max_values = [round(num, 3) for num in max_values]

    return m_max_values, q_max_values, n_max_values #return the 3 important lists

    # print(N_max_values)

    # end of def - function

#Internal_Forces_Matrix()
Result_IPE = []
Result_IPE = Internal_Forces_Matrix(factor_vektor,num_factor_vektor)

M_max_values, Q_max_values, N_max_values = Result_IPE

Truss_MQN_Matrix_IPE = [M_max_values,Q_max_values,N_max_values]
Truss_MQN_Matrix_IPE = [list(row) for row in zip(*Truss_MQN_Matrix_IPE)]

#for row in Truss_MQN_Matrix_IPE:
 #   print(row)

# Now for HEA =========================================================================================================

mass_vektor_HEA = []
num_rows_HEA =HEA.shape[0]
num_rows_HEA = int(num_rows_HEA)
gk_vektor_roof = []
sd_vektor = []


for i in range(num_rows_HEA):
    mass = HEA.iat[i, 8]
    mass_vektor_HEA.append(mass)
    gk_vektor_roof.append(gk_roof)
    sd_vektor.append(sd)

gk_vektor_HEA = []
factor_gk = 9.81/1000

for value in mass_vektor_HEA:
    new_value = value * factor_gk
    gk_vektor_HEA.append(new_value)

gk_vektor_HEA = [round(num, 2) for num in gk_vektor_HEA]

gk_vektor = [a + b for a, b in zip(gk_vektor_HEA, gk_vektor_roof)]

gd_vektor = []
for value in gk_vektor:
    new_value = value * 1.35
    gd_vektor.append(new_value)
gd_vektor = [round(num, 2) for num in gd_vektor]

#print(gd_vektor)

num_factor_vektor = HEA.shape[0]

factor_vektor = []
factor_vektor = [a / b for a, b in zip(gd_vektor, sd_vektor)]
factor_vektor = [round(num, 3) for num in factor_vektor]

#print(num_factor_vektor)
#print(len(factor_vektor))
#print(factor_vektor)

# take results from same function
Internal_Forces_Matrix(factor_vektor,num_factor_vektor)
Result_HEA = []
Result_HEA = Internal_Forces_Matrix(factor_vektor,num_factor_vektor)

M_max_values, Q_max_values, N_max_values = Result_HEA

Truss_MQN_Matrix_HEA = [M_max_values,Q_max_values,N_max_values]
Truss_MQN_Matrix_HEA = [list(row) for row in zip(*Truss_MQN_Matrix_HEA)]

#for row in Truss_MQN_Matrix_HEA:
 #   print(row)


# Now for HEB =========================================================================================================

mass_vektor_HEB = []
num_rows_HEB =HEB.shape[0]
num_rows_HEB = int(num_rows_HEB)
gk_vektor_roof = []
sd_vektor = []


for i in range(num_rows_HEB):
    mass = HEB.iat[i, 8]
    mass_vektor_HEB.append(mass)
    gk_vektor_roof.append(gk_roof)
    sd_vektor.append(sd)

gk_vektor_HEB = []
factor_gk = 9.81/1000

for value in mass_vektor_HEB:
    new_value = value * factor_gk
    gk_vektor_HEB.append(new_value)

gk_vektor_HEB = [round(num, 2) for num in gk_vektor_HEB]

gk_vektor = [a + b for a, b in zip(gk_vektor_HEB, gk_vektor_roof)]

gd_vektor = []
for value in gk_vektor:
    new_value = value * 1.35
    gd_vektor.append(new_value)
gd_vektor = [round(num, 2) for num in gd_vektor]

#print(gd_vektor)

num_factor_vektor = HEB.shape[0]

factor_vektor = []
factor_vektor = [a / b for a, b in zip(gd_vektor, sd_vektor)]
factor_vektor = [round(num, 3) for num in factor_vektor]

#print(num_factor_vektor)
#print(len(factor_vektor))
#print(factor_vektor)

# take results from same function
Internal_Forces_Matrix(factor_vektor,num_factor_vektor)
Result_HEB = []
Result_HEB = Internal_Forces_Matrix(factor_vektor,num_factor_vektor)

M_max_values, Q_max_values, N_max_values = Result_HEB

Truss_MQN_Matrix_HEB = [M_max_values,Q_max_values,N_max_values]
Truss_MQN_Matrix_HEB = [list(row) for row in zip(*Truss_MQN_Matrix_HEB)]

#for row in Truss_MQN_Matrix_HEB:
 #   print(row)

#=====================================================================================================================
#=====================================================================================================================
#=====================================================================================================================
# Now starting with the first Static proof to find a profile you can choose
print("You can choose for the truss one of the three profiles:")
# starting with IPE again

count = 0
Eta_IPE_vektor = []

for i in range(num_rows_IPE, 0, -1):
    i = i-1
    #print(i)
    M_Ed_variable = Truss_MQN_Matrix_IPE[i][0]
    #print(M_Ed_variable)
    S_x = IPE.iat[i, 16]
    W_pl_variable = float(2*S_x)
    M_cRD_variable = W_pl_variable * 23.5 / 100
    #print(M_cRD_variable)
    eta_IPE = M_Ed_variable / M_cRD_variable
    Eta_IPE = round(eta_IPE, 2)  # Round to two decimal
    #print(Eta_IPE)


    Eta_IPE_vektor.append(Eta_IPE)
    count += 1

    if Eta_IPE >= 0.9:
        break

profile_number_IPE = num_rows_IPE - count + 1
eta_number = count-2
#print(Eta_IPE_vektor)
print("IPE",IPE.iat[profile_number_IPE, 1],"with eta =",Eta_IPE_vektor[eta_number],)

# same for HEA

count = 0
Eta_HEA_vektor = []

for i in range(num_rows_HEA, 0, -1):
    i = i-1
    #print(i)
    M_Ed_variable = Truss_MQN_Matrix_HEA[i][0]
    #print(M_Ed_variable)
    S_x = HEA.iat[i, 16]
    W_pl_variable = float(2*S_x)
    M_cRD_variable = W_pl_variable * 23.5 / 100
    #print(M_cRD_variable)
    eta_HEA = M_Ed_variable / M_cRD_variable
    Eta_HEA = round(eta_HEA, 2)  # Round to two decimal
    #print(Eta_HEA)


    Eta_HEA_vektor.append(Eta_HEA)
    count += 1

    if Eta_HEA >= 0.9:
        break

profile_number_HEA = num_rows_HEA - count + 1
eta_number = count-2
#print(Eta_HEA_vektor)
print("HEA",HEA.iat[profile_number_HEA, 1],"with eta =",Eta_HEA_vektor[eta_number],)

# same for HEB

count = 0
Eta_HEB_vektor = []

for i in range(num_rows_HEB, 0, -1):
    i = i-1
    #print(i)
    M_Ed_variable = Truss_MQN_Matrix_HEB[i][0]
    #print(M_Ed_variable)
    S_x = HEB.iat[i, 16]
    W_pl_variable = float(2*S_x)
    M_cRD_variable = W_pl_variable * 23.5 / 100
    #print(M_cRD_variable)
    eta_HEB = M_Ed_variable / M_cRD_variable
    Eta_HEB = round(eta_HEB, 2)  # Round to two decimal
    #print(Eta_HEB)


    Eta_HEB_vektor.append(Eta_HEB)
    count += 1

    if Eta_HEB >= 0.9:
        break

profile_number_HEB = num_rows_HEB - count + 1
eta_number = count-2
#print(Eta_HEB_vektor)
print("HEB",HEB.iat[profile_number_HEA, 1],"with eta =",Eta_HEB_vektor[eta_number],)

# Choose a profile now
print("You can now choose a profile for the truss: IPE", IPE.iat[profile_number_IPE, 1], "or HEA", HEA.iat[profile_number_HEA, 1], "or HEB",
      HEB.iat[profile_number_HEB, 1], )
print("Write IPE or HEA or HEB to choose a profile!")

profile_choice = input("Your profile choice: ")

if profile_choice == "IPE":
    print("You choice is IPE", IPE.iat[profile_number_IPE, 1], )
    print("The internal forces with g_d are: M_max =",Truss_MQN_Matrix_IPE[profile_number_IPE][0],"kNm; Q_max =",Truss_MQN_Matrix_IPE[profile_number_IPE][1],"kN; N_max =",-Truss_MQN_Matrix_IPE[profile_number_IPE][2],"kN !")


elif profile_choice == "HEA":
    print("You choice is HEA", HEA.iat[profile_number_HEA, 1], )
    print("The internal forces with g_d are: M_max =",Truss_MQN_Matrix_HEA[profile_number_HEA][0],"kNm; Q_max =",Truss_MQN_Matrix_HEA[profile_number_HEA][1],"kN; N_max =",-Truss_MQN_Matrix_HEA[profile_number_HEA][2],"kN !")

elif profile_choice == "HEB":
    print("You choice is HEB", HEB.iat[profile_number_HEB, 1], )
    print("The internal forces with g_d are: M_max =", Truss_MQN_Matrix_HEB[profile_number_HEB][0], "kNm; Q_max =",
          Truss_MQN_Matrix_HEB[profile_number_HEB][1], "kN; N_max =", -Truss_MQN_Matrix_HEB[profile_number_HEB][2], "kN !")

else:
    print("Invalid entry. Please enter IPE or HEA or HEB!")






