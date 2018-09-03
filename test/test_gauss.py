import os, sys
import easyvvuq as uq

my_campaign = uq.Campaign(state_fname="test_input/test_gauss.json")
uq.uqp.basicUQP(my_campaign)
uq.populate_runs_dir(my_campaign)
uq.apply_for_each_run(my_campaign, uq.execute_local)
uq.apply_for_each_run(my_campaign, uq.uqp.statsUQP(reader=uq.reader.csvReader('output.csv', 1)))
my_campaign.print()
my_campaign.save_state("out_gauss.json")
