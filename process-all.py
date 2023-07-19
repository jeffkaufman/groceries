#!/usr/bin/env python3

import glob
from collections import defaultdict

parents = {
  "Semi Sweet Chocolate Chips": "Chocolate",
  "Prune Plums": "Plums",
  "4 Fold Bourbon Vanilla Paste": "Vanilla",
  "Frozen Ready To Bake Large Chocolate Croissant": "Chocolate Croissants",
  "Medallion All-Purpose Flour": "Flour",
  "Cara Cara Oranges": "Oranges",
  "Extra Firm Tofu": "Tofu",
  "Chocolate": "Dessert",
  "Chocolate Croissants": "Dessert",
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
  "Beans": "Protein",
  "Meat": "Protein",
  "Eggs": "Protein",
  "Dairy": "Protein",
  "Fruit": "Produce",
  "Vegetables": "Produce",
  "Condiments": "Cooking",
  "Baking": "Starch",
  "Cleaning": "Other",
  "Snacks": "Starch",
  "Cooking": "Root",
  "Dessert": "Root",
  "Other": "Root",
  "Produce": "Root",
  "Protein": "Root",
  "Snacks": "Root",
  "Starch": "Root",
}

costs = defaultdict(float)

with open("Instacart History - Sheet1.tsv") as inf:
  for line in inf:
    _, full_name, short_name, category = line.strip().split("\t")
    short_name = short_name.replace(
      "Vanilla Extract", "Vanilla").replace("Frozen ", "").replace(
        "Banana", "Bananas")
    if full_name != short_name:
      parents[full_name] = short_name
    if short_name != category:
      if category != parents.get(short_name, category):
        raise Exception("%s under %s and %s" % (
          short_name, category, parents[short_name]))
      parents[short_name] = category

for child, parent in {
    "Chicken Breast": "Chicken",
    "Chicken Legs": "Chicken",
    "Chicken Nuggets": "Chicken",
    "Chicken Thighs": "Chicken",
    "Chicken": "Meat",
    "Beef": "Meat",
    "Ground Beef": "Beef",
    "Meatballs": "Beef",
    "Hot Dogs": "Beef",
    "Pork": "Meat",
    "Italian Sausage": "Pork",
    "Pork Ribs": "Pork",
    "Pepperoni": "Pork",
    "Short Pasta": "Pasta",
    "Long Pasta": "Pasta",

    "Campanelle": "Short Pasta",
    "Elbows": "Short Pasta",
    "Farfalle": "Short Pasta",
    "Gemelli": "Short Pasta",
    "Radiatore": "Short Pasta",
    "Rigatoni": "Short Pasta",
    "Rotini": "Short Pasta",
    "Shells": "Short Pasta",

    "Rice Noodles": "Noncentral Pasta",
    "Egg Noodles": "Noncentral Pasta",
    "Lasagna Noodles": "Noncentral Pasta",
    "Ramen Noodles": "Noncentral Pasta",
    "Cauliflower Gnocchi": "Noncentral Pasta",
    "Gnocchi": "Noncentral Pasta",

    "Angel Hair": "Long Pasta",
    "Noncentral Pasta": "Pasta",
    "Linguine": "Long Pasta",
    "Spaghetti": "Long Pasta",
    "Thin Spaghetti": "Long Pasta",

    "Cheese Ravoili": "Prepared",

    "Sweeteners": "Baking",
    "Sugar": "Sweeteners",
    "Light Corn Syrup": "Sweeteners",
    "Molasses": "Sweeteners",
    "Stevia": "Sweeteners",
    "Powdered Sugar": "Sweeteners",
    "Brown Sugar": "Sweeteners",

    "Crackers": "Snacks",
    "Cheezits": "Crackers",
    "Graham Crackers": "Crackers",
    "Ritz Crackers": "Crackers",
    "Triscuits": "Crackers",
    "Water Crackers": "Crackers",

    "Chips": "Snacks",
    "Pita Chips": "Chips",
    "Tortilla Chips": "Chips",

    "Fake Cheese": "Fake Dairy",

    "Citrus": "Fruit",
    "Stone Fruit": "Fruit",
    "Berries": "Fruit",
    "Tropical Fruit": "Fruit",

    'Raspberries': 'Berries',
    'Clementines': 'Citrus',
    'Blueberries': 'Berries',
    'Plums': 'Stone Fruit',
    'Oranges': 'Citrus',
    'Mangoes': 'Tropical Fruit',
    'Peaches': 'Stone Fruit',
    'Limes': 'Citrus',
    'Cranberries': 'Berries',
    'Pineapple': 'Tropical Fruit',
    'Grapefruit': 'Citrus',
    'Lemons': 'Citrus',
    'Strawberries': 'Berries',
    'Nectarines': 'Stone Fruit',
    'Prunes': 'Stone Fruit',
    'Bananas': 'Tropical Fruit',

    'Tomatoes': 'Nightshades',
    'Peppers': 'Nightshades',
    'Baby Spinach': 'Leaves',
    'Spinach': 'Leaves',
    'Parsley': 'Leaves',
    'Swiss Chard': 'Leaves',
    'Spring Mix': 'Leaves',
    'Salad': 'Leaves',
    'Eggplant': 'Nightshades',
    'Kale': 'Leaves',
    'Hot Peppers': 'Nightshades',
    'Spinach and Kale': 'Leaves',

    'Nightshades': 'Vegetables',
    'Leaves': 'Vegetables',

    'Nut Butters': 'Condiments',
    'Spicy': 'Condiments',
    'Peanut Butter': 'Nut Butters',
    'Salsa': 'Spicy',
    'Nutella': 'Nut Butters',
    'Hummus': 'Nut Butters',
    'Almond Butter': 'Nut Butters',
    'Chili Oil': 'Spicy',
    'Salsa Verde': 'Spicy',
    'Enchilada Sauce': 'Spicy',
    'Curry Paste': 'Spicy',
    'Chili Crisp': 'Spicy',
    'Hot Sauce': 'Spicy',
    'Chili Sauce': 'Spicy',

}.items():
  parents[child] = parent

