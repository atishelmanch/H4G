import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils

process = cms.Process("FLASHggMicroAOD")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff") # gives deprecated message in 80X but still runs
from Configuration.AlCa.GlobalTag import GlobalTag

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( -1) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1000 )

import os
if os.environ["CMSSW_VERSION"].count("CMSSW_7_6"):
    process.GlobalTag = GlobalTag(process.GlobalTag, '76X_mcRun2_asymptotic_v13')
elif os.environ["CMSSW_VERSION"].count("CMSSW_8_0"):
    process.GlobalTag = GlobalTag(process.GlobalTag,'80X_mcRun2_asymptotic_v11')
else:
    raise Exception,"The default setup for microAODstd.py does not support releases other than 76X and 80X"

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService")
process.RandomNumberGeneratorService.flashggRandomizedPhotons = cms.PSet(
          initialSeed = cms.untracked.uint32(16253245)
        )

# 2012 data
#process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_R_74_V8A::All')
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring(
#        "/store/relval/CMSSW_7_4_0_pre9/DoubleElectron/MINIAOD/GR_R_74_V8A_RelVal_zEl2012D-v1/00000/5A04EF0A-29D4-E411-BB12-003048FFCC2C.root",
#        "/store/relval/CMSSW_7_4_0_pre9/DoubleElectron/MINIAOD/GR_R_74_V8A_RelVal_zEl2012D-v1/00000/A6D4F50A-29D4-E411-98A2-002618943838.root",
#        "/store/relval/CMSSW_7_4_0_pre9/DoubleElectron/MINIAOD/GR_R_74_V8A_RelVal_zEl2012D-v1/00000/DE947AB8-FED3-E411-995F-0025905AA9F0.root"
#        ))

# PHYS14 Files
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring(
#"/store/mc/Phys14DR/DYToMuMu_M-50_Tune4C_13TeV-pythia8/MINIAODSIM/PU40bx25_tsg_castor_PHYS14_25_V1-v2/00000/622CAFBA-BD9A-E411-BE11-002481E14FFC.root",
#"/store/mc/Phys14DR/DYToMuMu_M-50_Tune4C_13TeV-pythia8/MINIAODSIM/PU40bx25_tsg_castor_PHYS14_25_V1-v2/00000/FA4B46B9-8E9A-E411-A899-002590A3C954.root",
#"/store/mc/Phys14DR/DYToMuMu_M-50_Tune4C_13TeV-pythia8/MINIAODSIM/PU40bx25_tsg_castor_PHYS14_25_V1-v2/10000/8607F88E-F799-E411-A180-0025B3E063F0.root",
#"/store/mc/Phys14DR/DYToMuMu_M-50_Tune4C_13TeV-pythia8/MINIAODSIM/PU40bx25_tsg_castor_PHYS14_25_V1-v2/10000/F620A7C9-F799-E411-8DEF-002590A371AC.root"
#))
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/Phys14DR/GluGluToHToGG_M-125_13TeV-powheg-pythia6/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/3C2EFAB1-B16F-E411-AB34-7845C4FC39FB.root"))
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/Phys14DR/VBF_HToGG_M-125_13TeV-powheg-pythia6/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/4A8E0BD1-026C-E411-8760-00266CFFA418.root"))
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/Phys14DR/WH_ZH_HToGG_M-125_13TeV_pythia6/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/24B70163-5769-E411-93CA-002590200A28.root"))
### process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/Phys14DR/GJet_Pt40_doubleEMEnriched_TuneZ2star_13TeV-pythia6/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/101611CC-026E-E411-B8D7-00266CFFBF88.root"))
## process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/Phys14DR/GJets_HT-100to200_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/00D67F78-2873-E411-B3BB-0025907DC9C0.root"))

# 740 RelVal
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/relval/CMSSW_7_4_0_pre9_ROOT6/RelValH130GGgluonfusion_13/MINIAODSIM/MCRUN2_74_V7-v1/00000/0A35F6D-DAD1-E411-A8CC-0026189438CC.root"))
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/relval/CMSSW_7_4_0_pre9/RelValH130GGgluonfusion_13/MINIAODSIM/PU25ns_MCRUN2_74_V7-v1/00000/5ABC049C-4CD4-E411-B28A-0025905A613C.root",
#                                                                         "/store/relval/CMSSW_7_4_0_pre9/RelValH130GGgluonfusion_13/MINIAODSIM/PU25ns_MCRUN2_74_V7-v1/00000/C65FAFAA-4CD4-E411-9026-0025905A607E.root"))

# Spring15
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/RunIISpring15DR74/ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/70000/0232BC3C-01FF-E411-8779-0025907B4FC2.root"))
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/RunIISpring15DR74/GluGluHToGG_M-125_13TeV_powheg_pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/30000/54ECB9A4-912E-E511-BB7D-002590A831CA.root"))
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("file:/afs/cern.ch/work/s/sethzenz/public/GluGluHToGG_M-125_13TeV_powheg_pythia8_MINIAODSIM_Asympt50ns_MCRUN2_74_V9A-v1_54ECB9A4-912E-E511-BB7D-002590A831CA.root"))

# IF YOU RUN ON ANY EXAMPLE ABOVE, YOU NEED TO CHANGE THE WEIGHTPRODUCER BELOW

# reMiniAOD
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/RunIISpring15MiniAODv2/VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/6C4EEC22-C36D-E511-8CCF-002590AC4C74.root"))
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/data/Run2015D/DoubleEG/MINIAOD/05Oct2015-v1/50000/DEDE4FB0-556F-E511-9F9F-0025905B85E8.root"))
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/RunIISpring15MiniAODv2/GluGluHToGG_M-125_13TeV_powheg_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/048F7B0F-0A6E-E511-B710-00259073E37A.root"))
#process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/mc/RunIIFall15DR76/GluGluHToGG_M-125_13TeV_powheg_pythia8/MINIAODSIM/25nsFlat10to25TSG_76X_mcRun2_asymptotic_v12-v1/00000/0C6C1B51-9198-E511-B305-002590747D94.root"))
  
process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring(
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_1.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_10.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_11.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_12.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_13.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_14.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_15.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_16.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_17.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_18.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_19.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_2.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_20.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_21.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_22.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_23.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_24.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_25.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_26.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_27.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_28.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_29.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_3.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_30.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_31.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_32.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_33.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_34.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_36.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_37.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_38.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_39.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_4.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_40.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_41.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_42.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_43.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_44.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_45.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_46.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_47.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_48.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_49.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_5.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_50.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_51.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_52.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_53.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_54.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_55.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_56.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_57.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_58.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_59.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_6.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_60.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_61.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_62.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_63.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_64.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_65.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_66.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_67.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_68.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_7.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_8.root',
        'file:eos/cms/store/user/amassiro/H4G/GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8_FIX_3/AOD_miniAOD-RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_tris_FIX_3/160627_230328/0000/HIG-RunIIFall15MiniAODv2-00711_9.root'
  ))



