import os
import shutil
from openvoice_cli import tune_one
from pathlib import Path

os.chdir('Trans')

for item in Path('.').glob('*'):
    name = str(item)
    input_file = name
    ref_file = f'..\Origin\{name}'
    output_file = f'..\Out\{name}'
    device = 'cpu'
    try:
        tune_one(input_file=input_file, ref_file=ref_file, output_file=output_file, device=device)
        print(" ")
        print(f"\033[1;32m Out\{item}")
        print("\033[1;37m ")
    except Exception:
        pass
    
shutil.rmtree('..\Trans\processed')

