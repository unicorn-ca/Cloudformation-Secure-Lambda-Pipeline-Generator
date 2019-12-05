# Unicorn Pipeline

## Requirements
The Unicorn Pipeline requires:
- 3x AWS accounts (Master, Dev, Prod)
- [aws-cli](https://aws.amazon.com/cli/)
- Python3, virtualenv
- Ruby (version >= 2.3)

## Configuration
**[Help Wanted!](https://github.com/unicorn-ca/Unicorn-Pipeline/issues/1)**

## Installation

Install and run wizard by adding the `-w` flag:

```shell
curl https://raw.githubusercontent.com/unicorn-ca/Unicorn-Pipeline/master/build > tmp.sh; sh tmp.sh -w
```

You should expect the launch wizard opening on your browser. If this doesn't work for you, try doing a headless install.

### Headless Install

Install the pipeline with

```shell
curl https://raw.githubusercontent.com/unicorn-ca/Unicorn-Pipeline/master/build > tmp.sh; sh tmp.sh
``` 

## Contribution

Please read our [contribution guidelines](https://github.com/unicorn-ca/Unicorn-docs/blob/master/CONTRIBUTING.md) before creating an issue or pull request!
