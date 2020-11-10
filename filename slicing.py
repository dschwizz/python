from pathlib import Path
import shutil, os, time
import pandas as pd
import re

sourcePath = Path(r'C:\Users\Danny\Documents\cleanedFOCUS.xlsx')

print(sourcePath)
print(sourcePath.name)

asst_name = sourcePath.name
asst_name = asst_name[:len(asst_name)-5]
print(asst_name)
