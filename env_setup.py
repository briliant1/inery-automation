import os

innery_node_path = os.path.join(os.getcwd(), "inery-node")
innery_automation_path = os.path.join(os.getcwd(), os.path.dirname(__file__))
print(os.getcwd())

def exportPath() :
    os.chdir('../inery/bin')
    path = f'export PATH="$PATH:{os.getcwd()}"'
    user = os.getenv("HOME")
    bashrc_path = os.path.join(user, '.bashrc')
    with open(bashrc_path, 'a') as bashrc :
        bashrc.write(path)