score.py is now a self-contained script for prediction. To run it, use:
python score.py green 2022 2 682824de8ca349bc908f40268a891c34

Create prefect project: prefect init

Deployment creation uses script's main flow: 
prefect deploy score.py:ride_duration_prediction -n score_deployment -p mlops_module4_process

For starting worker that catches deployment's runs (in separate terminal):
prefect worker start -p 'mlops_module4_process'

Quick run of this deployment:
prefect deployment run 'ride-duration-prediction/score_deployment'