#import entrez module
from Bio import Entrez

# set variables
taxids = ['515482', '515474', '9606']       # id needs to be quoted, otherwise, it will give you attributeError

# set email
Entrez.email = "youremail@gmail.com"

# traverse ids
for taxid in taxids:
    handle = Entrez.efetch(db="taxonomy", id=taxid, mode="text", rettype="xml")
    records = Entrez.read(handle)
    for taxon in records:
        for k, v in taxon.items():
            print (k, v)
            print ("\n")
            
        taxid = taxon["TaxId"]
        name = taxon["ScientificName"]
        tids = []
        for t in taxon["LineageEx"]:
            tids.insert(0, t["TaxId"])
        tids.insert(0, taxid)
        print ("%s\t|\t%s\t|\t%s" % (taxid, name, " ".join(tids)))
