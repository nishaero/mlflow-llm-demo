import mlflow

EXPERIMENT_NAME = "agent-experiments"

def start_run(tags=None):
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment(EXPERIMENT_NAME)
    return mlflow.start_run(tags=tags)
