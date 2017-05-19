# TEXT CLASSIFIER

## Project Group Members
- Yılmaz BAYSAL _21327694_
- Yunus Emre ZENCİRLİ _21328667_

## Project Subject
Text Classification 

## Used Language
English

## Brief Introduction About Project Content   
In Text Classification one or more classes are assigned to a document according to their content. Classes are selected from a previously established taxonomy (a hierarchy of catergories or classes). The Text Classification API takes care of all preprocessing tasks (extracting text, tokenization, stop-word removal and stemming) required for automated classification.  

## Command To Run The Code
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

### Sample output  
    test_instance_1.txt -> Sport
    test_instance_2.txt -> Politics  
    test_instance_3.txt -> Art & Design  