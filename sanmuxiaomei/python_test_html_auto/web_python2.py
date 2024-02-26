from re import A
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

info = input_group('Add user', [
    input('username', type=TEXT, name='username', required=True),
    input('password', type=PASSWORD, name='password', required=True),
    actions('actions', [
        {'label': 'Save', 'value': 'save'},
        {'label': 'Save and add next', 'value': 'save_and_continue'},
        {'label': 'Reset', 'type': 'reset', 'color': 'warning'},
        {'label': 'Cancel', 'type': 'cancel', 'color': 'danger'},
    ], name='action', help_text='actions'),
])
put_code('info = ' + json.dumps(info, indent=4))
if info is not None:
    save_user(info['username'], info['password'])  
    if info['action'] == 'save_and_continue':
        add_next()  

if __name__=='__main__':
    #启动服务
    start_server(
        main, 
        port=8082, 
        debug=True, 
        cdn=False,
        auto_open_webbrowser=True)

