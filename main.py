import requests
import json
import os

mcv = '1.18.1'

print(f'In search of a new version of paper for {mcv} version...')

main = json.loads(requests.get(url=f'https://papermc.io/api/v2/projects/paper/versions/{mcv}/').content)

try:
    maxb = max(main['builds'])
except KeyError:
    print(f'Paper does not exist on {mcv} version')
    exit(28)
newv = json.loads(requests.get(url=f'https://papermc.io/api/v2/projects/paper/versions/{mcv}/builds/{maxb}').content)
fname = newv['downloads']['application']['name']
dw = f'https://papermc.io/api/v2/projects/paper/versions/{mcv}/builds/{maxb}/downloads/{fname}'

print('New paper version was found!')

if os.path.exists(f'{os.getcwd()}/{fname}'):
    print('The latest version already exists')
    exit()

iterr = 0
fold = os.listdir(os.getcwd())
for i in fold:
    if i.startswith(f'paper-{mcv}-') and i.endswith('.jar'):
        old = fold[iterr]
        print(f'Deleting the old {old} version...')
        os.remove(f'{os.getcwd()}/{old}')
        break
    iterr += 1

print('Downloading new version...')

with open(f'{os.getcwd()}/{fname}', 'wb') as f:
    f.write(requests.get(url=dw).content)

print(f'P{fname[1:]} successfully downloaded!')

# print('Editing start.sh') #If you need to, you can change the file to run the server.
#
# with open("start.sh", "r+") as f: #Or start.bat
#     f.write(f"java -Xms1024M -Xmx1024M -jar {fname} nogui") #Properties

print('Done!')
exit()
