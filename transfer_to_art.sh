# A script I use to compile the simulation and transfer it to the high performance computing facility @ USyd. 
# I'm leaving it here in case anyone else finds it useful. 

./compileSimulationJar.sh
rsync -rvx src lib j3dlibs art:/project/microanal/swarm_metric_paper/motilisim/.
#rsync -rvx results/test-cluster art:/project/microanal/swarm_metric_paper/motilisim/results/.
