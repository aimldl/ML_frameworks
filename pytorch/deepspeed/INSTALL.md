

# How to Install DeepSpeed

## Two options to use DeepSpeed

This page is a misnomer in a sense that you don't actually install DeepSpeed like other libraries. To use DeepSpeed, two options are suggested at [deepspeed.ai](https://www.deepspeed.ai/) > [Getting Started](https://www.deepspeed.ai/getting-started/) > [Installation](https://www.deepspeed.ai/getting-started/#installation).

### Option 1. Docker image for DeepSpeed

You can form your custom environment. Using the official docker image is recommended.

```bash
$ docker pull deepspeed/deepspeed:latest
```

The docker image come with DeepSpeed pre-installed and all the necessary dependences.

### Option 2. Azure VMs (Virtual Machines)

Use Microsoft Azure's compute service without installing DeepSpeed. Azure supports DeepSpeed off the shelf! Refer to [Getting Started with DeepSpeed on Azure](https://www.deepspeed.ai/tutorials/azure/)

### How to configure the DeepSpeed Environment with Docker image on AWS

Todo

## Next

* [Getting Started with DeepSpeed](QUICK_START.md)

