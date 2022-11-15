#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-06-04 11:25:06
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import pandas as pd
import re
import json
import time as tm
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from gcloud import storage
from ftplib import FTP
from glob import glob

def uploadjson(file, filename):
    credentials_dict = {
        'type': 'service_account',
        'client_id': "110677326745099597758",
        'client_email': 'cna-flask-project@appspot.gserviceaccount.com',
        'private_key_id': 'afc2c0eb7f067837400bf1dfa2b7d9db8efc5d80',
        'private_key': "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCx9pYsyRNhst55\nutGjnslD5j0v+ZW7Het34MkbCcQL1NPPKxccMLa30J8gE9uMBDGPLrDwzyFTSOhF\n3BIGhsnILks5E7nPWmUUy601lJkfBWE3rS0OcCs2/cntNwDhf/ng1sj3Jdi6PUVo\nydefKeA+2Ii41JRFtfXWlqAFhP3qrNxsx2ZPGB7/cUfm7gPHDheT9XRUQPuzHfYX\nFznPm2wmsLpJ3aEYW/SxCOmSVehhbj8bC53GFgyTxmZgvBqL4ZYsslKarl6fNemG\nduiNV04z0rNzHpEkuejnaldPRTfL+FqYglvUB0TswFoca1ZCYwPp4XM5F+LvSYsm\na1eXY6qtAgMBAAECggEAC5McsFwBoTSXiLZQZUJyF7L1XtXuWaW4B2t82P/ZGuXk\nQtCsJ565e5obh2QTPveU25mvU3I9WiPfS4/lMjx5CkaMiPFR//0CnwgiQ15fWSep\n64udZxd/kAuQoxeVPJVsxKVjm8N/5ZkPlyGtnwIDvkKqHc9ht2j+zM6uKL2+IBGz\nK/qHiA/ZHDrprknkTD4oKr3TU+0gbRN9bUgNDeCDaA1hruLhKikYo2h2Q/wsqPwd\nny//ZNsN/TYhrCKXRtsj95iC+Hg5slJKRxwijMahgqy/vatY+XHmbqrCOZelylNZ\n4jphmXU2VaLrgqXn68HwOp5PbLLvXMr8auKjUjzFUQKBgQDwey9d8d3cEJw4Pqvs\nkWhJv19hXoz5CyHhlDnbWsFHoT2Si4iV8M/ugk+wLiyerF4Mdo0TecUv/N56CWsM\n6EffaRanqB5vdO2ynLnMnrrZN0Gdypreb/ZbR07lF/gUT/nNev3awdqRVBP4+ckV\nex8Uw/uRX9TK4nYSuZ9PHD4vxQKBgQC9cpZ4dUnOahnsexb2nqIGl4l80/ujoZfu\noL7HacwaGOBjRoqc4mde1C3ZABO/iGSiRfweM4t1TXoc6ZqKUvJXURPXVPySAuoY\nvVSgoxOYnPASikUEqyl66cH3Gs+nMdA7wtfYjltwjMvmwv7UTXmRPjB49KhCUVUB\nGJ8Yy2EVyQKBgECYlkyh33pxa8Uf8IaHOIA2y6QYBb4P43X4nuHxKuHWyfdHS9Ua\n7n+euVEV1h55JnoqjhKhLvqI7inRxdOdwVCdpdw7KJG/0umbd70jFgWq9hEwjxEY\n+g/iw6p+GcE7ClrLoszULaXD8+l5Dy6Z9+tYCYcvOrWUxyqYedaCO6IRAoGBAKdO\nC+6jfiPJdc1vQu9XVrXFnAjeWKvAaKG32ePX3gTqFTf3MzCrjSik7zxlogsTE/Rv\nI+E0GiPk4UOpVe50pEpScthG2KrF4iEpCxS2D/dGGYn2DE+8LOy8hayJQ/tetYwh\nXWeFCOHTpbrMWCn7pbGMH1iij/nJQ+2s5cwKyFlpAoGBAJlAxteQm+1DSIFmkArp\n5NwrM3q0IwBrjCoCbuHB8ch0SqJq1X/m9WCtX2OQVgFlEVC2KcpIpNfgIR/YfV6l\nQPte4h4M0+oUzq2GP5WtobYb4VlsSthelq7Jbkc9VjTr/aMb3Ww84l46+oeoKiKJ\nrkrBvrVGAUzsucEHGcfyDt8i\n-----END PRIVATE KEY-----\n",
    }
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        credentials_dict
    )
    client = storage.Client(credentials=credentials, project='cna-flask-project')
    bucket = client.get_bucket('cna-flask-project.appspot.com')
    blob = bucket.blob('2020recall/{}.json'.format(filename))
    blob.upload_from_string(file, content_type='application/json')


