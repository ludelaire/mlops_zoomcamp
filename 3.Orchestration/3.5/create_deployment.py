# This creates a prefect deployment without the need for specifying absolute route to orchestration file

from orchestrate_s3 import main_flow_s3  # Import .py where your main flow is

from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule

deployment = Deployment.build_from_flow(
    flow=main_flow_s3,
    name="ride_duration_prediction",
    parameters={
        "taxi_type": "green",
        #"run_id": "a4b217a84e3a44ad870271b75331eb6c",
    },
    schedule=CronSchedule(cron="25 15 11 7 2"),
    work_pool_name="mlops_module3"
)

deployment.apply()