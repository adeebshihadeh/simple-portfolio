import json
import re
import mistune

sitefile = json.loads(open("site.json", "r").read())
outfile = sitefile["files"]["output"]
site_template = open(sitefile["files"]["site_template"], "r").read()
card_template = open(sitefile["files"]["card_template"], "r").read()
mddir = sitefile["files"]["mddir"]

def fix_links(md):
  for res in re.findall('\(([^)]+)\)', md):
    if "http" not in res:
      md = md.replace(res, mddir + res)
  return md

def build():
  content = sitefile["content"]
  html = ""
  id = 0
  for i in content:
    data = {
      "image": mddir + content[i]["image"],
      "card_title": "" if content[i]["imgonly"] else content[i]["title"],
      "title": content[i]["title"],
      "description": mistune.markdown(fix_links(open(mddir + content[i]["description"], "r").read())),
      "id": id
    }
    html += card_template.format(**data)
    id += 1

  html = site_template.format(title=sitefile["config"]["title"], subtitle=sitefile["config"]["subtitle"], body=html)

  # write to file
  with open(outfile, "w") as f:
    f.write(html)


if __name__ == "__main__":
  build()