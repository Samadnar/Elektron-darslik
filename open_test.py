import os
def open_file_s1():
    # script_dir = os.path.dirname(r'Documents\Savollar\savollar.pdf')
    # file_path = os.path.join(script_dir, 'savollar.pdf')
    # os.startfile(file_path)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'Documents/Savollar/savollar.pdf')
    os.startfile(file_path) 
    
def open_file_t1():
    # script_dir = os.path.dirname(r'Documents\Test\Test variantlari.pdf')
    # file_path = os.path.join(script_dir, 'Test variantlari.pdf')
    # os.startfile(file_path)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'Documents/Test/Test variantlari.pdf')
    os.startfile(file_path) 
    
def open_file_m1():
    # script_dir = os.path.dirname(r'Documents\Mustaqil\1.pdf')
    # file_path = os.path.join(script_dir, '1.pdf')
    # os.startfile(file_path)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'Documents/Mustaqil/1.pdf')
    os.startfile(file_path) 
    
def open_file_m2():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'Documents/Mustaqil/2.pdf')
    os.startfile(file_path) 