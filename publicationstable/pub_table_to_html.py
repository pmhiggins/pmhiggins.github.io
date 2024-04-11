import pandas as pd
import numpy as np

df = pd.read_csv('pub_table_cites.txt',sep='\t',engine='python')


print(df)
refs = []

for i in range(len(df)):
    loc = df.iloc[i]
    thisref = loc.loc['Authors']
    thisref += ' ('+str(loc.loc['Date'])+')'
    thisref += ' "'+loc.loc['Title'] + '" '
    thisref += ' <i>'+loc.loc['Journal'] + '</i>'
    if not pd.isna(loc.loc['Vol']):
        thisref += ' <b>'+str(int(loc.loc['Vol'])) +'</b>'
    if not pd.isna(loc.loc['Issue']):
        thisref += ' ('+str(int(loc.loc['Issue'])) +')'
    if not pd.isna(loc.loc['Pages']):
        thisref += ' '+str(loc.loc['Pages'])
    if not pd.isna(loc.loc['DOI']):
        thisref += ' DOI: <a href="https://doi.org/'+loc.loc['DOI']+'" target="_blank"> '+loc.loc['DOI']+'</a>'

    print(thisref)

    refsec = "<tr class='w3-hover-gray'>\n<td>"+thisref+"</td>\n"
    if pd.isna(loc.loc['OA-link']):
        refsec += "<td class='w3-center'>" + loc.loc['OA-label'] +"</td>\n"
    else:
        refsec += "<td class='w3-center'><a href=" + str(loc.loc['OA-link']) +' target="_blank"> ' + str(loc.loc['OA-label'])+ "</a></td>\n"

    refsec += "<td class='w3-center'>\n"

    if not pd.isna(loc.loc['DOI']):
        refsec += '<span data-badge-type="donut" data-doi="'+loc.loc['DOI']+'" data-hide-no-mentions="true" class="altmetric-embed"></span>\n'

        refsec += '<span class="__dimensions_badge_embed__" data-doi="'+loc.loc['DOI']+'" data-style="small_circle" style="display:inline-block" data-hide-zero-citations="true"></span>\n'

    if not pd.isna(loc.loc['CiteCount']):
        refsec += '<span> <a href="'+loc.loc['Scholar-link']+'" target="_blank" class="w3-button w3-white w3-circle w3-xxlarge w3-card-4 w3-padding"><p class="fa fa-graduation-cap w3-cell-middle w3-medium"> '+ str(int(loc.loc['CiteCount'])) + '</p> </a> </span>\n'

    refsec += "</td>\n"
    refsec += "</tr>\n"

    print(refsec)

    refs.append(refsec)


# Creating an HTML file
Func = open("pubs.html","w")

# Adding input data to the HTML file
for ref in refs:

    Func.write(ref+'\n')

# Saving the data into the HTML file
Func.close()


# now all pubs can be copy/pasted into the index.html file.
# Not ideal but directly importing the html server-side seems to be difficult
