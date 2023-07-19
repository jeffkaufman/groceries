#!/usr/bin/env python3

import glob
from collections import defaultdict

short_names = {
  "Semi Sweet Chocolate Chips": "Chocolate",
  "Basil": "Basil",
  "Prune Plums": "Plums",
  "4 Fold Bourbon Vanilla Paste": "Vanilla",
  "Frozen Ready To Bake Large Chocolate Croissant": "Chocolate Croissants",
  "Medallion All-Purpose Flour": "Flour",
  "Cara Cara Oranges": "Oranges",
  "Extra Firm Tofu": "Tofu",
}

categories = {
  "Chocolate": "Dessert",
  "Chocolate Croissants": "Dessert",
}
with open("Instacart History - Sheet1.tsv") as inf:
  for line in inf:
    _, full_name, short_name, category = line.strip().split("\t")
    short_names[full_name] = short_name

    if category != categories.get(short_name, category):
      raise Exception("%s under %s and %s" % (
        short_name, category, categories[short_name]))
    categories[short_name] = category
    
super_categories = {}
for category in categories.values():
  super_categories[category] = {
    "Fake Meat": "Meat",
    "Cheese": "Dairy",
    "Fake Cheese": "Dairy",
    "Fake Dairy": "Dairy",
    "Pasta": "Starch",
    "Bread": "Starch",
    "Tortillas": "Starch",
    "Cereal": "Starch",
    "Medical": "Other",
    "Alcohol": "Other",
    "Beverages": "Other",
    "Spices": "Cooking",
    "Prepared": "Cooking",
  }.get(category, category)
    
category_costs = defaultdict(float)
super_category_costs = defaultdict(float)
    
for fname in glob.glob("*.tsv"):
  if fname.startswith("Instacart"):
    continue
  
  with open(fname) as inf:
    for line in inf:
      line = line.strip()
      if not line: continue

      if fname.endswith(".txt.tsv"):
        date = fname.replace(".txt.tsv", "")
        item, unit_cost, size, quantity, total_cost = line.split("\t")
      elif fname.startswith("Baldor"):
        date = fname.split(" ")[-1].replace(".tsv", "")
        if line.startswith("PRODUCT"):
          continue
        product_id, item, pice_and_size, quantity_shipped,\
          total_cost = line.split("\t")
        total_cost = total_cost.replace("$", "")
        
      short_name = short_names[item]
      category = categories[short_name]
      category_costs[category] += float(total_cost)
      super_category = super_categories[category]
      super_category_costs[super_category] += float(total_cost)

for cost, category in sorted(
    (x, y) for (y, x) in category_costs.items()):
  print("%.2f\t%s" % (cost, category))

print()

for cost, super_category in sorted(
    (x, y) for (y, x) in super_category_costs.items()):
  print("%.2f\t%s" % (cost, super_category))

