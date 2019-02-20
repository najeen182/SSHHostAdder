#!/usr/bin/env python

def config_file(ip,hostname,user,port):
	config = '''Host {0}
	HostName {1}
	User {2}
	Port {3}'''.format(ip,hostname,user,port)

	return config

def host_config_template(hostname,ip,user,port,proxyserver):
	config = '''Host {0}
	HostName {1}
	User {2}
	Port {3}
	ProxyCommand ssh -q -W %h:%p {4}'''.format(hostname,ip,user,port,proxyserver)

	return config

def add_host_file(ip,cname,username,port):
	hostfile = {
	    'host' : ip,
	    'hostname' : cname,
	    'username' : username,
	    'port' : port,
	}

	return hostfile

def new_host_file(ip,cname,username,port):
	hostfile = {"hostlist":[{
		"host" : ip,
		"hostname" : cname,
		"username" : username,
		"port" : port
		}]}
	
	return hostfile
