#!/usr/bin/env python

import json

from template import add_host_file

def gethost():
	with open('host.json','r') as f:
		d = json.load(f)

	host = add_host_file("202.79.32.1","32","212","23")
	d['hostlist'].append(host)

	print(d['hostlist'])
def main():
	gethost()

if __name__ == "__main__":
	main()