while 'data\\final.json' not in glob('data\\*.json'):
    loopbegin = datetime.now()
    print('======================='+loopbegin.strftime("%H:%M"))
    with open('data\\running.json','r') as json_file:
        data = json.load(json_file)

    a = [i for i in data['CX'] if i['cityCode'] =='000' and i['deptCode']=='000'][0]

    with open('data\\progress.json','w') as f:
        json.dump(a, f)

    file_path = 'progress.json'
    # with FTP('demo.cna.com.tw','u0401006','capo4188') as ftp, open('data/'+file_path, 'rb') as file:
    #     ftp.cwd('/20200605-recallvote/data')
    #     ftp.storbinary(f'STOR {file_path}', file)
    with FTP('172.17.242.151','20090948','u0401006@CNA123') as ftp, open(f'data/'+ file_path, 'rb') as file:
        ftp.cwd('/20200605-recallvote/data')
        ftp.storbinary(f'STOR {file_path}', file)
    with FTP('210.69.89.186','20090948','u0401006@CNA123') as ftp, open('data/'+ file_path, 'rb') as file:
        ftp.cwd('/20200605-recallvote/data')
        ftp.storbinary(f'STOR {file_path}', file)

    print('now sleep {}s'.format(180-(datetime.now()-loopbegin).total_seconds()))
    tm.sleep(180-(datetime.now()-loopbegin).total_seconds())

with open('data\\final.json','r') as json_file:
    final = json.load(json_file)

df = pd.DataFrame.from_dict(final['CX'],orient='columns')
df['tboxNo']  = df['tboxNo'].astype('str')
df['deptbox'] = df['deptCode']+df['tboxNo']
lookup = pd.read_csv('data\\khd.csv', sep='\t',dtype='str')

df1 = pd.merge(df ,lookup, left_on="deptbox", right_on ='deptbox', how='left')
df1 = df1.groupby(['District','Village']).sum().reset_index()

df1['agreeRate'] = df1['agreeTks'] / df1['prof7'] * 100
df1['notInvolved'] = df1['prof4'] + df1['prof6']
df1['notInvolved'] = df1['notInvolved'].astype('int')
df1['notInvolved'] = df1['notInvolved'] / df1['prof7']*100
df1['prof2'] = df1['prof2'] / df1['prof7']*100
df1['disagreeRate'] = df1['disagreeTks'] / df1['prof7']*100

color = ['#272727','#3C3C3C','#4F4F4F','#5B5B5B','#6C6C6C','#8E8E8E','#ADADAD','#D0D0D0','#F0F0F0']
dcolor = []
for i in df1['agreeRate']:
    if i < 11:
        dcolor.append(color[8])
    elif i < 16:
        dcolor.append(color[7])
    elif i < 21:
        dcolor.append(color[6])
    elif i < 26:
        dcolor.append(color[5])
    elif i < 31:
        dcolor.append(color[4])
    elif i < 36:
        dcolor.append(color[3])
    elif i < 41:
        dcolor.append(color[2])
    elif i < 46:
        dcolor.append(color[1])
    else:
        dcolor.append(color[0])
df1['DistrictColor'] = dcolor
df2 = df1[['District', 'Village', 'agreeTks', 'agreeRate', 'disagreeTks','disagreeRate','prof2','notInvolved','DistrictColor']]

df2.to_json('data\\2020recall.json', orient='records')

file_path = '2020recall.json'

# with FTP('demo.cna.com.tw','u0401006','capo4188') as ftp, open('data\\'+file_path, 'rb') as file:
#     ftp.cwd('/20200605-recallvote/data')
#     ftp.storbinary(f'STOR {file_path}', file)
with FTP('172.17.242.151','20090948','u0401006@CNA123') as ftp, open(f'data\\'+ file_path, 'rb') as file:
    ftp.cwd('/20200605-recallvote/data')
    ftp.storbinary(f'STOR {file_path}', file)
with FTP('210.69.89.186','20090948','u0401006@CNA123') as ftp, open('data\\'+ file_path, 'rb') as file:
    ftp.cwd('/20200605-recallvote/data')
    ftp.storbinary(f'STOR {file_path}', file)