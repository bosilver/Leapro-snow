
rm -rf build

python manage.py staticsitegen --settings=leapro_snow.medusa_settings
#mkdir certification
#mv build/Leapro-snow/certification certification/index.html
#mv certification Leapro-snow/
