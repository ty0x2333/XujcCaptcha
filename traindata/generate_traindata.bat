@echo off
rem 执行改批处理前先要目录下创建font_properties文件

echo Run Tesseract for Training..
tesseract.exe xujc.normal.exp0.tif xujc.normal.exp0 nobatch box.train

echo Compute the Character Set..
unicharset_extractor.exe xujc.normal.exp0.box
mftraining -F font_properties -U unicharset -O xujc.unicharset xujc.normal.exp0.tr

echo Clustering..
cntraining xujc.normal.exp0.tr

echo Rename Files..
rename normproto xujc.normproto
rename inttemp xujc.inttemp
rename pffmtable xujc.pffmtable
rename shapetable xujc.shapetable

echo Create Tessdata..
combine_tessdata xujc.
