"""
LightningDataModule for CIFAR10
"""
import os
from typing import Optional

from omegaconf import DictConfig, OmegaConf
from pytorch_lightning import LightningDataModule
from torch.utils.data import DataLoader, random_split
from torchvision import transforms as T
from torchvision.datasets import CIFAR10


class CIFAR10DataModule(LightningDataModule):
    """DataModule for CIFAR10."""

    def __init__(
        self,
        train_dataloader_conf: Optional[DictConfig] = None,
        val_dataloader_conf: Optional[DictConfig] = None,
    ):
        super().__init__()
        self.train_dataloader_conf = train_dataloader_conf or OmegaConf.create()
        self.val_dataloader_conf = val_dataloader_conf or OmegaConf.create()

    def setup(self, stage: Optional[str] = None):
        train = CIFAR10(
            os.getcwd(),
            train=True,
            download=True,
            transform=T.Compose(
                [
                    T.Resize(size=(224, 224)),
                    T.ToTensor(),
                    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                ]
            ),
        )
        test = CIFAR10(
            os.getcwd(),
            train=False,
            download=True,
            transform=T.Compose(
                [
                    T.Resize(size=(224, 224)),
                    T.ToTensor(),
                    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                ]
            ),
        )
        train, val = random_split(train, [40000, 10000])
        self.train_dataset = train
        self.val_dataset = val
        self.test_dataset = test

    def train_dataloader(self):
        return DataLoader(self.train_dataset, **self.train_dataloader_conf)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, **self.val_dataloader_conf)

    def test_dataloader(self):
        return DataLoader(self.test_dataset, **self.val_dataloader_conf)
