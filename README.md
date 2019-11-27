# Unicorn Pipeline
## Background
- Essentially, the wizard will have two stages - a config stage and a deploy stage
- Wizard will be hosted locally - user clones the [pipeline repo](https://github.com/unicorn-ca/Unicorn-Pipeline) and runs some command to open Unicorn-Wiz in their browser
- Wizard, Herd and cfn-checker are linked to the Pipline repo via submodules
- By hosting the wizard locally, we don't have to tie the wizard to AWS (via an S3 or otherwise)
- We will also be able to access aws credentials, allowing us to deploy the pipeline with the same wizard instead of a shell script which the user has to download and run
- Assumptions:
    - user has the `aws-cli` set up
    - user has 3x AWS accounts (for dev, prod and master)

### Config Stage
- Wizard will configure the pipeline to the user's wishes
- Creates cfn templates for pipeline stages: `predeploy`, `child` and `stack`
- Creates Herd deployment files: `herd.predeploy` and `herd.deploy`
- Files are saved on the machine in the pipeline folder they cloned
- Creates a shell script that will deploy the pipeline
- User can stop here and deploy manually if they want to

### Deploy Stage
- cfn-checker validates the generated cfn templates
- Deploy the pipeline via Herd and aws-cli

## Requirements
The Unicorn Pipeline requires:
- 3x AWS accounts (Master, Dev, Prod)
- [aws-cli](https://aws.amazon.com/cli/)
- Python3, virtualenv
- Ruby (version >= 2.3)

## Configuration
**//TODO**

## Installation
Install pipeline with `$ curl https://raw.githubusercontent.com/unicorn-ca/Unicorn-Pipeline/build/build > tmp.sh; sh tmp.sh`.
Or install and run wizard by adding the `-w` flag `$ curl https://raw.githubusercontent.com/unicorn-ca/Unicorn-Pipeline/build/build > tmp.sh; sh tmp.sh -w`

## Usage
**//TODO**
