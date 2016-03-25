## H->aa->4gamma Signal MC Production

#### Pythia8 signal instructions
Based on Pythia6 RunI H->aa->bbtautau signal (from Abdollah: https://www.dropbox.com/s/egntcw42szj9qif/mmtt_ma35_cfg.py?dl=0)   
Pythia doesn't do h(125)->aa, but it does H->hh with 2HDM model. So, make m(H) = 125 and m(h) = [5,60].   
Full Pythia8 fragment is in this repository.   
Cannot use POWHEG LHE because it produces h(125) - pdgid 25.   

#### CMS GEN Production
##### Step 0
cmsDriver.py Configuration/GenProduction/python/Step0_GluGluToHToXXTo4G-fragment.py --fileout file:HIG-RunIISummer15GS-00174.root --mc --eventcontent RAWSIM --era Run2_25ns --datatier GEN-SIM --conditions 76X_mcRun2_asymptotic_v12 --pileup 2015_25ns_FallMC_matchData_PoissonOOTPU --step GEN,SIM --magField 38T_PostLS1 --python_filename HIG-RunIISummer15GS-00174_1_cfg.py --no_exec -n 32   
##### Step 1