#!/usr/bin/env python3

import re
import sys

for fname in sys.argv[1:]:
  records = []
  record = {}
  def save_item():
    if record:
      records.append(record.copy())
      record.clear()
  
  state = "initial"
  n_items = "0"
  n_replacements = "0"
  with open(fname) as inf:
    for line in inf:
      line = line.strip()
      if not line: continue

      print(state, repr(line))
      
      if state == "initial":
          n_items, = re.match("^(\d+) items found$", line).groups()
          state = "item"
      elif state == "item":
        if line == "Original price:":
          state = "ignore original price"
        elif re.match("^\d+ replacements", line):
          n_replacements, = re.match("^(\d+) replacements$", line).groups()
          state = "item"
        else:
          save_item()
          record["title"] = line
          state = "need price and quantity"
      elif state == "ignore original price":
        # ignore original price
        state = "item"
      elif state == "need price and quantity":
        record["price"], record["unit_quantity"] = re.match(
          "^[$]([^ ]+) •(.*)$", line).groups()
        record["unit_quantity"] = record["unit_quantity"].strip()
        state = "replacement"
      elif state == "replacement":
        if line == "If out of stock,":
          state = "if out of stock"
        elif line == "If out of stock, replace with":
          state = "replace with"
        elif line == "Original item:":
          state = "original item"
        else:
          assert False
      elif state == "if out of stock":
        assert line in ["refund item", "find best match"]
        state = "item quantity"
      elif state == "replace with":
        if line == "Item quantity:":
          # no replacement
          state = "real item quantity"
        else:
          # ignore replacement item
          state = "item quantity"
      elif state == "original item":
        # ignore original item
        state = "item quantity"
      elif state == "item quantity":
        if line.startswith("or some other kind"):
          state = "item quantity"
        else:
          assert line == "Item quantity:"
          state = "real item quantity"
      elif state == "real item quantity":
        record["item_quantity"] = line
        state = "need price"
      elif state == "need price":
        assert line == "Current price:"
        state = "real price"
      elif state == "real price":
        record["current_price"], =  re.match("^[$]([0-9.]+)$", line).groups()
        state = "item"

    save_item()

    assert len(records) == int(n_items) + int(n_replacements)

  with open(fname + ".tsv", "w") as outf:
    for record in records:
      outf.write(
        "\t".join((record["title"],
                   record["price"],
                   record["unit_quantity"],
                   record["item_quantity"],
                   record["current_price"])) + "\n")
      
          
        
        
        
      

    
      
