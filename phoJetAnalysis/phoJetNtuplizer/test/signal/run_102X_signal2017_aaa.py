import FWCore.ParameterSet.Config as cms

process = cms.Process("Analyzer")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff" )
process.load("Geometry.CaloEventSetup.CaloTowerConstituents_cfi")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '102X_mc2017_realistic_v6')
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v17')

#jec from sqlite
process.load("CondCore.CondDB.CondDB_cfi")
from CondCore.CondDB.CondDB_cfi import *
process.CondDB.connect = 'sqlite:Fall17_17Nov2017_V32_102X_MC.db'
process.jec = cms.ESSource("PoolDBESSource",CondDB,
    toGet = cms.VPSet(
      cms.PSet(
	record = cms.string('JetCorrectionsRecord'),
	tag    = cms.string('JetCorrectorParametersCollection_Fall17_17Nov2017_V32_102X_MC_AK4PFchs'),
	label  = cms.untracked.string('AK4PFchs')
	)
##      ,
##      cms.PSet(
##	record = cms.string('JetCorrectionsRecord'),
##	tag    = cms.string('JetCorrectorParametersCollection_Fall17_17Nov2017_V32_102X_MC_AK8PFPuppi'),
##	label  = cms.untracked.string('AK8PFPuppi')
##	)
      )
    )
process.es_prefer_jec = cms.ESPrefer('PoolDBESSource','jec')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#        'file:/hdfs/store/user/varuns/TEST-INPUTFILES/test_mc_12Apr2018_94X.root'
        #'file:/hdfs/store/user/ms/MonoHiggs_2017_signalSample_MINIAOD/2HDMa_bb_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_150_MH2_300_MHC_300-miniAOD_submit/miniAOD_submit-AOD_submit-REDIGI_submit-2HDMa_bb_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_150_MH2_300_MHC_300-0000.root',
        #'file:/afs/hep.wisc.edu/home/ms/monoHiggs_signal_sample/CMSSW_9_4_7/src/monoHiggsTauTau_2017MiniAOD.root'
        'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0000.root',
        'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0001.root',
        'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0002.root',
        'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0003.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0004.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0005.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0006.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0007.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0008.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0009.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0010.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0011.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0012.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0013.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0014.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0015.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0016.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0017.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0018.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0019.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0020.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0021.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0022.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0023.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0024.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0025.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0026.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0027.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0028.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0029.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0030.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0031.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0032.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0033.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0034.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0035.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0036.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0037.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0038.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0039.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0040.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0041.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0042.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0043.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0044.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0045.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0046.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0047.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0048.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0049.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0050.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0051.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0052.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0053.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0054.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0055.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0056.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0057.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0058.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0059.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0060.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0061.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0062.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0063.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0064.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0065.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0066.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0067.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0068.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0069.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0070.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0071.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0072.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0073.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0074.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0075.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0076.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0077.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0078.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0079.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0080.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0081.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0082.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0083.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0084.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0085.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0086.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0087.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0088.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0089.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0090.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0091.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0092.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0093.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0094.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0095.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0096.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0097.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0098.root',
'file:/hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/MINIAOD_submit_2017_v2-AOD_submit_2017_v2-REDIGI_submit_2017_v2-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-0099.root'

    )
)

process.TFileService = cms.Service("TFileService", 
    fileName = cms.string('Ntuple_signal_aaa.root')
    )

process.load( "PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff" )
process.load( "PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff" )
process.load( "PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff" )

##Re-run ECAL bad calibration filter 
##https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#2017_data
process.load('RecoMET.METFilters.ecalBadCalibFilter_cfi')
baddetEcallist = cms.vuint32(
    [872439604,872422825,872420274,872423218,
    872423215,872416066,872435036,872439336,
    872420273,872436907,872420147,872439731,
    872436657,872420397,872439732,872439339,
    872439603,872422436,872439861,872437051,
    872437052,872420649,872422436,872421950,
    872437185,872422564,872421566,872421695,
    872421955,872421567,872437184,872421951,
    872421694,872437056,872437057,872437313])

process.ecalBadCalibReducedMINIAODFilter = cms.EDFilter(
    "EcalBadCalibFilter",
    EcalRecHitSource = cms.InputTag("reducedEgamma:reducedEERecHits"),
    ecalMinEt        = cms.double(50.),
    baddetEcal       = baddetEcallist, 
    taggingMode      = cms.bool(True),
    debug            = cms.bool(False)
    )

