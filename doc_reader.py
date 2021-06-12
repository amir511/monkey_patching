import os

def document_view_function(func):

    func_name = func.__name__
    doc_file_name = func_name + '.md'
    doc_file_path = os.path.join(os.getcwd(), doc_file_name)
    with open(doc_file_path, 'r') as f:
        documentation = f.read()
    
    func.__doc__ = documentation
    return func