process.MessageLogger.cerr.threshold = 'ERROR' # can't get suppressWarning to work: disable all warnings for now
# process.MessageLogger.suppressWarning.extend(['SimpleMemoryCheck','MemoryCheck']) # this would have been better...

# Uncomment the following if you notice you have a memory leak
# This is a lightweight tool to digg further
#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",
#                                        ignoreTotal = cms.untracked.int32(1),
#                                        monitorPssAndPrivate = cms.untracked.bool(True)
#                                       )

process.load("flashgg/MicroAOD/flashggMicroAODSequence_cff")

# NEEDED FOR ANYTHING PRIOR TO reMiniAOD
#process.weightsCount.pileupInfo = "addPileupInfo"

from flashgg.MicroAOD.flashggMicroAODOutputCommands_cff import microAODDefaultOutputCommand
process.out = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string('/tmp/amassiro/myMicroAODOutputFile_GluGluToXToAATo4G_mX_750GeV_mA_370GeV_Pythia8.root'),
                               outputCommands = microAODDefaultOutputCommand
                               )

# All jets are now handled in MicroAODCustomize.py
# Switch from PFCHS to PUPPI with puppi=1 argument (both if puppi=2)

process.p = cms.Path(process.flashggMicroAODSequence)
process.e = cms.EndPath(process.out)

# Uncomment these lines to run the example commissioning module and send its output to root
#process.commissioning = cms.EDAnalyzer('flashggCommissioning',
#                                       PhotonTag=cms.untracked.InputTag('flashggPhotons'),
#                                       DiPhotonTag = cms.untracked.InputTag('flashggDiPhotons'),
#                                       VertexTag=cms.untracked.InputTag('offlineSlimmedPrimaryVertices')
#)
#process.TFileService = cms.Service("TFileService",
#                                   fileName = cms.string("commissioningTree.root")
#)
#process.p *= process.commissioning


from flashgg.MicroAOD.MicroAODCustomize import customize
customize(process)

if "DY" in customize.datasetName or "SingleElectron" in customize.datasetName or "DoubleEG" in customize.datasetName:
  customize.customizeHLT(process)