## EE noise mitigation
## https://twiki.cern.ch/twiki/bin/view/CMS/MissingETUncertaintyPrescription#Instructions_for_9_4_X_X_9_or_10
from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
runMetCorAndUncFromMiniAOD (
    process,
    isData          = False, # false for MC
    fixEE2017       = True,
    fixEE2017Params = {'userawPt': True, 'ptThreshold':50.0, 'minEtaThreshold':2.65, 'maxEtaThreshold': 3.139} ,
    postfix         = "ModifiedMET"
    )

## L1 Prefirring
## https://twiki.cern.ch/twiki/bin/viewauth/CMS/L1ECALPrefiringWeightRecipe
from PhysicsTools.PatUtils.l1ECALPrefiringWeightProducer_cfi import l1ECALPrefiringWeightProducer
process.prefiringweight = l1ECALPrefiringWeightProducer.clone(
    DataEra                      = cms.string("2017BtoF"),
    UseJetEMPt                   = cms.bool(False),
    PrefiringRateSystematicUncty = cms.double(0.2),
    SkipWarnings                 = False
    )

# random generator for jet smearing
process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    phoJetNtuplizer  = cms.PSet(
      initialSeed = cms.untracked.uint32(201678),
      engineName = cms.untracked.string('TRandom3')
      )
    )

## https://twiki.cern.ch/twiki/bin/view/CMS/EgammaPostRecoRecipes#Running_on_2017_MiniAOD_V2
from EgammaUser.EgammaPostRecoTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
setupEgammaPostRecoSeq(process,
    runVID = True, #saves CPU time by not needlessly re-running VID, if you want the Fall17V2 IDs, set this to True or remove (default is True)
    era    = '2017-Nov17ReReco'
    ) 

