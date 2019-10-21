import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", dest='input', required=True, type=str, help="add screenshot file path")
parser.add_argument("-o", dest='output', type=str, help="generate HTML report on given path")
args = parser.parse_args()
input = args.input
filename = "ScreenshotReport.html"

if args.output is None:
    output = os.path.join(input, filename)
else:
    output = args.output + "\\" + filename

strHTML = "<!DOCTYPE html><html><head><style>" \
          "body { font-size: 15px; font-family: Arial, Helvetica, sans-serif; background: black; color: white; } " \
          "th,td { padding: 10px; } img { height: 500px; width: 750px; border-style: double; padding: 5px; border-color: #8a8787; } " \
          "a { font-size: 15px; } h2 {color: #86868a; text-align: center;}</style>    " \
          "<title>Screenshot Preview Report</title></head><body><h2>Screenshot Report</h2><table>"

for file in os.listdir(input):
    src = file.rsplit('_', 1)
    src = src[0].replace("_", ":", 1)
    strBody = "<tr><td><img src=" + os.path.join(input, file) + " />" \
              "</td><td><a href=" + src + " target=\"_blank\">" + src + "</a></td></tr>"
    strHTML = strHTML + strBody

strHTML = strHTML + "</table></body></html>"

hs = open(output, 'w')
hs.write(strHTML)

print("Screenshot report generated.")
