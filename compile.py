import json
import mistune

sitefile = json.loads(open("site.json", "r").read())
outfile = sitefile["files"]["output"]
site_template = open(sitefile["files"]["site_template"], "r").read()
card_template = open(sitefile["files"]["card_template"], "r").read()

def build():
  content = sitefile["content"]
  html = ""
  id = 0
  for i in content:
    data = {
      "image": content[i]["image"],
      "title": content[i]["title"],
      "description": mistune.Markdown(content[i]["description"]),
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