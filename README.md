# Pipeline

## Installation
### Ruby
If you haven't installed Ruby, you can do so with [rvm](https://rvm.io/)
Install bundler:
```
$ gem install bundle
```

Install the ruby dependencies (cfn_nag)
```
$ bundle install
```

## Deploying the pipeline
The pipeline needs to be deployed into two steps. This will be automated using herd.

The first step is to deploy a staging bucket into the tooling account. This will hold the templates
and other resources for the deployment of the main toolchain.
```sh
$ python herd.py herd.predeploy.yaml
```

Next the pipeline can be deployed in full.
```sh
$ python herd.py herd.deploy.yaml
```