people_months = (
  12 + # Jeff
  12 + # Julia
  12 + # Lily
  12 + # Anna
#  12 + # Nora
  12 + # David
  12 + # Al
  9 + # Weiwei
  3 + # Ruthie
  3 # Andrew
)

raw_cost = 0
instacart_cost = 0

# taxes, fees, tips
instacart_overhead = 11524.69/8977.12

roots = set()
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
        total_cost = float(total_cost)
        total_cost *= instacart_overhead
        instacart_cost += float(total_cost)
      elif fname.startswith("Baldor"):
        date = fname.split(" ")[-1].replace(".tsv", "")
        if line.startswith("PRODUCT"):
          continue
        product_id, item, pice_and_size, quantity_shipped,\
          total_cost = line.split("\t")
        total_cost = total_cost.replace("$", "")
        total_cost = float(total_cost)

      raw_cost += total_cost

      monthly_cost = total_cost / people_months

      node = item
      while node in parents:
        node = parents[node]
        costs[node] += monthly_cost
      roots.add(node)

if len(roots) > 1:
  print(roots)
assert len(roots) == 1

def print_tree(node, depth=0):
  if costs[node]:
    print("%s%s $%.2f" % (
      "  "*depth, node, costs[node]))

  costs_children = []
  for child, parent in parents.items():
    if parent == node:
      costs_children.append((costs[child], child))
  for _, child in sorted(costs_children, reverse=True):
    print_tree(child, depth+1)

def print_html_tree(node, depth=0):
  if node != "Root":
    print("%s<li>%s $%.2f" % (
      "  "*depth, node, costs[node]))

  costs_children = []
  for child, parent in parents.items():
    if parent == node and costs[child]:
      costs_children.append((costs[child], child))

  if costs_children:
    print("%s<ul>" % ("  "*depth))

  for _, child in sorted(costs_children, reverse=True):
    print_html_tree(child, depth+1)

  if costs_children:
    print("%s</ul>" % ("  "*depth))

if False:
  print_tree("Root")
else:
  print_html_tree("Root")

#print("%.2f for %s people-months" % (raw_cost, people_months))
#print("%.2f on instacart" % instacart_cost)
