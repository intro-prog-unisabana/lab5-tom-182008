global_int = None
global_str = None

def set_globals(some_int, some_str):
    global global_int
    global global_str
    
    global_int = some_int
    global_str = some_str

def get_globals():
    return (global_int, global_str)