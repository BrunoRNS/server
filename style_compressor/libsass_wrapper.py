# This file is a wrapper for the libsass library. It compiles scss files to css files in compressed format.
from pathlib import Path
import sass

BASE_DIR = Path(__file__).resolve().parent.parent

def _compile_scss(input_file_loc: str, output_file_loc: str) -> str:
   """
   This function compiles a scss file to css in compressed format.
   """
   file: str
    
   input_file_loc = BASE_DIR / input_file_loc
   output_file_loc = BASE_DIR / output_file_loc


   with open(input_file_loc, 'r') as input_scss:
      file = input_scss.read()

   with open(output_file_loc, 'w') as output_css:
      output_css.write(sass.compile(string=file, output_style='compressed'))
