#!/usr/bin/env python3
import argparse
import requests
import json
from prettytable import PrettyTable
from colorama import Fore, Back, Style
import os

# Docs:
# https://api.gandi.net/docs/livedns/

try:
	API_KEY=os.environ['API_KEY']
except Exception as e:
	print("Error: environment variable API_KEY must be specified")
	exit(-1)

def colourize_type(rr_type):

	if rr_type == 'A':
		return Fore.RED + Style.BRIGHT + rr_type + Style.RESET_ALL
	if rr_type == 'AAAA':
		return Fore.RED + rr_type + Style.RESET_ALL
	if rr_type == 'MX':
		return Fore.YELLOW + Style.BRIGHT + rr_type + Style.RESET_ALL
	if rr_type == 'CNAME':
		return Fore.BLUE + Style.BRIGHT + rr_type + Style.RESET_ALL

	return rr_type

def list_domains():
	
	resp = requests.get('https://api.gandi.net/v5/livedns/domains',
		headers={'Authorization': f'Apikey {API_KEY}'}).json()

	return [x['fqdn'] for x in resp]

def examine_domain(domain):
	
	resp = requests.get(f'https://api.gandi.net/v5/livedns/domains/{domain}/records',
		headers={'Authorization': f'Apikey {API_KEY}'}).json()

	table = []
	for d in resp:
		vals = []
		vals.append(d['rrset_name'])
		vals.append(colourize_type(d['rrset_type']))
		vals.append(d['rrset_ttl'])
		vals.append('\n'.join(d['rrset_values']))

		table.append(vals)

	tab = PrettyTable(['Name', 'Record Type', 'TTL', 'RR Values'])
	tab.add_rows(table)
	print(f'\nInfo for {Fore.GREEN + Style.BRIGHT + domain + Style.RESET_ALL}:')
	print(tab)

	return

def add_record(domain, type, ip):
	
	data = {
		'rrset_name': domain,
		'rrset_type': type,
		'rrset_values': [ip]
	}

	resp = requests.post(f'https://api.gandi.net/v5/livedns/domains/{domain}/records',
		headers={'Authorization': f'Apikey {API_KEY}'},
		data=data
		)

	return resp

def delete_record(domain, rr_name):

	resp = requests.delete(f'https://api.gandi.net/v5/livedns/domains/{domain}/records/{rr_name}',
		headers={'Authorization': f'Apikey {API_KEY}'}
		)

	return resp.text()


def clear_records(domain):

	resp = requests.delete(f'https://api.gandi.net/v5/livedns/domains/{domain}/records',
		headers={'Authorization': f'Apikey {API_KEY}'})

def main(args):
	if args.action == 'list':
		print('Domains:')
		print(list_domains())
	if args.action == 'info':
		examine_domain(args.domain)
	if args.action == 'clear':
		clear_records(args.domain)
		examine_domain(args.domain)
	if args.action == 'add':
		add_record(args.domain, args.type, args.ip)
		examine_domain(args.domain)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('action', choices=['list', 'info', 'clear', 'add'])
	parser.add_argument('--domain', '-d', help='Domain')
	parser.add_argument('--ip', '-i', help='IP address')
	parser.add_argument('--type', '-t', help='Type of record to add')

	args = parser.parse_args()

	main(args)