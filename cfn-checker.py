import subprocess
import os
import argparse

# Make stdout in pretty colours
class bcolours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Check if a cfn template is valid via cfn_nag
def check_template(directory, log):
    # Read the directory
    directory = os.fsencode(directory)

    for file in os.listdir(directory):
        # Read the current file
        filename = os.fsdecode(file)

        # Check if the file is a cfn template
        if filename.endswith("template.yaml") or filename.endswith("templates.json"):
            path = f"{directory.decode('utf-8')}/{filename}"

            if log is None: # Run cfn_nag_scan and output it to stdout
                subprocess.run(["cfn_nag_scan", "--input-path", path])
            else: # Run cfn_nag_scan and output it into logs/
                print(bcolours.HEADER + path + bcolours.ENDC, end='\t')
                output = f"{log}/{directory.decode('utf-8')}.{filename}.log"
                subprocess.run(["cfn_nag_scan", "--input-path", path], stdout=open(output, 'w'))
                print_output(output)

# Print the warnings/failures in pretty colours
def print_output(logfile):
    # Grep for the number of failures
    failures_proc = subprocess.run(["grep", "Failures count:", logfile], stdout=subprocess.PIPE)
    failures = failures_proc.stdout.decode('utf-8').strip('\n')
    if failures.endswith('0'):
        print(bcolours.OKGREEN + failures + bcolours.ENDC, end='\t')
    else:
        print(bcolours.FAIL + failures + bcolours.ENDC, end='\t')

    # Grep for the number of warnings
    warnings_proc = subprocess.run(["grep", "Warnings count:", logfile], stdout=subprocess.PIPE)
    warnings = warnings_proc.stdout.decode('utf-8').strip('\n')
    if warnings.endswith('0'):
        print(bcolours.OKGREEN + warnings + bcolours.ENDC)
    else:
        print(bcolours.WARNING + warnings + bcolours.ENDC)

# Get the directories with the cfn templates
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--logdir", type=str, help="directory to output logs to")
parser.add_argument("-d", "--dir", type=str, required=True, nargs='+', help="input directories")
args = parser.parse_args()

# Check if the directory exists
if args.logdir is not None and os.path.isdir(args.logdir) is False:
    print(bcolours.FAIL + "Directory does not exist!" + bcolours.ENDC)
    parser.print_usage()
    exit(1)

# Check templates
print("------------------------------------------------------------")
print(bcolours.OKBLUE + "cfn-checker starting" + bcolours.ENDC)
print("------------------------------------------------------------")
for directory in args.dir:
    check_template(directory, args.logdir)
print("------------------------------------------------------------")
print(bcolours.OKBLUE + "cfn-checker complete" + bcolours.ENDC)
print("------------------------------------------------------------")