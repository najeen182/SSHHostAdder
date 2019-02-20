#!/usr/bin/env python

import os
import sys
import json
import socket
import argparse

from template import config_file,host_config_template,add_host_file,new_host_file


DEFAULT_CONFIG_FILE = os.path.join(os.getcwd(),"config.json")
DEFAULT_HOST_FILE = os.path.join(os.getcwd(),"host.json")
DEFAULT_SSH_CONFIG_FILE = os.path.expanduser("~/.ssh/config")

def parseargs():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i","--hostname",help="Hostname to be added",required=True)
	parser.add_argument("-p","--cport",help="port number if its not on default",required=False)
	parser.add_argument("-u","--uname",help="Username for login",required=False)
	parser.add_argument("-c","--cname",help="Short name",required=False)

	return parser.parse_args()

def create_ssh_config_file():
	with open(DEFAULT_CONFIG_FILE,"r") as f:
		data = json.load(f)

	if data:
		username = data.get('default').get('username')
		proxyserver = data.get('default').get('proxyserver')
		proxyip = data.get('default').get('proxyip')
		proxyport = data.get('default').get('proxyport')
	else:
		print("Config File Not Found")
		return

	with open(DEFAULT_SSH_CONFIG_FILE,"w") as f:
		template = config_file(proxyserver,proxyip,username,proxyport)
		f.write(template)

def template(hostname,cport,uname,cname):
        '''
	with open(DEFAULT_HOST_FILE,"r") as f:
            hostdata = json.loads(f)
        return hostdata
        '''
	#print(hostdata["hostlist"])
	with open(DEFAULT_CONFIG_FILE,"r") as f:
		data = json.load(f)   

	if data:
		username = data.get('default').get('username')
		domain = data.get('default').get('domain')
		port = data.get('default').get('port')
		proxyserver = data.get('default').get('proxyserver')
	else:
		print("Config File Not Found")
		return

	try:
		ip = socket.gethostbyname(hostname+'.'+domain)

	except socket.gaierror as e:
		print("Name Not Found")
		return 
		sys.exit(1)
	if cname:
		hostname = cname

	if uname:
		username = uname

	if cport:
		port = cport	

	hosttemplate = host_config_template(hostname,ip,username,port,proxyserver)

	with open(DEFAULT_SSH_CONFIG_FILE,"a+") as f:
		f.write("\n")
		f.write(hosttemplate)
                
        os.system('ssh-copy-id {0}'.format(hostname))
        '''
        if hostdata:
            h = hostdata
        else:
            h = []
        try:
            os.system('ssh-copy-id {0}'.format(hostname))
            h.append(add_host_file(ip,hostname,username,port))
        except:
            return "Error"
	with open(DEFAULT_HOST_FILE,"w") as f:
            json.dump(h,f,indent=4,sort_keys=True)
	'''

def add_in_file():
	print("file")


def main():
	if not os.path.exists(DEFAULT_SSH_CONFIG_FILE):
		create_ssh_config_file()
	try:
		args = parseargs()
	except argparse.ArgumentError as msg:
		print(msg)

	if args.hostname:
		template(args.hostname,args.cport,args.uname,args.cname)

if __name__ == "__main__":
	main()
