In this folder, there are all the configs for running different models with different datasets.

There should be each config file for each model family which filename is model family name.

Generally, config file for the model family includes:

```yaml
# project name
name: efficientnet-b0
defaults:
  - dm: cifar10 # for LightningDataModule

# for logger and checkpoint
logger: true
ckpt: true

# .test() or not
test: true

# for LightningModule
lm:
  optimizer: Adam
  learning_rate: 0.001
  weight_decay: 0.05
  num_classes: 10

# pl.Trainer configs
pl:
  max_epochs: 10
  gpus: -1
  fast_dev_run: false
  overfit_batches: 0
```
