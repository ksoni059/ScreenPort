# ScreenPort

The ScreenPort is a reporting tool mostly used for recon purpose. When tools like webscreenshot generate lots screenshot of subdomains, so open each image manually and browse that domain manually is very boring and time consuming task. so rather do it manually this tool will do it same with automation and generate report of it. Report contains each subdomins's screenshots and its hyperlinks.

## Usage:

```
python ScreenshotReport.py -h
```
This will display help for the tool. Here are all options.

| Flag | Description | Usage |
|---|---|---|
| -i  |Use for get screenshot filepath as input | python ScreenshotReport.py -i 'imagefilepath'   |
| -o  |Use for generate HTML report on output path   | python ScreenshotReport.py -i 'imagefilepath' -o 'outputpath'  |

By default tool will generate HTML report on given input filepath.

Tool will take two argument, -i for images path as input and -o for generate HTML report on given path. -o is optional parameter, if user give outpath then report will generated on that path otherwise it will generate on given input path.

```
python ScreenshotReport.py -i E:\Screenshot\
```
Generate HTML report of all extracted screenshots

```
python ScreenshotReport.py -i E:\Screenshot\ -o E:\Reports\
```
Generate HTML report on given path.
