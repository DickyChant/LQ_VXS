import os

dirnames = ['check_vlq_noQED',
 'check_vlq_QEDnoZP',
 'check_vlq_QED',

 'check_vlq_noQED_1TeV',
 'check_vlq_QEDnoZP_1TeV',

 'check_vlq_QED_1TeV',]
 
for irun in [1,2,3,4,5]:
    for dirname in dirnames:
        os.system(f"cp {dirname}/Events/run_0{irun}/unweighted_events.lhe.gz LHEs/{dirname}_run{irun}.lhe.gz")
        
for irun in [1,2,3,4,5]:
    for dirname in dirnames:
        os.system(f"rm LHEs/{dirname}_run{irun}.lhe")
        os.system(f"gzip -d LHEs/{dirname}_run{irun}.lhe.gz")

for irun in [1,2,3,4,5]:
    for dirname in dirnames:
        os.system(f"python3 LHEConverter.py -i LHEs/{dirname}_run{irun}.lhe -o rootfiles/{dirname}_run{irun}.root")