#for use with programs/languages page, generates
#html for whatever div holds program box boxes

import json;

def main():
    with open("pbox.json","r",encoding="utf8") as jfile:
        data=json.load(jfile);

    for x in data["boxes"]:
        print(genBoxBox(x));


def genBoxBox(data):
    html='''<div class="program-box-box {}a">
<p class="pbox-title {}b">{}</p>\n\n'''.format(data["colour"],data["colour"],data["title"]);

    for x in data["items"]:
        html+=genBox(x["img"],x["title"]);

        if x!=data["items"][-1]:
            html+="\n";

    html+="</div>\n";

    return html;

def genBox(img,name):
    return '''<div class="program-box">
<img src="{}">
<p>{}</p>
</div>\n'''.format(img,name);

main();
