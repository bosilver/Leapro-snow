
rm -rf build

python manage.py staticsitegen --settings=leapro_snow.medusa_settings
cp -r build/* /Users/sherry/Documents/program-project/website/leaprosnow-static
cp -r static /Users/sherry/Documents/program-project/website/leaprosnow-static
cp -r media /Users/sherry/Documents/program-project/website/leaprosnow-static
#mkdir certification
#mv build/Leapro-snow/certification certification/index.html
#mv certification Leapro-snow/
