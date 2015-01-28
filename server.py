from flask import Flask
from flask import render_template
from flask import jsonify, request
import requests
import xml.etree.ElementTree as ET
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/site/<site>')
def getSite(site=None):
    riversite = {}
    riversite['site'] = site
    xmlUrl = 'http://www.nwrfc.noaa.gov/xml/xml.cgi?id=' + site
    xmlResponse = requests.get(xmlUrl)
    xmlTree = ET.fromstring(re.sub('xmlns="[^"]+"', '', xmlResponse.content, count=1))
    riversite['sitedata'] = getSiteData(xmlTree)
    riversite['observedvalue'] = getObservedValue(xmlTree)
    return jsonify(riversite)

@app.route('/api/sites')
def getSites():
    riversites = { 'sites': [] }
    sites = request.args.get('sites')
    xmlUrl = 'http://www.nwrfc.noaa.gov/xml/xml.cgi?id='
    for site in sites.split(','):
        riversite = {}
        riversite['site'] = site
        xmlResponse = requests.get(xmlUrl + site)
        xmlTree = ET.fromstring(re.sub('xmlns="[^"]+"', '', xmlResponse.content, count=1))
        riversite['sitedata'] = getSiteData(xmlTree)
        riversite['observedvalue'] = getObservedValue(xmlTree)
        riversites['sites'].append(riversite)
    return jsonify(riversites)


def getSiteData(xmlTree):
    sitedata = {}
    sitedata['description'] = xmlTree.findtext('SiteData/description', '')
    sitedata['county'] = xmlTree.findtext('SiteData/county', '')
    sitedata['state'] = xmlTree.findtext('SiteData/state', '')
    sitedata['elevation'] = xmlTree.findtext('SiteData/elevation', '')
    sitedata['lat'] = xmlTree.findtext('SiteData/latitude', '')
    sitedata['long'] = xmlTree.findtext('SiteData/longitude', '')
    sitedata['bankfullstage'] = xmlTree.findtext('SiteData/bankfullStage', '')
    sitedata['floodstage'] = xmlTree.findtext('SiteData/floodStage', '')
    return sitedata

def getObservedValue(xmlTree):
    observeddata = xmlTree.findall('.//observedValue')[-1:][0]
    observedvalue = {}
    observedvalue['datadatetime'] = observeddata.findtext('dataDateTime', '')
    observedvalue['stage'] = observeddata.findtext('stage', '')
    observedvalue['discharge'] = observeddata.findtext('discharge', '')
    return observedvalue

if __name__ == '__main__':
    app.debug = True
    app.run()
