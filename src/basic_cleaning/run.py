#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import argparse
import logging
import wandb
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    artifact_local_path = run.use_artifact(args.input_artifact).file()

    logger.info("INFO - Download Artifact: %s", args.input_artifact)
    data = pd.read_csv(artifact_local_path)

    min_price = args.min_price
    max_price = args.max_price

    idx = data["price"].between(min_price, max_price)
    df = df[idx].copy()

    idx = df['longitude'].between(-74.25, -73.50) & df['latitude'].between(40.5, 41.2)
    df = df[idx].copy()

    # Save dataframe
    output_artifact = args.output_artifact
    output_type = args.output_type,
    description=args.output_descriptio

    logger.info(f'INFO - Saving Dataframe: {output_artifact}')
    df.to_csv('clean_sample.csv', index=False)


    artifact = wandb.Artifact(
        output_artifact,
        type=output_type,
        description=description
    )

    artifact.add_file(local_path='clean_sample.csv')
    run.log_artifact(artifact)

    artifact.wait()
    logger.info("INFO - Artifact uploaded.")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--input_artifact", 
        type=str,
        help="Name input artifact",
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help="Name output artifact",
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help="Type output artifact",
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help="Describe output artifact.",
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help="Set minimum price limit",
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help="Set maximum price limit",
        required=True
    )


    args = parser.parse_args()

    go(args)
