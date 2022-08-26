import os

dataset = {

 'TTTo2L2Nu_TuneCP5' : '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
  
}
#
#if __name__ == '__main__':
from CRABAPI.RawCommand import crabCommand

def submit(config):
  res = crabCommand('submit', config = config)

from CRABClient.UserUtilities import config
from multiprocessing import Process

config = config()
name = 'MC2017_12Apr2018_monoHiggs_09Jun2020'
config.General.workArea = 'crab_'+name
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.inputFiles = ['Fall17_17Nov2017_V32_102X_MC.db']
config.JobType.allowUndistributedCMSSW = True

config.section_('Data') 
config.Data.publication = False
config.Data.inputDBS = 'global'
config.Data.splitting =  'FileBased'#'EventAwareLumiBased' #'FileBased'

config.Site.storageSite = 'T2_US_Wisconsin'
#config.Site.whitelist = ["T2_US_Wisconsin"]
#config.Site.blacklist = ['T2_CH_CERN']
#listOfSamples = ['DY4JetsToLL_M-50_TuneCP5']
#listOfSamples =[ 'TTTo2L2Nu_TuneCP5', 'TTToHadronic_TuneCP5', 'TTToSemiLeptonic_TuneCP5', 'WJetsToLNu_TuneCP5', 'W1JetsToLNu_TuneCP5', 'W2JetsToLNu_TuneCP5', 'W3JetsToLNu_TuneCP5', 'W4JetsToLNu_TuneCP5', 'DYJetsToLL_M-50_TuneCP5_v1', 'DYJetsToLL_M-50_TuneCP5_ext1_v1', 'DYJetsToLL_M-10to50_TuneCP5', 'DY1JetsToLL_M-50_TuneCP5', 'DY2JetsToLL_M-50_TuneCP5', 'DY3JetsToLL_M-50_TuneCP5_v1', 'DY3JetsToLL_M-50_TuneCP5_ext1', 'DY4JetsToLL_M-50_TuneCP5', 'WW_TuneCP5', 'WZ_TuneCP5', 'ZZ_TuneCP5', 'ST_t-channel_top_4f_inclusiveDecays_TuneCP5', 'ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5', 'ST_tW_top_5f_inclusiveDecays_TuneCP5', 'ST_tW_antitop_5f_inclusiveDecays_TuneCP5', 'EWKZ2Jets_ZToLL_M-50_TuneCP5', 'EWKZ2Jets_ZToNuNu_TuneCP5', 'EWKWPlus2Jets_WToLNu_M-50_TuneCP5', 'EWKWMinus2Jets_WToLNu_M-50_TuneCP5', 'GluGluHToTauTau_M125', 'VBFHToTauTau_M125', 'WplusHToTauTau_M125', 'WminusHToTauTau_M125', 'ZHToTauTau_M125', 'ttHToTauTau_M125_TuneCP5', 'ggZH_HToTauTau_ZToLL_M125', 'ggZH_HToTauTau_ZToNuNu_M125', 'ZJetsToNuNu_HT-100To200', 'ZJetsToNuNu_HT-200To400', 'ZJetsToNuNu_HT-400To600', 'ZJetsToNuNu_HT-600To800', 'ZJetsToNuNu_HT-800To1200', 'ZJetsToNuNu_HT-1200To2500', 'ZJetsToNuNu_HT-2500ToInf', 'WWToLNuQQ_NNPDF31_TuneCP5', 'VVTo2L2Nu', 'WZTo3LNu_TuneCP5', 'WWTo1L1Nu2Q', 'ZZTo4L_TuneCP5', 'ZZTo2L2Q', 'GluGluHToWWTo2L2Nu_M125', 'VBFHToWWTo2L2Nu_M125', 'WWW_4F_TuneCP5', 'WWZ_4F_TuneCP5', 'WZZ_TuneCP5', 'ZZZ_TuneCP5' ] 
listOfSamples =[ 'DY4JetsToLL_M-50_TuneCP5']
for sample in listOfSamples:
  os.popen('cp run_102X_mc2017.py run_102X_mc2017_'+sample+'.py')
  with open('run_102X_mc2017_'+sample+'.py') as oldFile:
    newText = oldFile.read().replace('Ntuple_mc.root', 'Ntuple_mc.root')
  with open('run_102X_mc2017_'+sample+'.py', 'w') as newFile:
    newFile.write(newText) 

  config.General.requestName = 'job_'+sample
  
  config.JobType.psetName = 'run_102X_mc2017_'+sample+'.py'
  config.JobType.outputFiles = ['Ntuple_mc.root']
  
  config.Data.inputDataset   = dataset[sample]
  config.Data.unitsPerJob = 1 #10000
  config.Data.totalUnits = -1
  config.Data.outLFNDirBase = '/store/user/jmadhusu/'+name
  #submit(config)
  p = Process(target=submit, args=(config,))
  p.start()
  p.join()
