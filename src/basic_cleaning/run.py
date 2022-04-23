#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import argparse
import logging
import wandb


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    ######################
    # YOUR CODE HERE     #
    ######################


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