## Apply JEC in AK4
## https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#CorrPatJets
from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
updateJetCollection(
    process,
    jetSource = cms.InputTag('slimmedJets'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']), 'None'),  # Update: Safe to always add 'L2L3Residual' as MC contains dummy L2L3Residual corrections (always set to 1)
    postfix='UpdatedJECAK4'
    )
## AK4Jet Tag: selectedUpdatedPatJetsUpdatedJECAK4

##--| ## Apply JEC in AK8
##--| from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
##--| updateJetCollection(
##--|     process,
##--|     jetSource = cms.InputTag('slimmedJetsAK8'),
##--|     pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
##--|     svSource = cms.InputTag('slimmedSecondaryVertices'),
##--|     rParam = 0.8,
##--|     jetCorrections = ('AK8PFPuppi', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']), 'None'),
##--|     postfix='UpdatedJECAK8',
##--|     printWarning = True
##--|     )
##--| ## AK8Jet Tag: selectedUpdatedPatJetsUpdatedJECAK8
##--| 
##--| ## https://twiki.cern.ch/twiki/bin/viewauth/CMS/DeepAKXTagging#Option_1_Add_DeepAK8_to_slimmed
##--| from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
##--| from RecoBTag.MXNet.pfDeepBoostedJet_cff import _pfDeepBoostedJetTagsAll, _pfDeepBoostedJetTagsProbs, _pfDeepBoostedJetTagsMetaDiscrs, _pfMassDecorrelatedDeepBoostedJetTagsProbs, _pfMassDecorrelatedDeepBoostedJetTagsMetaDiscrs
##--| 
##--| from RecoBTag.MXNet.pfDeepBoostedJet_cff import pfDeepBoostedJetTags, pfMassDecorrelatedDeepBoostedJetTags
##--| from RecoBTag.MXNet.Parameters.V02.pfDeepBoostedJetPreprocessParams_cfi import pfDeepBoostedJetPreprocessParams as pfDeepBoostedJetPreprocessParamsV02
##--| from RecoBTag.MXNet.Parameters.V02.pfMassDecorrelatedDeepBoostedJetPreprocessParams_cfi import pfMassDecorrelatedDeepBoostedJetPreprocessParams as pfMassDecorrelatedDeepBoostedJetPreprocessParamsV02
##--| pfDeepBoostedJetTags.preprocessParams = pfDeepBoostedJetPreprocessParamsV02
##--| pfDeepBoostedJetTags.model_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/full/resnet-symbol.json'
##--| pfDeepBoostedJetTags.param_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/full/resnet-0000.params'
##--| pfMassDecorrelatedDeepBoostedJetTags.preprocessParams = pfMassDecorrelatedDeepBoostedJetPreprocessParamsV02
##--| pfMassDecorrelatedDeepBoostedJetTags.model_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/decorrelated/resnet-symbol.json'
##--| pfMassDecorrelatedDeepBoostedJetTags.param_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/decorrelated/resnet-0000.params'
##--| 
##--| updateJetCollection(
##--|     process,
##--|     jetSource = cms.InputTag('slimmedJetsAK8'),
##--|     pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
##--|     svSource = cms.InputTag('slimmedSecondaryVertices'),
##--|     rParam = 0.8,
##--|     jetCorrections = ('AK8PFPuppi', cms.vstring(['L2Relative', 'L3Absolute', 'L2L3Residual']), 'None'),
##--|     btagDiscriminators = _pfDeepBoostedJetTagsAll,
##--|     postfix='AK8WithDeepTags',
##--|     printWarning = True
##--|     )
##--| ## AK8Jet Tag: selectedUpdatedPatJetsAK8WithDeepTags

from PhysicsTools.PatAlgos.tools.helpers import getPatAlgosToolsTask
task = getPatAlgosToolsTask(process)
process.endpath = cms.EndPath(task)
#//// adding with ref to fsa
process.tauGenJets = cms.EDProducer(
    "TauGenJetProducer",
    GenParticles =  cms.InputTag('prunedGenParticles'),
    includeNeutrinos = cms.bool( False ),
    verbose = cms.untracked.bool( False )
)


process.tauGenJetsSelectorAllHadrons = cms.EDFilter(
    "TauGenJetDecayModeSelector",
    src = cms.InputTag("tauGenJets"),
    select = cms.vstring('oneProng0Pi0',
                         'oneProng1Pi0',
                         'oneProng2Pi0',
                         'oneProngOther',
                         'threeProng0Pi0',
                         'threeProng1Pi0',
                         'threeProngOther',
                         'rare'),
    filter = cms.bool(False)
)

process.tauGenJetsSelectorElectrons = cms.EDFilter(
    "TauGenJetDecayModeSelector",
    src = cms.InputTag("tauGenJets"),
    select = cms.vstring('electron'),
    filter = cms.bool(False)
)

process.tauGenJetsSelectorMuons = cms.EDFilter(
    "TauGenJetDecayModeSelector",
    src = cms.InputTag("tauGenJets"),
    select = cms.vstring('muon'),
    filter = cms.bool(False)
)
process.buildGenTaus = cms.Path(
    process.tauGenJets
    * process.tauGenJetsSelectorAllHadrons
    * process.tauGenJetsSelectorElectrons
    * process.tauGenJetsSelectorMuons
)


### Tau ID
#from phoJetAnalysis.phoJetNtuplizer.runTauIdMVA import *
#na = TauIDEmbedder(process, cms, # pass tour process object
#     debug=True,
#     toKeep = ["2017v2"] # pick the one you need: ["2017v1", "2017v2", "newDM2017v2", "dR0p32017v2", "2016v1", "newDM2016v1"]
#    )
#na.runTauID()
##    Tau ID DNN based 
updatedTauName = "slimmedTausNewID" #name of pat::Tau collection with new tau-Ids
import RecoTauTag.RecoTau.tools.runTauIdMVA as tauIdConfig
tauIdEmbedder = tauIdConfig.TauIDEmbedder(process, cms, debug = False,
                    updatedTauName = updatedTauName,
                    toKeep = [ "2017v2", "deepTau2017v2p1" ])
tauIdEmbedder.runTauID()

### Analyzer Related
process.load("phoJetAnalysis.phoJetNtuplizer.phoJetNtuplizer_cfi")
process.phoJetNtuplizer.debug       = cms.bool(False);
process.phoJetNtuplizer.is_Data     = cms.bool(False); # True for Data
process.phoJetNtuplizer.runGenInfo  = cms.bool(True);  # True for MC
process.phoJetNtuplizer.runak8Jets  = cms.bool(False);
process.phoJetNtuplizer.runJetWidthCalculator = cms.bool(True); # needed for monoZprime Analysis [Valid only if runJets is True]
process.phoJetNtuplizer.jetsAK4Token = cms.InputTag("selectedUpdatedPatJetsUpdatedJECAK4")
##process.phoJetNtuplizer.jetsAK8Token = cms.InputTag("selectedUpdatedPatJetsUpdatedJECAK8")
##process.phoJetNtuplizer.jetsAK8TagToken = cms.InputTag("selectedUpdatedPatJetsAK8WithDeepTags")
process.phoJetNtuplizer.pfmetToken   = cms.InputTag("slimmedMETsModifiedMET")

process.p = cms.Path(
    process.ecalBadCalibReducedMINIAODFilter *
    process.fullPatMetSequenceModifiedMET *
    process.egammaPostRecoSeq *
    process.tauGenJets *
    process.prefiringweight *
    process.rerunMvaIsolationSequence *
    getattr(process,updatedTauName) *
    process.phoJetNtuplizer
    )

#print process.dumpPython()