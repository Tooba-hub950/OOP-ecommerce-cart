# ===== Starter Template: E-Commerce Cart System =====
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict
class PricingStrategy(ABC):

  @abstractmethod
  def calculate(self, subtotal: float) -> float:
   ...
   
class NoDiscount(PricingStrategy):
   def calculate(self, subtotal: float) -> float:
    # TODO: return subtotal unchanged
    raise NotImplementedError

class PercentageDiscount(PricingStrategy):
  def __init__(self, percent: float):
   # TODO: validate 0..100
    self.percent = percent
  def calculate(self, subtotal: float) -> float:
   # TODO: apply percent discount
   raise NotImplementedError

@dataclass(frozen=True)
class Product:
  sku : str
  name: str
  price: float
@dataclass
class CartItem:
  product: Product
  qty: int = 1
  def subtotal(self) -> float:
   # TODO: price * qty
   raise NotImplementedError

class ShoppingCart:
 def __init__(self, strategy: PricingStrategy):
  self._items: Dict[str, CartItem] = {}
  self.strategy = strategy
  
 def add(self, product: Product, qty: int = 1) -> None:
  # TODO: validate qty >= 1, add or increase quantity
  raise NotImplementedError

 def remove(self, sku: str) -> None:
  # TODO: remove item if exists else raise KeyError
  raise NotImplementedError

 def subtotal(self) -> float:
  # TODO: sum of CartItem.subtotal()
  raise NotImplementedError

 def total(self) -> float:
 # TODO: apply strategy.calculate(subtotal)
  raise NotImplementedError