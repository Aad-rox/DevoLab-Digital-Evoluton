import subprocess
import os

# Define the path for the log directory
log_dir = 'logsTruncation'

# Create the log directory if it doesn't exist
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

for mu in [0.001, 0.01, 0.1]:
    for ps in [10, 100, 1000]:
        for ts in range(1,101):
            slurm_script = f"""#!/bin/bash -login
#SBATCH --constraint="[intel14|intel16|intel18]"
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=03:55:00
#SBATCH --mem=2G
#SBATCH --mail-type=FAIL
#SBATCH --output=logs/job_{mu}_{ps}_{ts}.out
#SBATCH --job-name=job_{mu}_{ps}_{ts}

python3 data_collection_truncation.py --mutation_rate_ {mu} --population_size_ {ps} --truncation_rate_ {ts}; """

            script_name = f"submit_job_{mu}_{ps}_{ts}.slurm"
            with open(script_name, 'w') as file:
                file.write(slurm_script)

            # Submit the job
            subprocess.run(["sbatch", script_name])

            # Delete the script file after submission
            os.remove(script_name)

