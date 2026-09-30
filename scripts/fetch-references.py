import urllib.request,urllib.parse,json,pathlib,time
ids=['40517027','12856767','39996479','32772396','9787779','31918723','40470277','42791806','40216095','10659311','24528139','26340142','25996660','34067449','37060454']
results=[]
for pmid in ids:
 url='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':'EXT_ID:'+pmid+' AND SRC:MED','format':'json','resultType':'core'})
 try:
  data=json.load(urllib.request.urlopen(url))['resultList']['result'][0]
  results.append(data)
  print(pmid, data['title'],data.get('doi'),data.get('authorString'),data.get('pubYear'))
  print(data.get('abstractText','')[:7000])
 except Exception as e: print('ERROR',pmid,str(e))
pathlib.Path('../references-verified.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
