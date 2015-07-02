#!/usr/bin/python

import sys, urllib2, xmltodict,re

# setup params
ofile = 'spend.dat'
endpoint = 'http://www.usaspending.gov/faads/faads.php?'
outfile = open(ofile,'w')
outfile.write("%s,%s\n" % ("Recipient","Amount"))

# build endpoint call
options = ['detail=l',
           'fiscal_year=2013',
           'principal_place_state_code=47']
url = ''.join([endpoint,'&'.join(options)])
file = urllib2.urlopen(url)
data = file.read()
file.close()
data = xmltodict.parse(data)
spend = 0.0
for a in data['usaspendingSearchResults']['data']['records']['record']:
    recip = str(a['recipient_name'])
    recip = re.sub(r'\W+', '_', recip)
    amt = float(a['fed_funding_amount'])
    outfile.write("%s,%.2f\n" % (recip,amt))
    spend += amt
spend = spend/1.0e9
print "Total spend: $%.0fB" % spend
outfile.close()
