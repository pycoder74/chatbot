import os
def install_package(packagename):
    install=f'cmd /k pip3 install {packagename}'
    os.system(install)
    print(f'{packagename} installed')

