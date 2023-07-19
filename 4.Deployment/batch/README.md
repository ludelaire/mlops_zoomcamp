score.py is now a self-contained script for prediction. To run it, use:
python score.py green 2022 2 682824de8ca349bc908f40268a891c34

Create prefect project: prefect init

Deployment creation uses script's main flow: 
prefect deploy score.py:ride_duration_prediction -n score_deployment -p mlops_module4_process

For starting worker that catches deployment's runs (in separate terminal):
prefect worker start -p 'mlops_module4_process'

Quick run of this deployment:
prefect deployment run 'ride-duration-prediction/score_deployment'

Remember that prefect tends to have this "No such file or directory" issue if you do not specify absolute path to script file. And push to github or whatever remote location before running any deployment.

prefect.orion was renamed to prefect.server, thus the change in score_deploy.py. See [these release notes](https://github.com/PrefectHQ/prefect/blob/main/RELEASE-NOTES.md#release-281)

However, just remembered [this](https://discourse.prefect.io/t/work-queue-automatically-goes-unhealthy/2072/2), which is the reason why I actually switched to agent pools instead of process (worker) pools