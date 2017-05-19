# Text Classifier

Yılmaz BAYSAL (21327694) - Yunus Emre ZENCİRLİ (21328667)

Project subject: Text Classification - Used languages: English

=============================  
In Text Classification one or more classes are assigned to a document according to their content. Classes are selected from a previously established taxonomy (a hierarchy of catergories or classes). The Text Classification API takes care of all preprocessing tasks (extracting text, tokenization, stop-word removal and stemming) required for automated classification.
=============================

## Command to run the code
_python3 main.py $(data_folder_path)_

## Input file structure
    |-- data/
    |   |-- train/
    |   |   |-- class1/
    |   |   |   |-- train_instance_1.txt
    |   |   |   |-- train_instance_2.txt
    |   |   |   |-- train_instance_3.txt
    |   |   |   |-- ...
    |   |   |-- class2/
    |   |   |   |-- train_instance_1.txt
    |   |   |   |-- ...
    |   |   |-- ...
    |   |-- test/
    |   |   |-- test_instance_1.txt
    |   |   |-- test_instance_2.txt
    |   |   |-- test_instance_3.txt
    |   |   |-- ...
    |   |-- stop_words.txt
        
## Output file format
Outputs are printed on both to the console and to a file named _output.txt_

=============================  
art_design_1.txt -> Art & Design  
art_design_2.txt -> Art & Design  
art_design_3.txt -> Art & Design  
  
education_1.txt -> Education  
education_2.txt -> Education  
education_3.txt -> Education  
=============================  