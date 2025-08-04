#!/usr/bin/env python
import argparse
import logging
import pathlib
import wandb
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):
    logger.info("Creating run in project exercise_1")
    run = wandb.init(project="exercise_1", job_type="use_file")

    logger.info("Getting artifact")
    artifact = run.use_artifact(args.artifact_name)

    # Specify an absolute path for the artifacts directory
    artifacts_dir = os.path.join(os.getcwd(), "artifacts")

    # Download the artifact
    artifact_path = artifact.get_path("zen.txt").download(root="artifacts")

    logger.info("Artifact content:")
    with open(artifact_path, "r") as fp:
        content = fp.read()

    print(content)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="Use an artifact from W&B", fromfile_prefix_chars="@"
    )

    parser.add_argument(
        "--artifact_name", type=str, help="Name and version of W&B artifact", required=True
    )

    args = parser.parse_args()

    go(args)
