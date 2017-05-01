
r = te.loada('''
// Created by libAntimony v2.8.0
function Function_for_PGI(F6P, G6P, Keq, KmF6P, KmG6P, KmPEP, PEP, Vmax, PGN, KmPGN)
  (Vmax*(G6P - F6P/Keq))/KmG6P/(1 + F6P/KmF6P + G6P/KmG6P + PEP/KmPEP + PGN/KmPGN);
end

function Function_for_PFK(ATP, F6P, FDP, KefrADP, KefrPEP, KeftADP, KeftPEP, Keq, KirADP, KirATP, KirF6P, KirFDP, KitADP, KitATP, KitF6P, KitFDP, KmrADP, KmrATPMg, KmrF6P, KmrFDP, KmtADP, KmtATPMg, KmtF6P, KmtFDP, L0, MgADP, MgATP, PEP, Vmax, Wr, Wt, n)
  (Vmax*n*(MgATP*F6P - (MgADP*FDP)/Keq))/(KirF6P*KmrATPMg)/(1 + KmrFDP/KirFDP*(MgADP/KmrADP) + KmrF6P/KirF6P*(MgATP/KmrATPMg) + KmrFDP/KirFDP*(MgADP/KmrADP)*(F6P/KirF6P) + MgATP/KmrATPMg*(F6P/KirF6P) + MgADP/KirADP*(MgATP/KmrATPMg)*(F6P/KirF6P) + (1 + (ATP - MgATP)/KirATP)*(F6P/KirF6P) + FDP/KirFDP + MgADP/KmrADP*(FDP/KirFDP) + KmrF6P/KirF6P*(MgATP/KmrATPMg)*(FDP/KirFDP) + Wr*(KmrF6P/KirF6P)*(MgADP/KirADP)*(MgATP/KmrATPMg)*(FDP/KmrFDP))/(1 + L0*(((1 + KmtFDP/KitFDP*(MgADP/KmtADP) + KmtF6P/KitF6P*(MgATP/KmtATPMg) + KmtFDP/KitFDP*(MgADP/KmtADP)*(F6P/KitF6P) + MgATP/KmtATPMg*(F6P/KitF6P) + MgADP/KitADP*(MgATP/KmtATPMg)*(F6P/KitF6P) + (1 + (ATP - MgATP)/KitATP)*(F6P/KitF6P) + FDP/KitFDP + MgADP/KmtADP*(FDP/KitFDP) + KmtF6P/KitF6P*(MgATP/KmtATPMg)*(FDP/KitFDP) + Wt*(KmtF6P/KitF6P)*(MgADP/KitADP)*(MgATP/KmtATPMg)*(FDP/KmtFDP))*(1 + MgADP/KeftADP + PEP/KeftPEP + MgADP/KeftADP*(PEP/KeftPEP)))/((1 + KmrFDP/KirFDP*(MgADP/KmrADP) + (KmrF6P*MgATP)/(KirF6P*KmrATPMg) + KmrFDP/KirFDP*(MgADP/KmrADP)*(F6P/KirF6P) + MgATP/KmrATPMg*(F6P/KirF6P) + MgADP/KirADP*(MgATP/KmrATPMg)*(F6P/KirF6P) + (1 + (ATP - MgATP)/KirATP)*(F6P/KirF6P) + FDP/KirFDP + MgADP/KmrADP*(FDP/KirFDP) + KmrF6P/KirF6P*(MgATP/KmrATPMg)*(FDP/KirFDP) + Wr*(KmrF6P/KirF6P)*(MgADP/KirADP)*(MgATP/KmrATPMg)*(FDP/KmrFDP))*(1 + MgADP/KefrADP + PEP/KefrPEP + MgADP/KefrADP*(PEP/KefrPEP))))^n);
end

function Function_for_FBA(DAP, FDP, GAP, Keq, KmDAP, KmFDP, KmGAP, KmPEP, PEP, Vmax)
  (Vmax*(FDP - (DAP*GAP)/Keq))/KmFDP/(1 + FDP/KmFDP + DAP/KmDAP + DAP/KmDAP*(GAP/KmGAP) + PEP/KmPEP);
end

function Function_for_TPI(DAP, GAP, Keq, KmDAP, KmGAP, Vmax)
  (Vmax*(DAP - GAP/Keq))/KmDAP/(1 + DAP/KmDAP + GAP/KmGAP);
end

function Function_for_GDH(BPG, GAP, Keq, KmBPG, KmGAP, KmNAD, KmNADH, KmP, NAD, NADH, P, Vmax)
  (Vmax*(P*GAP*NAD - (BPG*NADH)/Keq))/(KmP*KmGAP*KmNAD)/(((1 + P/KmP)*(1 + GAP/KmGAP)*(1 + NAD/KmNAD) + (1 + BPG/KmBPG)*(1 + NADH/KmNADH)) - 1);
end

function Function_for_PGK(BPG, Keq, KmADPMg, KmATPMg, KmBPG, KmPGA3, MgADP, MgATP, PGA3, Vmax)
  (Vmax*(MgADP*BPG - (MgATP*PGA3)/Keq))/(KmADPMg*KmBPG)/(1 + MgADP/KmADPMg + BPG/KmBPG + (MgADP/KmADPMg*BPG)/KmBPG + MgATP/KmATPMg + PGA3/KmPGA3 + (MgATP/KmATPMg*PGA3)/KmPGA3);
end

function Function_for_GPM(Keq, KmPGA2, KmPGA3, PGA2, PGA3, Vmax)
  (Vmax*(PGA3 - PGA2/Keq))/KmPGA3/(1 + PGA3/KmPGA3 + PGA2/KmPGA2);
end

function Function_for_ENO(Keq, KmPEP, KmPGA2, PEP, PGA2, Vmax)
  (Vmax*(PGA2 - PEP/Keq))/KmPGA2/(1 + PGA2/KmPGA2 + PEP/KmPEP);
end

function Function_for_PYK(ADP, FDP, G6P, GL6P, KefrFDP, KefrG6P, KefrGL6P, KefrR5P, KefrRU5P, KefrS7P, KefrX5P, KeftATP, KeftSUCCOA, KirADP, KirATP, KirPEP, KirPYR, KirPyrATP, KitADP, KitATP, KitPEP, KitPYR, KitPyrATP, KmrADPMg, KmrPEP, KmtADPMg, KmtPEP, L0, MgADP, MgATP, PEP, PYR, R5P, RU5P, S7P, SUCCOA, Vmax, X5P, n)
  (Vmax*n*PEP*MgADP)/(KirPEP*KmrADPMg)/(1 + KmrPEP/KirPEP*(MgADP/KmrADPMg) + MgATP/KirATP + MgADP/KmrADPMg*(PEP/KirPEP) + KmrADPMg/KmrADPMg*(1 + (ADP - MgADP)/KirADP)*(PEP/KirPEP) + PYR/KirPYR + MgATP/KirPyrATP*(PYR/KirPYR))/(1 + L0*(((1 + KmtPEP/KitPEP*(MgADP/KmtADPMg) + MgATP/KitATP + (MgADP*PEP)/(KitPEP*KmtADPMg) + (1 + (ADP - MgADP)/KitADP)*(PEP/KitPEP) + PYR/KitPYR + MgATP/KitPyrATP*(PYR/KitPYR))*(1 + SUCCOA/KeftSUCCOA + (MgATP*SUCCOA)/(KeftATP*KeftSUCCOA)))/((1 + KmrPEP/KirPEP*(MgADP/KmrADPMg) + MgATP/KirATP + MgADP/KmrADPMg*(PEP/KirPEP) + (1 + (ADP - MgADP)/KirADP)*(PEP/KirPEP) + PYR/KirPYR + MgATP/KirPyrATP*(PYR/KirPYR))*(1 + FDP/KefrFDP + G6P/KefrG6P + GL6P/KefrGL6P + R5P/KefrR5P + RU5P/KefrRU5P + S7P/KefrS7P + X5P/KefrX5P)))^n);
end

function Function_for_ZWF(G6P, GL6P, KdG6P, KdGL6P, Keq, KmG6P, KmGL6P, KmNADP, KmNADPH, NADP, NADPH, Vmax)
  (Vmax*(G6P*NADP - (GL6P*NADPH)/Keq))/(KdG6P*KmNADP)/(1 + G6P/KdG6P + KmG6P/KdG6P*(NADP/KmNADP) + G6P/KdG6P*(NADP/KmNADP) + KmGL6P/KdGL6P*(NADPH/KmNADPH) + GL6P/KdGL6P*(NADPH/KmNADPH));
end

function Function_for_PGL(G6P, GL6P, Keq, KiG6P, KmGL6P, KmPGN, PGN, Vmax)
  (Vmax*(GL6P - PGN/Keq))/KmGL6P/(1 + GL6P/KmGL6P + PGN/KmPGN + G6P/KiG6P);
end

function Function_for_GND(ATP, FDP, HCO3, KdHCO3, KdHCO3NADPH, KdNADP, KdNADPH, KdRu5P, KefATP, KefFbP, KefNADPATP, KefNADPFbP, Keq, KmHCO3, KmNADP, KmNADPH, KmPGN, KmRU5P, NADP, NADPH, PGN, RU5P, Vmax)
  (Vmax*(NADP*PGN - (NADPH*RU5P*HCO3)/Keq))/(KdNADP*KmPGN)/(1 + NADP/KdNADP + FDP/KefFbP + NADP/KdNADP*(FDP/KefNADPFbP) + KmNADP/KdNADP*(PGN/KmPGN) + NADP/KdNADP*(PGN/KmPGN) + ATP/KefATP + ATP/KefNADPATP*(KmNADP/KdNADP)*(PGN/KmPGN) + HCO3/KdHCO3 + NADPH/KdNADPH + RU5P/KdRu5P + HCO3/KdHCO3*(NADPH/KdHCO3NADPH) + HCO3/KdHCO3*(KmNADPH/KdHCO3NADPH)*(RU5P/KmRU5P) + HCO3/KdHCO3*(NADPH/KdHCO3NADPH)*(RU5P/KmRU5P) + KmHCO3/KdHCO3*(NADPH/KdHCO3NADPH)*(RU5P/KmRU5P));
end

function Function_for_RPE(Keq, KmRU5P, KmX5P, RU5P, Vmax, X5P)
  (Vmax*(RU5P - X5P/Keq))/KmRU5P/(1 + RU5P/KmRU5P + X5P/KmX5P);
end

function Function_for_RPI(E4P, Keq, KmE4P, KmR5P, KmRU5P, R5P, RU5P, Vmax)
  (Vmax*(RU5P - R5P/Keq))/KmRU5P/(1 + RU5P/KmRU5P + R5P/KmR5P + E4P/KmE4P);
end

function Function_for_X5P_GAP_TKT(GAP, Keq, X5P, kcat, tkt, tktC2)
  kcat*(tkt*X5P - (GAP*tktC2)/Keq);
end

function Function_for_F6P_E4P_TKT(E4P, F6P, Keq, kcat, tkt, tktC2)
  kcat*(E4P*tktC2 - (F6P*tkt)/Keq);
end

function Function_for_S7P_R5P_TKT(Keq, R5P, S7P, kcat, tkt, tktC2)
  kcat*(R5P*tktC2 - (S7P*tkt)/Keq);
end

function Function_for_F6P_GAP_TAL(F6P, GAP, Keq, kcat, tal, talC3)
  kcat*(GAP*talC3 - (F6P*tal)/Keq);
end

function Function_for_S7P_E4P_TAL(E4P, Keq, S7P, kcat, tal, talC3)
  kcat*(S7P*tal - (E4P*talC3)/Keq);
end

function Function_for_FBP(AMP, F6P, FDP, KdFDPMg, KirAMP, KirAMPFDP, KirF6P, KirF6PMg, KirFDP, KirFDPMg, KirFDPMgMg, KirP, KirPF6P, KirPF6PMg, KirPMg, KitAMP, KitAMPFDP, KitF6P, KitF6PMg, KitFDP, KitFDPMg, KitFDPMgMg, KitP, KitPF6P, KitPF6PMg, KitPMg, KmrFDP, KmrMg, KmtFDP, KmtMg, L0, MG, MgFDP, P, Vmax, n)
  (Vmax*n*MgFDP)/KirFDPMg/(1 + KmrFDP/KirFDP*(MG/KmrMg) + P/KirP + P/KirP*(MG/KirPMg) + F6P/KirF6P + F6P/KirF6P*(MG/KirF6PMg) + P/KirP*(F6P/KirPF6P) + P/KirP*(F6P/KirPF6P)*(MG/KirPF6PMg) + (FDP - MgFDP)/KirFDP + KdFDPMg/KmrMg*(MgFDP/KirFDP) + AMP/KirAMP + MgFDP/KirFDPMg + MgFDP/KirFDPMg*(MG/KirFDPMgMg) + AMP/KirAMP*((FDP - MgFDP)/KirAMPFDP))/(1 + L0*((1 + KmtFDP/KitFDP*(MG/KmtMg) + P/KitP + P/KitP*(MG/KitPMg) + F6P/KitF6P + F6P/KitF6P*(MG/KitF6PMg) + P/KitP*(F6P/KitPF6P) + P/KitP*(F6P/KitPF6P)*(MG/KitPF6PMg) + (FDP - MgFDP)/KitFDP + KdFDPMg/KmtMg*(MgFDP/KitFDP) + AMP/KitAMP + MgFDP/KitFDPMg + MgFDP/KitFDPMg*(MG/KitFDPMgMg) + AMP/KitAMP*((FDP - MgFDP)/KitAMPFDP))/(1 + KmrFDP/KirFDP*(MG/KmrMg) + P/KirP + P/KirP*(MG/KirPMg) + F6P/KirF6P + F6P/KirF6P*(MG/KirF6PMg) + P/KirP*(F6P/KirPF6P) + P/KirP*(F6P/KirPF6P)*(MG/KirPF6PMg) + (FDP - MgFDP)/KirFDP + KdFDPMg/KmrMg*(MgFDP/KirFDP) + AMP/KirAMP + MgFDP/KirFDPMg + MgFDP/KirFDPMg*(MG/KirFDPMgMg) + AMP/KirAMP*((FDP - MgFDP)/KirAMPFDP)))^n);
end

function Function_for_PPC(ACCOA, ASP, CIT, CYS, FDP, FUM, HCO3, KdrOAA, KdrPEP, KdtOAA, KdtPEP, KefrACCOA, KefrASP, KefrCIT, KefrCYS, KefrFDP, KefrFDPACCOA, KefrFUM, KefrMAL, KefrSUC, KeftACCOA, KeftASP, KeftCIT, KeftCYS, KeftFDP, KeftFDPACCOA, KeftFUM, KeftMAL, KeftSUC, Keq, KmrHCO3, KmrOAA, KmrP, KmrPEP, KmtHCO3, KmtOAA, KmtP, KmtPEP, L0, MAL, OAA, P, PEP, SUC, Vmax, n)
  (Vmax*n*(PEP*HCO3 - (OAA*P)/Keq))/(KdrPEP*KmrHCO3)/(1 + KmrPEP/KdrPEP*(HCO3/KmrHCO3) + KmrOAA/KdrOAA*(P/KmrP) + OAA/KdrOAA + P/KmrP*(OAA/KdrOAA) + HCO3/KmrHCO3*(PEP/KdrPEP) + PEP/KdrPEP)/(1 + L0*(((1 + ACCOA/KeftACCOA + FDP/KeftFDP + FDP/KeftFDP*(ACCOA/KeftFDPACCOA))*(1 + KmtPEP/KdtPEP*(HCO3/KmtHCO3) + KmtOAA/KdtOAA*(P/KmtP) + OAA/KdtOAA + P/KmtP*(OAA/KdtOAA) + HCO3/KmtHCO3*(PEP/KdtPEP) + PEP/KdtPEP)*(1 + ASP/KeftASP + CYS/KeftCYS + CIT/KeftCIT + FUM/KeftFUM + MAL/KeftMAL + SUC/KeftSUC))/((1 + ACCOA/KefrACCOA + FDP/KefrFDP + FDP/KefrFDP*(ACCOA/KefrFDPACCOA))*(1 + KmrPEP/KdrPEP*(HCO3/KmrHCO3) + KmrOAA/KdrOAA*(P/KmrP) + OAA/KdrOAA + P/KmrP*(OAA/KdrOAA) + HCO3/KmrHCO3*(PEP/KdrPEP) + PEP/KdrPEP)*(1 + ASP/KefrASP + CYS/KefrCYS + CIT/KefrCIT + FUM/KefrFUM + MAL/KefrMAL + SUC/KefrSUC)))^n);
end

function Function_for_PCK(ADP, HCO3, Keq, KmADP, KmATP, KmHCO3, KmOAA, KmPEP, MgADP, MgATP, OAA, PEP, Vmax)
  (Vmax*(MgATP*OAA - (HCO3*MgADP*PEP)/Keq))/(KmATP*KmOAA)/(1 + HCO3/KmHCO3 + HCO3/KmHCO3*(ADP/KmADP) + MgADP/KmADP + MgATP/KmATP + OAA/KmOAA + MgATP/KmATP*(OAA/KmOAA) + HCO3/KmHCO3*(PEP/KmPEP) + PEP/KmPEP + HCO3/KmHCO3*(MgADP/KmADP)*(PEP/KmPEP) + MgADP/KmADP*(PEP/KmPEP));
end

function Function_for_PPS(ADP, AKG, AMP, ATP, KdADPMg, KdAMP, KdATPMg, KdATPMgPPS, KdMg, KdP, KdPEP, KdPYR, KefADP, KefAKG, KefATP, KefOAA, Keq, KmAMP, KmATPMg, KmP, KmPEP, KmPYR, MG, MgADP, MgATP, OAA, P, PEP, PYR, Vmax, W, alpha)
  (Vmax*(MgATP*PYR - (AMP*PEP*P*MG)/Keq))/(KmATPMg*KmPYR)/(MgATP/KmATPMg + alpha*(P/KdP)*(MgATP/KmATPMg) + alpha*(AMP/KdAMP)*(MgATP/KmATPMg) + alpha*(P/KdP)*(AMP/KdAMP)*(MgATP/KmATPMg) + (alpha*(MG/KdMg)*(P/KmP)*(AMP/KdAMP)*(MgATP/KdATPMgPPS))/(W*(1 + MG/KdMg)) + MgATP/KmATPMg*(AKG/KefAKG) + ((1 + MG/KdMg)*(AKG/KefAKG)*(PEP/KmPEP))/W + MgATP/KmATPMg*(OAA/KefOAA) + ((1 + MG/KdMg)*(OAA/KefOAA)*(PEP/KmPEP))/W + (MG/KdMg*(P/KmP)*(AMP/KdAMP))/W + (alpha*(P/KdP)*(AMP/KdAMP)*(PEP/KmPEP))/W + (alpha*(MG/KdMg)*(P/KmP)*(AMP/KdAMP)*(PEP/KmPEP))/W + (alpha*(1 + MG/KdMg)*(KmAMP/KdAMP*(P/KmP)*(PEP/KmPEP) + AMP/KdAMP*(PEP/KmPEP)))/W + (1 + MG/KdMg)*(PYR/KmPYR) + MgATP/KmATPMg*(PYR/KmPYR) + (KdADPMg/KdMg*(P/KmP)*(MgADP/KefADP)*(AMP/KdAMP))/(W*(1 + MG/KdMg)) + (ADP - MgADP)/KefADP*(PYR/KmPYR) + (KdATPMg/KdMg*(P/KmP)*(AMP/KdAMP)*(MgATP/KefATP))/(W*(1 + MG/KdMg)) + (ATP - MgATP)/KefATP*(PYR/KmPYR) + ((1 + MG/KdMg)*(PEP/KmPEP))/W + alpha*(1 + MG/KdMg)*(PEP/KdPEP)*(PYR/KmPYR) + ((1 + MG/KdMg)*(PYR/KdPYR)*(PEP/KmPEP))/W);
end

function Function_for_MAD(ACCOA, ASP, ATP, COA, KefrACCOA, KefrASP, KefrATP, KefrCOA, KeftACCOA, KeftASP, KeftATP, KeftCOA, KirNAD, KitNAD, KmrMAL, KmrMg, KmrMn, KmrNAD, KmtMAL, KmtMg, KmtMn, KmtNAD, L0, MAL, MG, MN, NAD, Vmax, n)
  ((Vmax*n*MAL*NAD)/(KmrMAL*KirNAD)/(1 + KmrNAD/KirNAD*(MAL/KmrMAL) + NAD/KirNAD + MAL/KmrMAL*(NAD/KirNAD))*((MG/KmrMg + MN/KmrMn)/(1 + MG/KmrMg + MN/KmrMn)))/(1 + L0*(((1 + ASP/KeftASP)*(1 + MG/KmtMg + MN/KmtMn)*(1 + ATP/KeftATP)*(1 + ACCOA/KeftACCOA + COA/KeftCOA)*(1 + KmtNAD/KitNAD*(MAL/KmtMAL) + NAD/KitNAD + MAL/KmtMAL*(NAD/KitNAD)))/((1 + ASP/KefrASP)*(1 + MG/KmrMg + MN/KmrMn)*(1 + ATP/KefrATP)*(1 + ACCOA/KefrACCOA + COA/KefrCOA)*(1 + KmrNAD/KirNAD*(MAL/KmrMAL) + NAD/KirNAD + MAL/KmrMAL*(NAD/KirNAD))))^n);
end

function Function_for_PDH(ACCOA, COA, HCO3, Keq, KmACCOA, KmCOA, KmHCO3, KmNAD, KmNADH, KmPYR, NAD, NADH, PYR, Vmax)
  (Vmax*(COA*NAD*PYR - (ACCOA*NADH*HCO3)/Keq))/(KmCOA*KmNAD*KmPYR)/(ACCOA/KmACCOA + NADH/KmNADH + ACCOA/KmACCOA*(NADH/KmNADH) + COA/KmCOA*(NADH/KmNADH) + ACCOA/KmACCOA*(COA/KmCOA)*(NADH/KmNADH) + NAD/KmNAD*(NADH/KmNADH) + COA/KmCOA*(NAD/KmNAD)*(NADH/KmNADH) + ACCOA/KmACCOA*(PYR/KmPYR) + ACCOA/KmACCOA*(COA/KmCOA)*(PYR/KmPYR) + COA/KmCOA*(1 + NAD/KmNAD)*(PYR/KmPYR) + NAD/KmNAD*(1 + COA/KmCOA + PYR/KmPYR))/(1 + HCO3/KmHCO3);
end

function Function_for_GLT(ACCOA, AKG, ATP, CIT, COA, KdACCOA0, KdcsCIT, KdcsCOA, KdcsOAA, Keq, Ki1AKG, Ki1NADH, Ki2AKG, Ki2NADH, KiATP, KmACCOA0, KmOAA0, KmcsCIT, KmcsCOA, NADH, OAA, Vmax)
  (Vmax*(ACCOA*OAA - (CIT*COA)/Keq))/(KdACCOA0*KmOAA0)/(ACCOA/KdACCOA0*(1 + AKG/Ki1AKG + NADH/Ki1NADH) + ACCOA/KdACCOA0*(OAA/KmOAA0)*(1 + AKG/Ki2AKG + NADH/Ki2NADH) + (1 + ATP/KiATP)*(1 + KmACCOA0/KdACCOA0*(OAA/KmOAA0)) + KmcsCOA/KdcsCOA*(CIT/KmcsCIT) + KmcsCOA/KdcsCOA*(ACCOA/KdACCOA0)*(CIT/KmcsCIT) + COA/KdcsCOA + CIT/KmcsCIT*(OAA/KmOAA0) + ACCOA/KdACCOA0*(CIT/KdcsCIT)*(OAA/KmOAA0) + KmACCOA0/KdACCOA0*(COA/KdcsCOA)*(OAA/KmOAA0) + CIT/KmcsCIT*(COA/KdcsCOA)*(OAA/KdcsOAA));
end

function Function_for_ACN_1(ACO, CIT, ICIT, Keq, KmACO, KmCIT, KmICIT, Vmax)
  (Vmax*(CIT - ACO/Keq))/KmCIT/(1 + CIT/KmCIT + ACO/KmACO + ICIT/KmICIT);
end

function Function_for_ACN_2(ACO, CIT, ICIT, Keq, KmACO, KmCIT, KmICIT, Vmax)
  (Vmax*(ACO - ICIT/Keq))/KmACO/(1 + ACO/KmACO + ICIT/KmICIT + CIT/KmCIT);
end

function Function_for_ICD(AKG, ICIT, Keq, KmAKG, KmICIT, KmNADP, KmNADPH, NADP, NADPH, icd, kcat)
  (icd*kcat*(ICIT*NADP - (AKG*NADPH)/Keq))/(KmICIT*KmNADP)/(((1 + ICIT/KmICIT)*(1 + NADP/KmNADP) + (1 + AKG/KmAKG)*(1 + NADPH/KmNADPH)) - 1);
end

function Function_for_LPD(AKG, COA, KdAKG, KmAKG, KmCOA, KmNAD, NAD, Vmax, alpha)
  (Vmax*COA*AKG*NAD*(1 - AKG/KdAKG))/(KmCOA*KmAKG*KmNAD)/((COA/KmCOA*(AKG/KmAKG) + COA/KmCOA*(NAD/KmNAD) + AKG/KmAKG*(NAD/KmNAD) + COA/KmCOA*(AKG/KmAKG)*(NAD/KmNAD)) - AKG/KdAKG*(COA/KmCOA*(AKG/KmAKG) + AKG/KmAKG*(NAD/KmNAD) + alpha*(COA/KmCOA)*(AKG/KmAKG)*(NAD/KmNAD)));
end

function Function_for_SK(ADP, ATP, COA, Keq, KmADP, KmATP, KmCOA, KmP, KmSUC, KmSUCCOA, P, SUC, SUCCOA, Vmax)
  (Vmax*(ADP*SUCCOA*P - (ATP*COA*SUC)/Keq))/(KmADP*KmSUCCOA*KmP)/(((1 + ADP/KmADP)*(1 + SUCCOA/KmSUCCOA)*(1 + P/KmP) + (1 + ATP/KmATP)*(1 + COA/KmCOA)*(1 + SUC/KmSUC)) - 1);
end

function Function_for_SDH(FUM, KefFUM, KefSUC, Keq, KmFUM, KmQ, KmQH2, KmSUC, Q, QH2, SUC, Vmax)
  (Vmax*(SUC*Q - (FUM*QH2)/Keq))/(KefSUC*KmQ)/(1 + FUM/KefFUM + KmSUC/KefSUC*(Q/KmQ) + KmFUM/KefFUM*(QH2/KmQH2) + FUM/KefFUM*(QH2/KmQH2) + SUC/KefSUC + SUC/KefSUC*(Q/KmQ));
end

function Function_for_FUMA(FUM, Keq, KmFUM, KmMAL, MAL, Vmax)
  (Vmax*(FUM - MAL/Keq))/KmFUM/(1 + FUM/KmFUM + MAL/KmMAL);
end

function Function_for_MQO(Keq, KmMAL, KmOAA, KmQ, KmQH2, MAL, OAA, Q, QH2, Vmax)
  (Vmax*(MAL*Q - (OAA*QH2)/Keq))/(KmMAL*KmQ)/(((1 + MAL/KmMAL)*(1 + Q/KmQ) + (1 + OAA/KmOAA)*(1 + QH2/KmQH2)) - 1);
end

function Function_for_MDH(Keq, KiNAD, KiNADH, KiOAA, KmMAL, KmNAD, KmNADH, KmOAA, MAL, NAD, NADH, OAA, Vmax)
  (Vmax*(NADH*OAA - (MAL*NAD)/Keq))/(KiNADH*KmOAA)/(1 + KmNAD/KiNAD*(MAL/KmMAL) + NAD/KiNAD + MAL/KmMAL*(NAD/KiNAD) + NADH/KiNADH + KmNAD/KiNAD*(MAL/KmMAL)*(NADH/KiNADH) + KmNADH/KiNADH*(OAA/KmOAA) + KmNADH/KiNADH*(NAD/KiNAD)*(OAA/KmOAA) + (MAL*NAD*OAA)/(KiNAD*KiOAA*KmMAL) + NADH/KiNADH*(OAA/KmOAA) + Keq*((KiNADH*KmOAA)/(KiNAD*KmMAL))*(KmNAD/KiNAD)*(MAL/KmMAL)*(NADH/KmNADH)*(OAA/KiOAA));
end

function Function_for_ACEA(GLX, ICIT, KdICITsuc, KdPEP, KdPEPglx, KdPEPicit, KdPGA3, KdSUC, Keq, KmGLX, KmICIT, KmSUC, PEP, PGA3, SUC, Vmax)
  (Vmax*(ICIT - (GLX*SUC)/Keq))/KmICIT/(1 + ICIT/KmICIT*(1 + PEP/KdPEPicit) + SUC/KdSUC*(1 + ICIT/KdICITsuc) + KmSUC/KdSUC*(GLX/KmGLX)*(1 + PEP/KdPEPglx) + GLX/KmGLX*(SUC/KdSUC) + PEP/KdPEP + PGA3/KdPGA3);
end

function Function_for_ACEB(ACCOA, COA, GLX, Keq, KmACCOA, KmCOA, KmGLX, KmMAL, MAL, Vmax)
  (Vmax*(ACCOA*GLX - (COA*MAL)/Keq))/(KmACCOA*KmGLX)/(((1 + ACCOA/KmACCOA)*(1 + GLX/KmGLX) + (1 + COA/KmCOA)*(1 + MAL/KmMAL)) - 1);
end

function Function_for_ACEK_1(ADP, ATP, Keq, icd, icdP, k)
  k*(ATP*icd - (ADP*icdP)/Keq);
end

function Function_for_ACEK_2(Keq, P, icd, icdP, k)
  k*(icdP - (icd*P)/Keq);
end

function Function_for_EDD(KDPG, Keq, KmKDPG, KmPGN, PGN, Vmax)
  (Vmax*(PGN - KDPG/Keq))/KmPGN/(1 + PGN/KmPGN + KDPG/KmKDPG);
end

function Function_for_EDA(GAP, KDPG, Keq, KmGAP, KmKDPG, KmPYR, PYR, Vmax)
  (Vmax*(KDPG - (GAP*PYR)/Keq))/KmKDPG/((1 + KDPG/KmKDPG + (1 + GAP/KmGAP)*(1 + PYR/KmPYR)) - 1);
end

function Function_for_PNT(Keq, NAD, NADH, NADP, NADPH, k)
  k*(NAD*NADPH - (NADH*NADP)/Keq);
end

function Function_for_ADK(ADP, AMP, ATP, Keq, k)
  k*(AMP*ATP - ADP^2/Keq);
end

function Function_for_CYA(ATP, CAMP, Keq, P, k, eiiaP, KaeiiaP)
  (k*(ATP - (CAMP*P^2)/Keq)*eiiaP)/(eiiaP + KaeiiaP);
end

function Function_for_DOS(AMP, CAMP, Keq, k)
  k*(CAMP - AMP/Keq);
end

function Function_for_ACK(ACEx, ACP, ADP, ATP, Keq, KmACE, KmACP, KmADP, KmATP, Vmax, cell)
  (cell*Vmax*(ACP*ADP - (ACEx*ATP)/Keq))/(KmACP*KmADP)/((1 + ACP/KmACP + ACEx/KmACE)*(1 + ADP/KmADP + ATP/KmATP));
end

function Function_for_ACS(ACEx, ATP, COA, KmACE, KmATP, KmCOA, Vmax, cell)
  (cell*Vmax*ACEx*ATP*COA)/(KmACE*KmATP*KmCOA)/((1 + ACEx/KmACE)*(1 + ATP/KmATP)*(1 + COA/KmCOA));
end

function Function_for_PTA(ACCOA, ACP, COA, Keq, KiACCOA, KiACP, KiCOA, KiP, KmACP, KmP, P, Vmax)
  (Vmax*(ACCOA*P - (ACP*COA)/Keq))/(KiACCOA*KmP)/(1 + ACCOA/KiACCOA + P/KiP + ACP/KiACP + COA/KiCOA + (ACCOA*P)/(KiACCOA*KmP) + (ACP*COA)/(KmACP*KiCOA));
end

function Function_for_PTS_0(KmPEP, KmPYR, PEP, PYR, ei, eiP, kF, kR)
  (kF*ei*PEP^2)/(KmPEP^2 + PEP^2) - (kR*eiP*PYR^2)/(KmPYR^2 + PYR^2);
end

function Function_for_PTS_4(G6P, GLCx, KmG6P, KmGLC, cell, eiicb, eiicbP, kF, kR)
  cell*((kF*eiicbP*GLCx)/(KmGLC + GLCx) - (kR*eiicb*G6P)/(KmG6P + G6P));
end

function Function_for_GLC_FEED(FEED, cell, extracellular)
  (cell*FEED)/extracellular;
end

function Function_for_ATP_MAINTENANCE(Vmax, ADP, P, ATP, Keq)
  Vmax*(ATP - (ADP*P)/Keq);
end

function Function_for_ATP_SYN(Vmax, Hin, Hout, ADP, P, ATP, Keq)
  (Vmax*(ln(Hout/Hin)/ln(10))^4)/(1 + (ln(Hout/Hin)/ln(10))^4)*(ADP*P - ATP/Keq);
end

function Function_for_NDH1(Vmax, Hin, Hout, NADH, Q, NAD, QH2, Keq)
  Vmax/(1 + (ln(Hout/Hin)/ln(10))^2)*(NADH*Q - (NAD*QH2)/Keq);
end

function Function_for_CYTBO(Vmax, Hin, Hout, Keq, O2, QH2, Q)
  Vmax/(1 + (ln(Hout/Hin)/ln(10))^2)*(QH2^2*O2 - Q^2/Keq);
end

function Function_for_SQR(FADH2, Q, FAD, QH2, Keq, Vmax)
  Vmax*(FADH2*Q - (FAD*QH2)/Keq);
end

function Function_for_NDH2(Vmax, NADH, Q, NAD, QH2, Keq)
  Vmax*(NADH*Q - (NAD*QH2)/Keq);
end

function Function_for_GROWTH(Vmax, G6P, E4P, PGA3, OAA, AKG, PYR, R5P, PEP, GAP, F6P, NADPH, ACCOA, NAD, ATP, KmG6P, KmE4P, KmPGA3, KmOAA, KmAKG, KmPYR, KmR5P, KmPEP, KmGAP, KmF6P, KmNADPH, KmACCOA, KmNAD, KmATP)
  (Vmax*G6P*E4P*PGA3*OAA*AKG*PYR*R5P*PEP*GAP*F6P*NADPH*ACCOA*NAD*ATP)/(KmG6P*KmE4P*KmPGA3*KmOAA*KmAKG*KmPYR*KmR5P*KmPEP*KmGAP*KmF6P*KmNADPH*KmACCOA*KmNAD*KmATP)/((1 + G6P/KmG6P)*(1 + E4P/KmE4P)*(1 + PGA3/KmPGA3)*(1 + OAA/KmOAA)*(1 + AKG/KmAKG)*(1 + PYR/KmPYR)*(1 + R5P/KmR5P)*(1 + PEP/KmPEP)*(1 + GAP/KmGAP)*(1 + F6P/KmF6P)*(1 + NADPH/KmNADPH)*(1 + ACCOA/KmACCOA)*(1 + NAD/KmNAD)*(1 + ATP/KmATP));
end

function Function_for_PIT(Vmax, Hout, Hin, Pp, KmPp, Kr, P, KmP)
  Vmax*((ln(Hout/Hin)/ln(10))^2/(1 + (ln(Hout/Hin)/ln(10))^2)*(Pp/(KmPp + Pp)) - Kr/(1 + (ln(Hout/Hin)/ln(10))^2)*(P/(KmP + P)));
end

function Function_for_GL6P_HYDROLYSIS(KGl6Phydrol, GL6P, PGN, KeqGl6Phydrol)
  KGl6Phydrol*(GL6P - PGN/KeqGl6Phydrol);
end

function Function_for_XCH_RMM(Vmax, S, P, Km)
  (Vmax*(S/Km - P/Km))/(1 + S/Km + P/Km);
end


model *Millard2016___E__coli_central_carbon_and_energy_metabolism()

  // Compartments and Species:
  compartment cell, extracellular, cell_periplasm;
  species ACCOA in cell, ACO in cell, ACP in cell, AKG in cell, BPG in cell;
  species CIT in cell, DAP in cell, E4P in cell, F6P in cell, FDP in cell;
  species FUM in cell, G6P in cell, GAP in cell, GL6P in cell, GLX in cell;
  species ICIT in cell, KDPG in cell, MAL in cell, NAD in cell, NADH in cell;
  species NADP in cell, NADPH in cell, OAA in cell, PEP in cell, PGA2 in cell;
  species PGA3 in cell, PGN in cell, PYR in cell, Q in cell, QH2 in cell;
  species R5P in cell, RU5P in cell, S7P in cell, SUC in cell, SUCCOA in cell;
  species X5P in cell, ei in cell, eiP in cell, eiia in cell, eiiaP in cell;
  species eiicb in cell, eiicbP in cell, hpr in cell, hprP in cell, icd in cell;
  species icdP in cell, tal in cell, talC3 in cell, tkt in cell, tktC2 in cell;
  species ADP in cell, AMP in cell, ATP in cell, CAMP in cell, $COA in cell;
  species $HCO3 in cell, P in cell, $MG in cell, $MgADP in cell, $MgATP in cell;
  species $MgFDP in cell, $ASP in cell, $CYS in cell, $MN in cell, $Hin in cell;
  species $H2O in cell, $O2 in cell, FAD in cell, FADH2 in cell, ACEx in cell;
  species GLCx in extracellular, $Px in extracellular, ACEx_0 in extracellular;
  species Hout in cell_periplasm, GLCp in cell_periplasm, Pp in cell_periplasm;
  species ACEp in cell_periplasm;

  // Assignment Rules:
  MgADP := (MG*ADP)/(KdADPMg + MG);
  MgATP := (MG*ATP)/(KdATPMg + MG);
  MgFDP := (MG*FDP)/(KdFDPMg + MG);

  // Reactions:
  PGI: G6P -> F6P; cell*Function_for_PGI(F6P, G6P, PGI_Keq, PGI_KmF6P, PGI_KmG6P, PGI_KmPEP, PEP, PGI_Vmax, PGN, PGI_KmPGN);
  PFK: ATP + F6P -> ADP + FDP; cell*Function_for_PFK(ATP, F6P, FDP, PFK_KefrADP, PFK_KefrPEP, PFK_KeftADP, PFK_KeftPEP, PFK_Keq, PFK_KirADP, PFK_KirATP, PFK_KirF6P, PFK_KirFDP, PFK_KitADP, PFK_KitATP, PFK_KitF6P, PFK_KitFDP, PFK_KmrADP, PFK_KmrATPMg, PFK_KmrF6P, PFK_KmrFDP, PFK_KmtADP, PFK_KmtATPMg, PFK_KmtF6P, PFK_KmtFDP, PFK_L0, MgADP, MgATP, PEP, PFK_Vmax, PFK_Wr, PFK_Wt, PFK_n);
  FBA: FDP -> DAP + GAP; cell*Function_for_FBA(DAP, FDP, GAP, FBA_Keq, FBA_KmDAP, FBA_KmFDP, FBA_KmGAP, FBA_KmPEP, PEP, FBA_Vmax);
  TPI: DAP -> GAP; cell*Function_for_TPI(DAP, GAP, TPI_Keq, TPI_KmDAP, TPI_KmGAP, TPI_Vmax);
  GDH: GAP + NAD + P -> BPG + NADH; cell*Function_for_GDH(BPG, GAP, GDH_Keq, GDH_KmBPG, GDH_KmGAP, GDH_KmNAD, GDH_KmNADH, GDH_KmP, NAD, NADH, P, GDH_Vmax);
  PGK: ADP + BPG -> ATP + PGA3; cell*Function_for_PGK(BPG, PGK_Keq, PGK_KmADPMg, PGK_KmATPMg, PGK_KmBPG, PGK_KmPGA3, MgADP, MgATP, PGA3, PGK_Vmax);
  GPM: PGA3 -> PGA2; cell*Function_for_GPM(GPM_Keq, GPM_KmPGA2, GPM_KmPGA3, PGA2, PGA3, GPM_Vmax);
  ENO: PGA2 -> PEP; cell*Function_for_ENO(ENO_Keq, ENO_KmPEP, ENO_KmPGA2, PEP, PGA2, ENO_Vmax);
  PYK: ADP + PEP => ATP + PYR; cell*Function_for_PYK(ADP, FDP, G6P, GL6P, PYK_KefrFDP, PYK_KefrG6P, PYK_KefrGL6P, PYK_KefrR5P, PYK_KefrRU5P, PYK_KefrS7P, PYK_KefrX5P, PYK_KeftATP, PYK_KeftSUCCOA, PYK_KirADP, PYK_KirATP, PYK_KirPEP, PYK_KirPYR, PYK_KirPyrATP, PYK_KitADP, PYK_KitATP, PYK_KitPEP, PYK_KitPYR, PYK_KitPyrATP, PYK_KmrADPMg, PYK_KmrPEP, PYK_KmtADPMg, PYK_KmtPEP, PYK_L0, MgADP, MgATP, PEP, PYR, R5P, RU5P, S7P, SUCCOA, PYK_Vmax, X5P, PYK_n);
  ZWF: G6P + NADP -> GL6P + NADPH; cell*Function_for_ZWF(G6P, GL6P, ZWF_KdG6P, ZWF_KdGL6P, ZWF_Keq, ZWF_KmG6P, ZWF_KmGL6P, ZWF_KmNADP, ZWF_KmNADPH, NADP, NADPH, ZWF_Vmax);
  PGL: GL6P -> PGN; cell*Function_for_PGL(G6P, GL6P, PGL_Keq, PGL_KiG6P, PGL_KmGL6P, PGL_KmPGN, PGN, PGL_Vmax);
  GND: NADP + PGN -> NADPH + RU5P + $HCO3; cell*Function_for_GND(ATP, FDP, HCO3, GND_KdHCO3, GND_KdHCO3NADPH, GND_KdNADP, GND_KdNADPH, GND_KdRu5P, GND_KefATP, GND_KefFbP, GND_KefNADPATP, GND_KefNADPFbP, GND_Keq, GND_KmHCO3, GND_KmNADP, GND_KmNADPH, GND_KmPGN, GND_KmRU5P, NADP, NADPH, PGN, RU5P, GND_Vmax);
  RPE: RU5P -> X5P; cell*Function_for_RPE(RPE_Keq, RPE_KmRU5P, RPE_KmX5P, RU5P, RPE_Vmax, X5P);
  RPI: RU5P -> R5P; cell*Function_for_RPI(E_4P, RPI_Keq, RPI_KmE4P, RPI_KmR5P, RPI_KmRU5P, R5P, RU5P, RPI_Vmax);
  X5P_GAP_TKT: tkt + X5P -> GAP + tktC2; cell*Function_for_X5P_GAP_TKT(GAP, X5P_GAP_TKT_Keq, X5P, X5P_GAP_TKT_kcat, tkt, tktC2);
  F6P_E4P_TKT: E_4P + tktC2 -> F6P + tkt; cell*Function_for_F6P_E4P_TKT(E_4P, F6P, F6P_E4P_TKT_Keq, F6P_E4P_TKT_kcat, tkt, tktC2);
  S7P_R5P_TKT: R5P + tktC2 -> S7P + tkt; cell*Function_for_S7P_R5P_TKT(S7P_R5P_TKT_Keq, R5P, S7P, S7P_R5P_TKT_kcat, tkt, tktC2);
  F6P_GAP_TAL: GAP + talC3 -> F6P + tal; cell*Function_for_F6P_GAP_TAL(F6P, GAP, F6P_GAP_TAL_Keq, F6P_GAP_TAL_kcat, tal, talC3);
  S7P_E4P_TAL: S7P + tal -> E_4P + talC3; cell*Function_for_S7P_E4P_TAL(E_4P, S7P_E4P_TAL_Keq, S7P, S7P_E4P_TAL_kcat, tal, talC3);
  FBP: FDP => F6P + P; cell*Function_for_FBP(AMP, F6P, FDP, KdFDPMg, FBP_KirAMP, FBP_KirAMPFDP, FBP_KirF6P, FBP_KirF6PMg, FBP_KirFDP, FBP_KirFDPMg, FBP_KirFDPMgMg, FBP_KirP, FBP_KirPF6P, FBP_KirPF6PMg, FBP_KirPMg, FBP_KitAMP, FBP_KitAMPFDP, FBP_KitF6P, FBP_KitF6PMg, FBP_KitFDP, FBP_KitFDPMg, FBP_KitFDPMgMg, FBP_KitP, FBP_KitPF6P, FBP_KitPF6PMg, FBP_KitPMg, FBP_KmrFDP, FBP_KmrMg, FBP_KmtFDP, FBP_KmtMg, FBP_L0, MG, MgFDP, P, FBP_Vmax, FBP_n);
  PPC: PEP + $HCO3 -> OAA + P; cell*Function_for_PPC(ACCOA, ASP, CIT, CYS, FDP, FUM, HCO3, PPC_KdrOAA, PPC_KdrPEP, PPC_KdtOAA, PPC_KdtPEP, PPC_KefrACCOA, PPC_KefrASP, PPC_KefrCIT, PPC_KefrCYS, PPC_KefrFDP, PPC_KefrFDPACCOA, PPC_KefrFUM, PPC_KefrMAL, PPC_KefrSUC, PPC_KeftACCOA, PPC_KeftASP, PPC_KeftCIT, PPC_KeftCYS, PPC_KeftFDP, PPC_KeftFDPACCOA, PPC_KeftFUM, PPC_KeftMAL, PPC_KeftSUC, PPC_Keq, PPC_KmrHCO3, PPC_KmrOAA, PPC_KmrP, PPC_KmrPEP, PPC_KmtHCO3, PPC_KmtOAA, PPC_KmtP, PPC_KmtPEP, PPC_L0, MAL, OAA, P, PEP, SUC, PPC_Vmax, PPC_n);
  PCK: ATP + OAA -> ADP + PEP + $HCO3; cell*Function_for_PCK(ADP, HCO3, PCK_Keq, PCK_KmADP, PCK_KmATP, PCK_KmHCO3, PCK_KmOAA, PCK_KmPEP, MgADP, MgATP, OAA, PEP, PCK_Vmax);
  PPS: ATP + PYR -> AMP + PEP + P; cell*Function_for_PPS(ADP, AKG, AMP, ATP, KdADPMg, PPS_KdAMP, KdATPMg, PPS_KdATPMgPPS, PPS_KdMg, PPS_KdP, PPS_KdPEP, PPS_KdPYR, PPS_KefADP, PPS_KefAKG, PPS_KefATP, PPS_KefOAA, PPS_Keq, PPS_KmAMP, PPS_KmATPMg, PPS_KmP, PPS_KmPEP, PPS_KmPYR, MG, MgADP, MgATP, OAA, P, PEP, PYR, PPS_Vmax, PPS_W, PPS_alpha);
  MAD: MAL + NAD => NADH + PYR + $HCO3; cell*Function_for_MAD(ACCOA, ASP, ATP, COA, MAD_KefrACCOA, MAD_KefrASP, MAD_KefrATP, MAD_KefrCOA, MAD_KeftACCOA, MAD_KeftASP, MAD_KeftATP, MAD_KeftCOA, MAD_KirNAD, MAD_KitNAD, MAD_KmrMAL, MAD_KmrMg, MAD_KmrMn, MAD_KmrNAD, MAD_KmtMAL, MAD_KmtMg, MAD_KmtMn, MAD_KmtNAD, MAD_L0, MAL, MG, MN, NAD, MAD_Vmax, MAD_n);
  PDH: $COA + NAD + PYR -> ACCOA + NADH + $HCO3; cell*Function_for_PDH(ACCOA, COA, HCO3, PDH_Keq, PDH_KmACCOA, PDH_KmCOA, PDH_KmHCO3, PDH_KmNAD, PDH_KmNADH, PDH_KmPYR, NAD, NADH, PYR, PDH_Vmax);
  GLT: ACCOA + OAA -> CIT + $COA; cell*Function_for_GLT(ACCOA, AKG, ATP, CIT, COA, GLT_KdACCOA0, GLT_KdcsCIT, GLT_KdcsCOA, GLT_KdcsOAA, GLT_Keq, GLT_Ki1AKG, GLT_Ki1NADH, GLT_Ki2AKG, GLT_Ki2NADH, GLT_KiATP, GLT_KmACCOA0, GLT_KmOAA0, GLT_KmcsCIT, GLT_KmcsCOA, NADH, OAA, GLT_Vmax);
  ACN_1: CIT -> ACO; cell*Function_for_ACN_1(ACO, CIT, ICIT, ACN_1_Keq, KmACO_ACN, KmCIT_ACN, KmICIT_ACN, ACN_1_Vmax);
  ACN_2: ACO -> ICIT; cell*Function_for_ACN_2(ACO, CIT, ICIT, ACN_2_Keq, KmACO_ACN, KmCIT_ACN, KmICIT_ACN, ACN_2_Vmax);
  ICD: ICIT + NADP -> AKG + NADPH + $HCO3; cell*Function_for_ICD(AKG, ICIT, ICD_Keq, ICD_KmAKG, ICD_KmICIT, ICD_KmNADP, ICD_KmNADPH, NADP, NADPH, icd, ICD_kcat);
  LPD: $COA + AKG + NAD => NADH + SUCCOA + $HCO3; cell*Function_for_LPD(AKG, COA, LPD_KdAKG, LPD_KmAKG, LPD_KmCOA, LPD_KmNAD, NAD, LPD_Vmax, LPD_alpha);
  SK: ADP + SUCCOA + P -> ATP + $COA + SUC; cell*Function_for_SK(ADP, ATP, COA, SK_Keq, SK_KmADP, SK_KmATP, SK_KmCOA, SK_KmP, SK_KmSUC, SK_KmSUCCOA, P, SUC, SUCCOA, SK_Vmax);
  SDH: FAD + SUC -> FUM + FADH2; cell*Function_for_SDH(FUM, SDH_KefFUM, SDH_KefSUC, SDH_Keq, SDH_KmFUM, SDH_KmQ, SDH_KmQH2, SDH_KmSUC, FAD, FADH2, SUC, SDH_Vmax);
  FUMA: FUM -> MAL; cell*Function_for_FUMA(FUM, FUMA_Keq, FUMA_KmFUM, FUMA_KmMAL, MAL, FUMA_Vmax);
  MQO: MAL + Q -> OAA + QH2; cell*Function_for_MQO(MQO_Keq, MQO_KmMAL, MQO_KmOAA, MQO_KmQ, MQO_KmQH2, MAL, OAA, Q, QH2, MQO_Vmax);
  MDH: QH2 + OAA -> MAL + Q; cell*Function_for_MDH(MDH_Keq, MDH_KiNAD, MDH_KiNADH, MDH_KiOAA, MDH_KmMAL, MDH_KmNAD, MDH_KmNADH, MDH_KmOAA, MAL, NAD, NADH, OAA, MDH_Vmax);
  ACEA: ICIT -> GLX + SUC; cell*Function_for_ACEA(GLX, ICIT, ACEA_KdICITsuc, ACEA_KdPEP, ACEA_KdPEPglx, ACEA_KdPEPicit, ACEA_KdPGA3, ACEA_KdSUC, ACEA_Keq, ACEA_KmGLX, ACEA_KmICIT, ACEA_KmSUC, PEP, PGA3, SUC, ACEA_Vmax);
  ACEB: ACCOA + GLX -> $COA + MAL; cell*Function_for_ACEB(ACCOA, COA, GLX, ACEB_Keq, ACEB_KmACCOA, ACEB_KmCOA, ACEB_KmGLX, ACEB_KmMAL, MAL, ACEB_Vmax);
  ACEK_1: ATP + icd -> ADP + icdP; cell*Function_for_ACEK_1(ADP, ATP, ACEK_1_Keq, icd, icdP, ACEK_1_k);
  ACEK_2: icdP -> icd + P; cell*Function_for_ACEK_2(ACEK_2_Keq, P, icd, icdP, ACEK_2_k);
  EDD: PGN -> KDPG; cell*Function_for_EDD(KDPG, EDD_Keq, EDD_KmKDPG, EDD_KmPGN, PGN, EDD_Vmax);
  EDA: KDPG -> GAP + PYR; cell*Function_for_EDA(GAP, KDPG, EDA_Keq, EDA_KmGAP, EDA_KmKDPG, EDA_KmPYR, PYR, EDA_Vmax);
  NADH_req: NADH + Q + 4$Hin -> NAD + QH2 + 4Hout; Function_for_NDH1(NADH_req_Vmax, Hin, Hout, NADH, Q, NAD, QH2, KeqNDH);
  PNT_req: NAD + NADPH -> NADH + NADP; cell*Function_for_PNT(PNT_req_Keq, NAD, NADH, NADP, NADPH, PNT_req_k);
  ADK: AMP + ATP -> 2ADP; cell*Function_for_ADK(ADP, AMP, ATP, ADK_Keq, ADK_k);
  ATP_syn: ADP + P + 4Hout -> ATP + 4$Hin; Function_for_ATP_SYN(ATP_syn_Vmax, Hin, Hout, ADP, P, ATP, ATP_syn_Keq);
  CYA: ATP -> CAMP + 2P; cell*Function_for_CYA(ATP, CAMP, CYA_Keq, P, CYA_k, eiiaP, CYA_KaeiiaP);
  DOS: CAMP -> AMP; cell*Function_for_DOS(AMP, CAMP, DOS_Keq, DOS_k);
  ACK: ACP + ADP -> ACEx + ATP; cell*Function_for_ACK(ACEx, ACP, ADP, ATP, ACK_Keq, ACK_KmACE, ACK_KmACP, ACK_KmADP, ACK_KmATP, ACK_Vmax, cell);
  ACS: ACEx + ATP + $COA => ACCOA + AMP + 2P; cell*Function_for_ACS(ACEx, ATP, COA, ACS_KmACE, ACS_KmATP, ACS_KmCOA, ACS_Vmax, cell);
  PTA: ACCOA + P -> $COA + ACP; cell*Function_for_PTA(ACCOA, ACP, COA, PTA_Keq, PTA_KiACCOA, PTA_KiACP, PTA_KiCOA, PTA_KiP, PTA_KmACP, PTA_KmP, P, PTA_Vmax);
  PTS_0: ei + PEP -> eiP + PYR; cell*Function_for_PTS_0(PTS_0_KmPEP, PTS_0_KmPYR, PEP, PYR, ei, eiP, PTS_0_kF, PTS_0_kR);
  PTS_1: hpr + eiP -> hprP + ei; cell*(PTS_1_k1*hpr*eiP - PTS_1_k2*hprP*ei);
  PTS_2: eiia + hprP -> eiiaP + hpr; cell*(PTS_2_k1*eiia*hprP - PTS_2_k2*eiiaP*hpr);
  PTS_3: eiicb + eiiaP -> eiicbP + eiia; cell*(PTS_3_k1*eiicb*eiiaP - PTS_3_k2*eiicbP*eiia);
  PTS_4: GLCp + eiicbP -> G6P + eiicb; Function_for_PTS_4(G6P, GLCp, PTS_4_KmG6P, PTS_4_KmGLC, cell, eiicb, eiicbP, PTS_4_kF, PTS_4_kR);
  GLC_feed:  => GLCx; extracellular*Function_for_GLC_FEED(FEED, cell, extracellular);
  CYTBO: 2QH2 + 8$Hin + $O2 -> 2Q + 8Hout + 2$H2O; Function_for_CYTBO(CYTBO_Vmax, Hin, Hout, CYTBO_Keq, O2, QH2, Q);
  SQR_: FADH2 + Q -> FAD + QH2; cell*Function_for_SQR(FADH2, Q, FAD, QH2, SQR_Keq, SQR_Vmax);
  NDHII: NADH + Q -> NAD + QH2; cell*Function_for_NDH2(NDHII_Vmax, NADH, Q, NAD, QH2, KeqNDH);
  GROWTH: 116G6P + 204 E_4P + 845PGA3 + 1010OAA + 610AKG + 1601PYR + 507R5P + 293PEP + 73GAP + 40F6P + 10169NADPH + 2118ACCOA + 2004NAD + 30508ATP => 10169NADP + 2118$COA + 2004NADH + 30508ADP + 30508P; cell*Function_for_GROWTH(GROWTH_Vmax, G6P, E_4P, PGA3, OAA, AKG, PYR, R5P, PEP, GAP, F6P, NADPH, ACCOA, NAD, ATP, GROWTH_KmG6P, GROWTH_KmE4P, GROWTH_KmPGA3, GROWTH_KmOAA, GROWTH_KmAKG, GROWTH_KmPYR, GROWTH_KmR5P, GROWTH_KmPEP, GROWTH_KmGAP, GROWTH_KmF6P, GROWTH_KmNADPH, GROWTH_KmACCOA, GROWTH_KmNAD, GROWTH_KmATP);
  ATP_MAINTENANCE: ATP -> ADP + P; cell*Function_for_ATP_MAINTENANCE(ATP_MAINTENANCE_Vmax, ADP, P, ATP, ATP_MAINTENANCE_Keq);
  XCH_GLC: GLCx -> GLCp; Function_for_XCH_RMM(XCH_GLC_Vmax, GLCx, GLCp, XCH_GLC_Km);
  PIT: Pp + Hout -> P + $Hin; Function_for_PIT(PIT_Vmax, Hout, Hin, Pp, PIT_KmPp, PIT_Kr, P, PIT_KmP);
  XCH_P: $Px -> Pp; Function_for_XCH_RMM(XCH_P_Vmax, Px, Pp, XCH_P_Km);
  XCH_ACE1: ACEx -> ACEp; Function_for_XCH_RMM(XCH_ACE1_Vmax, ACEx, ACEp, XCH_ACE1_Km);
  _ACE_OUT: ACEx_0 => ; extracellular*_ACE_OUT_k1*ACEx_0;
  XCH_ACE2: ACEp -> ACEx_0; Function_for_XCH_RMM(XCH_ACE2_Vmax, ACEp, ACEx_0, XCH_ACE2_Km);
  GL6P_HYDROLYSIS: GL6P -> PGN; cell*Function_for_GL6P_HYDROLYSIS(GL6P_HYDROLYSIS_KGl6Phydrol, GL6P, PGN, GL6P_HYDROLYSIS_KeqGl6Phydrol);

  // Species initializations:
  ACCOA = 0.154743005197164;
  ACO = 0.0321498018175313;
  ACP = 0.0143909273594558;
  AKG = 0.59787032384441;
  BPG = 0.0654105657862152;
  CIT = 0.0895304736844159;
  DAP = 0.437094067658024;
  E_4P = 0.131299932172739;
  F6P = 0.261766478740896;
  FDP = 0.281808159864253;
  FUM = 0.213114978422209;
  G6P = 0.861129502441293;
  GAP = 0.117183109596569;
  GL6P = 0.00326165203359758;
  GLX = 0.00881041031115986;
  ICIT = 0.105782426191547;
  KDPG = 0.0868176890659311;
  MAL = 1.03215312348775;
  NAD = 1.4115436522776;
  NADH = 0.158456348418614;
  NADP = 0.16783720710787;
  NADPH = 0.0891627925196171;
  OAA = 0.127839589734497;
  PEP = 0.997038344330946;
  PGA2 = 0.378297104706903;
  PGA3 = 0.696274165244089;
  PGN = 0.131599781202154;
  PYR = 0.236891381334918;
  Q = 0.326117384176523;
  QH2 = 0.673882615474956;
  R5P = 0.106841687532834;
  RU5P = 0.341826588051515;
  S7P = 0.141985142359057;
  SUC = 0.216055294883695;
  SUCCOA = 0.0410877780107645;
  X5P = 0.506017991063706;
  ei = 0.00033401303458514;
  eiP = 0.00638116273837147;
  eiia = 0.0142018557253279;
  eiiaP = 0.48056854395108;
  eiicb = 4.7190967217532e-005;
  eiicbP = 0.000342621394230619;
  hpr = 0.000191211795334012;
  hprP = 0.00525081181407641;
  icd = 0.000542743814193054;
  icdP = 0.0514572567075189;
  tal = 0.00278094383903305;
  talC3 = 0.0572190561261228;
  tkt = 0.0138307829063354;
  tktC2 = 0.0561692170121894;
  ADP = 0.598314702968157;
  AMP = 0.186252612968725;
  ATP = 2.57220146109274;
  CAMP = 0.923131385715857;
  COA = 0.5;
  HCO3 = 1.4;
  P = 9.7639478565112;
  MG = 1;
  ASP = 1.17;
  CYS = 0.085;
  MN = 0.3;
  Hin = 3.16227766e-005;
  H2O = 1;
  O2 = 0.21;
  FAD = 0.253914296785258;
  FADH2 = 0.746085703291575;
  ACEx = 0.000186707816309202;
  GLCx = 0.00633336972696918;
  Px = 10;
  ACEx_0 = 0.000186687071641801;
  Hout = 5.37448236126923e-005;
  GLCp = 0.00403336972696918;
  Pp = 9.99942809822305;
  ACEp = 0.000186697443975502;

  // Compartment initializations:
  cell = 1;
  extracellular = 100;
  cell_periplasm = 0.25;

  // Variable initializations:
  KdADPMg = 1.27771;
  KdATPMg = 0.0847634;
  KdFDPMg = 5.81;
  FEED = 0.23;
  KmICIT_ACN = 9.31352;
  KmCIT_ACN = 0.0628882;
  KmACO_ACN = 0.02001;
  KeqNDH = 27.6193;
  PGI_Keq = 0.36;
  PGI_KmF6P = 0.147;
  PGI_KmG6P = 0.28;
  PGI_KmPEP = 1.999;
  PGI_Vmax = 2.32456;
  PGI_KmPGN = 0.515958;
  PFK_KefrADP = 0.0735264;
  PFK_KefrPEP = 19.98;
  PFK_KeftADP = 9.009;
  PFK_KeftPEP = 0.26026;
  PFK_Keq = 1998;
  PFK_KirADP = 54.945;
  PFK_KirATP = 2.4975e-005;
  PFK_KirF6P = 1.84615;
  PFK_KirFDP = 0.045954;
  PFK_KitADP = 80.08;
  PFK_KitATP = 0.014014;
  PFK_KitF6P = 0.00856856;
  PFK_KitFDP = 50.5505;
  PFK_KmrADP = 0.690009;
  PFK_KmrATPMg = 8.12187e-005;
  PFK_KmrF6P = 2.05205e-005;
  PFK_KmrFDP = 10.01;
  PFK_KmtADP = 2.002;
  PFK_KmtATPMg = 3.34334;
  PFK_KmtF6P = 32.967;
  PFK_KmtFDP = 9.99;
  PFK_L0 = 14.0851;
  PFK_Vmax = 0.185253;
  PFK_Wr = 0.0237041;
  PFK_Wt = 0.146735;
  PFK_n = 4;
  FBA_Keq = 0.18981;
  FBA_KmDAP = 0.13001;
  FBA_KmFDP = 0.12012;
  FBA_KmGAP = 0.13001;
  FBA_KmPEP = 0.5;
  FBA_Vmax = 21.6978;
  TPI_Keq = 0.270203;
  TPI_KmDAP = 0.01;
  TPI_KmGAP = 1.89301;
  TPI_Vmax = 24.1843;
  GDH_Keq = 20;
  GDH_KmBPG = 0.2;
  GDH_KmGAP = 2.47265;
  GDH_KmNAD = 0.0110454;
  GDH_KmNADH = 3.69797;
  GDH_KmP = 0.017;
  GDH_Vmax = 8.66573;
  PGK_Keq = 99.9925;
  PGK_KmADPMg = 0.085416;
  PGK_KmATPMg = 3.47737;
  PGK_KmBPG = 0.0113296;
  PGK_KmPGA3 = 2.45722;
  PGK_Vmax = 16.1089;
  GPM_Keq = 0.565818;
  GPM_KmPGA2 = 1.9153;
  GPM_KmPGA3 = 0.115;
  GPM_Vmax = 10.9934;
  ENO_Keq = 3;
  ENO_KmPEP = 0.1;
  ENO_KmPGA2 = 0.1;
  ENO_Vmax = 11.7189;
  PYK_KefrFDP = 0.449149;
  PYK_KefrG6P = 0.158746;
  PYK_KefrGL6P = 0.150482;
  PYK_KefrR5P = 9.33254;
  PYK_KefrRU5P = 1.53591;
  PYK_KefrS7P = 0.0785955;
  PYK_KefrX5P = 0.677374;
  PYK_KeftATP = 3.69117;
  PYK_KeftSUCCOA = 8.26406;
  PYK_KirADP = 0.517585;
  PYK_KirATP = 96.0333;
  PYK_KirPEP = 0.181056;
  PYK_KirPYR = 15.1403;
  PYK_KirPyrATP = 230.781;
  PYK_KitADP = 0.224911;
  PYK_KitATP = 0.039564;
  PYK_KitPEP = 0.465672;
  PYK_KitPYR = 0.2499;
  PYK_KitPyrATP = 11.3691;
  PYK_KmrADPMg = 0.326144;
  PYK_KmrPEP = 5.56368e-007;
  PYK_KmtADPMg = 0.054678;
  PYK_KmtPEP = 0.11475;
  PYK_L0 = 50.4818;
  PYK_Vmax = 0.74716;
  PYK_n = 4;
  ZWF_KdG6P = 0.192;
  ZWF_KdGL6P = 0.02;
  ZWF_Keq = 60000000000;
  ZWF_KmG6P = 0.118525;
  ZWF_KmGL6P = 0.328629;
  ZWF_KmNADP = 0.0274;
  ZWF_KmNADPH = 0.0168;
  ZWF_Vmax = 0.2658;
  PGL_Keq = 42.7572;
  PGL_KiG6P = 2.0001;
  PGL_KmGL6P = 0.022977;
  PGL_KmPGN = 9.99;
  PGL_Vmax = 11.5967;
  GND_KdHCO3 = 58.8951;
  GND_KdHCO3NADPH = 9.7257;
  GND_KdNADP = 0.116989;
  GND_KdNADPH = 0.00340034;
  GND_KdRu5P = 0.0440044;
  GND_KefATP = 0.0650065;
  GND_KefFbP = 0.0129987;
  GND_KefNADPATP = 0.139986;
  GND_KefNADPFbP = 0.00519948;
  GND_Keq = 49.962;
  GND_KmHCO3 = 6.41899;
  GND_KmNADP = 0.049;
  GND_KmNADPH = 68.3828;
  GND_KmPGN = 0.093;
  GND_KmRU5P = 45.1977;
  GND_Vmax = 4.08105;
  RPE_Keq = 1.5015;
  RPE_KmRU5P = 0.872522;
  RPE_KmX5P = 0.893607;
  RPE_Vmax = 6.00103;
  RPI_Keq = 0.330093;
  RPI_KmE4P = 0.67067;
  RPI_KmR5P = 3.09715;
  RPI_KmRU5P = 4.40263;
  RPI_Vmax = 8;
  X5P_GAP_TKT_Keq = 1.001;
  X5P_GAP_TKT_kcat = 40;
  F6P_E4P_TKT_Keq = 0.5005;
  F6P_E4P_TKT_kcat = 40.0002;
  S7P_R5P_TKT_Keq = 0.33033;
  S7P_R5P_TKT_kcat = 199.979;
  F6P_GAP_TAL_Keq = 0.11011;
  F6P_GAP_TAL_kcat = 119.992;
  S7P_E4P_TAL_Keq = 26.6266;
  S7P_E4P_TAL_kcat = 99.9991;
  FBP_KirAMP = 0.00122122;
  FBP_KirAMPFDP = 0.256256;
  FBP_KirF6P = 1.12112;
  FBP_KirF6PMg = 0.384615;
  FBP_KirFDP = 1.35327;
  FBP_KirFDPMg = 0.75924;
  FBP_KirFDPMgMg = 0.356356;
  FBP_KirP = 3.16316;
  FBP_KirPF6P = 6.60538;
  FBP_KirPF6PMg = 48.4484;
  FBP_KirPMg = 0.856;
  FBP_KitAMP = 0.000255;
  FBP_KitAMPFDP = 690;
  FBP_KitF6P = 0.304;
  FBP_KitF6PMg = 315;
  FBP_KitFDP = 0.043101;
  FBP_KitFDPMg = 0.00642;
  FBP_KitFDPMgMg = 100;
  FBP_KitP = 0.642;
  FBP_KitPF6P = 0.00689;
  FBP_KitPF6PMg = 16.5;
  FBP_KitPMg = 539;
  FBP_KmrFDP = 0.0636141;
  FBP_KmrMg = 0.039039;
  FBP_KmtFDP = 1e-005;
  FBP_KmtMg = 55.055;
  FBP_L0 = 0.000815;
  FBP_Vmax = 0.215583;
  FBP_n = 4;
  PPC_KdrOAA = 4.35404;
  PPC_KdrPEP = 655.591;
  PPC_KdtOAA = 17.9127;
  PPC_KdtPEP = 0.0121991;
  PPC_KefrACCOA = 0.140029;
  PPC_KefrASP = 0.389183;
  PPC_KefrCIT = 34.4277;
  PPC_KefrCYS = 0.000448843;
  PPC_KefrFDP = 9.99126;
  PPC_KefrFDPACCOA = 0.0156251;
  PPC_KefrFUM = 2.7475;
  PPC_KefrMAL = 0.23002;
  PPC_KefrSUC = 22.9834;
  PPC_KeftACCOA = 1.27598;
  PPC_KeftASP = 27.4729;
  PPC_KeftCIT = 0.521945;
  PPC_KeftCYS = 0.977374;
  PPC_KeftFDP = 13.2064;
  PPC_KeftFDPACCOA = 47.7563;
  PPC_KeftFUM = 9.76119;
  PPC_KeftMAL = 0.737283;
  PPC_KeftSUC = 107.18;
  PPC_Keq = 149.705;
  PPC_KmrHCO3 = 0.00219811;
  PPC_KmrOAA = 13.0469;
  PPC_KmrP = 0.663356;
  PPC_KmrPEP = 3.20089;
  PPC_KmtHCO3 = 0.00220031;
  PPC_KmtOAA = 6.80995;
  PPC_KmtP = 0.285131;
  PPC_KmtPEP = 5.12497;
  PPC_L0 = 6.37209e-006;
  PPC_Vmax = 21.439;
  PPC_n = 4.00319;
  PCK_Keq = 1.88166;
  PCK_KmADP = 0.04997;
  PCK_KmATP = 0.0600418;
  PCK_KmHCO3 = 2.6319;
  PCK_KmOAA = 0.66966;
  PCK_KmPEP = 0.0699833;
  PCK_Vmax = 8.08777;
  PPS_KdAMP = 1480;
  PPS_KdATPMgPPS = 0.0549;
  PPS_KdMg = 36.9;
  PPS_KdP = 346;
  PPS_KdPEP = 95.7;
  PPS_KdPYR = 2740;
  PPS_KefADP = 0.0283;
  PPS_KefAKG = 0.274;
  PPS_KefATP = 0.000628;
  PPS_KefOAA = 0.796;
  PPS_Keq = 200000;
  PPS_KmAMP = 0.000384;
  PPS_KmATPMg = 0.0549;
  PPS_KmP = 84.4;
  PPS_KmPEP = 20.7;
  PPS_KmPYR = 0.229;
  PPS_Vmax = 0.0163772;
  PPS_W = 10;
  PPS_alpha = 38900;
  MAD_KefrACCOA = 1.83336;
  MAD_KefrASP = 0.362142;
  MAD_KefrATP = 88.9752;
  MAD_KefrCOA = 0.268;
  MAD_KeftACCOA = 0.197;
  MAD_KeftASP = 0.583;
  MAD_KeftATP = 0.26;
  MAD_KeftCOA = 0.268;
  MAD_KirNAD = 0.636457;
  MAD_KitNAD = 0.990398;
  MAD_KmrMAL = 0.212913;
  MAD_KmrMg = 0.191871;
  MAD_KmrMn = 0.272568;
  MAD_KmrNAD = 1.36636;
  MAD_KmtMAL = 0.093;
  MAD_KmtMg = 2.37681;
  MAD_KmtMn = 0.410198;
  MAD_KmtNAD = 0.108;
  MAD_L0 = 19.9;
  MAD_Vmax = 6.64269;
  MAD_n = 4;
  PDH_Keq = 3138.16;
  PDH_KmACCOA = 10.174;
  PDH_KmCOA = 0.00500461;
  PDH_KmHCO3 = 0.00545112;
  PDH_KmNAD = 0.00999;
  PDH_KmNADH = 6.63512;
  PDH_KmPYR = 2;
  PDH_Vmax = 961.706;
  GLT_KdACCOA0 = 0.699309;
  GLT_KdcsCIT = 7.38128;
  GLT_KdcsCOA = 0.00174282;
  GLT_KdcsOAA = 0.154601;
  GLT_Keq = 83067.1;
  GLT_Ki1AKG = 0.0150083;
  GLT_Ki1NADH = 0.000330313;
  GLT_Ki2AKG = 0.256252;
  GLT_Ki2NADH = 0.0504;
  GLT_KiATP = 0.579939;
  GLT_KmACCOA0 = 0.119974;
  GLT_KmOAA0 = 0.00123458;
  GLT_KmcsCIT = 1.15715;
  GLT_KmcsCOA = 9.6344e-005;
  GLT_Vmax = 57.0584;
  ACN_1_Keq = 0.384503;
  ACN_1_Vmax = 9.72413;
  ACN_2_Keq = 3.49183;
  ACN_2_Vmax = 9.86571;
  ICD_Keq = 28.1631;
  ICD_KmAKG = 0.038038;
  ICD_KmICIT = 0.010989;
  ICD_KmNADP = 0.005994;
  ICD_KmNADPH = 0.000683333;
  ICD_kcat = 2461.97;
  LPD_KdAKG = 14.9386;
  LPD_KmAKG = 0.020002;
  LPD_KmCOA = 0.0760076;
  LPD_KmNAD = 0.0980098;
  LPD_Vmax = 0.0684413;
  LPD_alpha = 16.4304;
  SK_Keq = 1.15994;
  SK_KmADP = 0.00868475;
  SK_KmATP = 0.102321;
  SK_KmCOA = 0.255019;
  SK_KmP = 0.914709;
  SK_KmSUC = 0.800744;
  SK_KmSUCCOA = 0.0085;
  SK_Vmax = 76.8163;
  SDH_KefFUM = 0.067048;
  SDH_KefSUC = 0.0322425;
  SDH_Keq = 2250;
  SDH_KmFUM = 1.36019;
  SDH_KmQ = 0.00160718;
  SDH_KmQH2 = 0.00611663;
  SDH_KmSUC = 0.805727;
  SDH_Vmax = 1.56184;
  FUMA_Keq = 4.99966;
  FUMA_KmFUM = 0.6;
  FUMA_KmMAL = 0.7;
  FUMA_Vmax = 53.3414;
  MQO_Keq = 9;
  MQO_KmMAL = 0.435;
  MQO_KmOAA = 75.8036;
  MQO_KmQ = 0.0414;
  MQO_KmQH2 = 8.77942;
  MQO_Vmax = 4.62283;
  MDH_Keq = 100000;
  MDH_KiNAD = 0.0233122;
  MDH_KiNADH = 0.000196981;
  MDH_KiOAA = 2.46446;
  MDH_KmMAL = 0.86;
  MDH_KmNAD = 0.64;
  MDH_KmNADH = 0.003;
  MDH_KmOAA = 0.001;
  MDH_Vmax = 6.11492;
  ACEA_KdICITsuc = 0.00489074;
  ACEA_KdPEP = 1.05105;
  ACEA_KdPEPglx = 0.0358555;
  ACEA_KdPEPicit = 0.164263;
  ACEA_KdPGA3 = 0.8;
  ACEA_KdSUC = 0.53053;
  ACEA_Keq = 8.8088;
  ACEA_KmGLX = 0.13013;
  ACEA_KmICIT = 0.063063;
  ACEA_KmSUC = 0.58941;
  ACEA_Vmax = 1.52595;
  ACEB_Keq = 230000;
  ACEB_KmACCOA = 0.009;
  ACEB_KmCOA = 10.5652;
  ACEB_KmGLX = 0.021;
  ACEB_KmMAL = 15.0572;
  ACEB_Vmax = 0.352769;
  ACEK_1_Keq = 888;
  ACEK_1_k = 1.25457;
  ACEK_2_Keq = 400;
  ACEK_2_k = 0.0332;
  EDD_Keq = 1000;
  EDD_KmKDPG = 0.318316;
  EDD_KmPGN = 0.6;
  EDD_Vmax = 0.111359;
  EDA_Keq = 0.5;
  EDA_KmGAP = 86.678;
  EDA_KmKDPG = 0.06;
  EDA_KmPYR = 10;
  EDA_Vmax = 0.0775241;
  NADH_req_Vmax = 23.0735;
  PNT_req_Keq = 0.181891;
  PNT_req_k = 2.49441;
  ADK_Keq = 0.962758;
  ADK_k = 0.242256;
  ATP_syn_Vmax = 108.733;
  ATP_syn_Keq = 49.8315;
  CYA_Keq = 2591.19;
  CYA_k = 0.00414418;
  CYA_KaeiiaP = 0.180981;
  DOS_Keq = 674.242;
  DOS_k = 0.00828;
  ACK_Keq = 174;
  ACK_KmACE = 7;
  ACK_KmACP = 0.16;
  ACK_KmADP = 0.5;
  ACK_KmATP = 0.07;
  ACK_Vmax = 7.23;
  ACS_KmACE = 0.07;
  ACS_KmATP = 0.1;
  ACS_KmCOA = 0.01;
  ACS_Vmax = 7.3;
  PTA_Keq = 0.0053952;
  PTA_KiACCOA = 0.2;
  PTA_KiACP = 0.2;
  PTA_KiCOA = 0.029;
  PTA_KiP = 13.54;
  PTA_KmACP = 0.7;
  PTA_KmP = 6.1;
  PTA_Vmax = 2.7;
  PTS_0_KmPEP = 0.6;
  PTS_0_KmPYR = 1;
  PTS_0_kF = 12000;
  PTS_0_kR = 8000;
  PTS_1_k1 = 200000;
  PTS_1_k2 = 8000;
  PTS_2_k1 = 61000;
  PTS_2_k2 = 47000;
  PTS_3_k1 = 11000;
  PTS_3_k2 = 4000;
  PTS_4_KmG6P = 2125.91;
  PTS_4_KmGLC = 0.02;
  PTS_4_kF = 4000;
  PTS_4_kR = 1e-005;
  CYTBO_Vmax = 8.54045;
  CYTBO_Keq = 12.067;
  SQR_Keq = 0.94033;
  SQR_Vmax = 3.41617;
  NDHII_Vmax = 30.8306;
  GROWTH_Vmax = 9.74137;
  GROWTH_KmG6P = 1.20911;
  GROWTH_KmE4P = 1.63298;
  GROWTH_KmPGA3 = 0.0764619;
  GROWTH_KmOAA = 0.0248351;
  GROWTH_KmAKG = 5.11989;
  GROWTH_KmPYR = 0.00463904;
  GROWTH_KmR5P = 0.021234;
  GROWTH_KmPEP = 0.457734;
  GROWTH_KmGAP = 0.024854;
  GROWTH_KmF6P = 0.366423;
  GROWTH_KmNADPH = 3.59774;
  GROWTH_KmACCOA = 0.0494404;
  GROWTH_KmNAD = 2.82239;
  GROWTH_KmATP = 0.0468266;
  ATP_MAINTENANCE_Vmax = 1.30166;
  ATP_MAINTENANCE_Keq = 3.63369;
  XCH_GLC_Vmax = 100;
  XCH_GLC_Km = 10;
  PIT_Vmax = 7.146;
  PIT_KmPp = 0.025;
  PIT_Kr = 0.1;
  PIT_KmP = 12.18;
  XCH_P_Vmax = 100;
  XCH_P_Km = 10;
  XCH_ACE1_Vmax = 100;
  XCH_ACE1_Km = 10;
  _ACE_OUT_k1 = 5.556e-005;
  XCH_ACE2_Vmax = 100;
  XCH_ACE2_Km = 10;
  GL6P_HYDROLYSIS_KGl6Phydrol = 0.000167;
  GL6P_HYDROLYSIS_KeqGl6Phydrol = 42.8;

  // Other declarations:
  const cell, extracellular, cell_periplasm, KdADPMg, KdATPMg, KdFDPMg, FEED;
  const KmICIT_ACN, KmCIT_ACN, KmACO_ACN, KeqNDH;

  // Unit definitions:
  unit substance = 1e-3 mole;

  // Display Names:
  cell is "cell_cytoplasm";
  ACEx is "ACE";
  ACEx_0 is "ACEx";
  MAD is "MAE";
  NADH_req is "NDHI";
  PNT_req is "PNT";
  ATP_syn is "ATP_SYN";
  GLC_feed is "_GLC_FEED";
end
''')

m = r.simulate (0, 500, 5000)
r.plot(loc=None)

