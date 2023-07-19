score.py is now a self-contained script for prediction. To run it, use:
python score.py green 2022 2 682824de8ca349bc908f40268a891c34

Create prefect project: prefect init

Deployment creation uses script's main flow (agent pool should exist already, you can create it through the UI): 
prefect deploy ABSOLUTE/PATH/TO/FILE/score.py:ride_duration_prediction -n score_deployment -p mlops_module4_process

For starting agent that catches deployment's runs (in separate terminal):
prefect agent start -p mlops_module4_process

Run the deployment from the UI to enter parameters straightforward. Remember that you don't have to start a server if you've previously logged into prefect cloud from terminal.

Remember that prefect tends to have this "No such file or directory" issue if you do not specify absolute path to script file. And push to github or whatever remote location before running any deployment.

prefect.orion was renamed to prefect.server, hence the change in score_deploy.py. See [these release notes](https://github.com/PrefectHQ/prefect/blob/main/RELEASE-NOTES.md#release-281)

However, just remembered [this](https://discourse.prefect.io/t/work-queue-automatically-goes-unhealthy/2072/2), which is the reason why I actually switched to agent pools instead of process (worker) pools on module 3, which leaves some parts of video 4.6.7 obsolete(?). UPDATE: using the absolute path to score.py worked with a process (worker) pool, as suggested in [this doc](https://docs.prefect.io/2.10.21/concepts/deployments/)

Don't forget to set run date according to data's (parquet file) month and year. Prefect UI says it's optional, but run will fail if you don't select the proper parameters.