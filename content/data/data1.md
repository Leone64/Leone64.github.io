---
title: "Cloud Data" 
date: 2025-04-10
lastmod: 2025-04-10
tags: ["dust cloud","dataset","python"]
author: ["Leon Engel"]
description: "This dataset contains the parameters of the cloud catalogue."
summary: "This dataset contains the parameters of the cloud catalogue."
editPost:
    URL: "https://github.com/Leone64/Leone64.github.io/tree/main/static"
    Text: "GitHub repository"
showToc: true
disableAnchoredHeadings: false

---

## Overview

This dataset describes the parameters of the members in the cloud catalogue as presented in my Bachelor Thesis.

---

## Download data

The parameters of the clouds in the catalogue are available in this [repository](https://github.com/Leone64/catalogue_dustclouds), as ```cloud-data.csv```.

---

## Working with the repo

```python
data_array = np.array(data)  # Convert the list to a NumPy array
mean = np.mean(data_array)
median = np.median(data_array)
std_dev = np.std(data_array)
min_value = np.min(data_array)
max_value = np.max(data_array)
```
---

