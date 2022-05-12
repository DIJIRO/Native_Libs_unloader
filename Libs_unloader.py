import subprocess
import json
import os
import sys
import re
def parsing(response_data):
    try:
        dir = re.findall('\./([^:]*)', response_data)[0]
        native_libs = re.findall('([^ ]*\.so)', response_data, re.DOTALL)
        if native_libs != []:
            #dirs.append({dir: native_libs})
            return {dir: native_libs}
    except Exception as ex:
        pass
def adb():
    adb_init = subprocess.Popen(['adb', 'shell'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    adb_init.stdin.write(b"su\n")#run adb shell with root
    return adb_init
def main():
    print('Created by https://github.com/DIJIRO')
    packet = sys.argv[1]# get packet name (com.example)
    adb_init = adb()
    cd_str = f'cd data/data/{packet}\n'
    adb_init.stdin.write(bytes(cd_str,encoding='cp866'))# cd to packet's data
    adb_init.stdin.write(b"ls -Ral\n")
    response = adb_init.communicate()[0].decode('cp866')#all dirs & files
    response_data = response.split('\r\n\r\n')
    dirs = [parsing(i) for i in response_data if i != None]
    dirs = [ i for i in dirs if i != None]
    out_dir = os.path.dirname(__file__) + '/' + packet
    if not os.path.exists(out_dir):# creating folder for output
        os.makedirs(out_dir)
    print(f'Output dir : {out_dir}')
    print('Processing...')
    for part in dirs:
        for dirname,libs in part.items():
            for lib in libs:
                adb_init = adb()
                adb_str = f"cp data/data/{packet}/{dirname}/{lib} /sdcard/{lib}\n"
                adb_init.stdin.write(bytes(adb_str,encoding='cp866'))
                adb_init.communicate()
                copy = subprocess.run(f'adb pull /sdcard/{lib} {out_dir}')#copying libs to pc

if __name__ == '__main__':
    main()