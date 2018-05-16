pyuic5 design.ui -o design.py
echo 'mainUI done'

pyuic5 ./modules/Dash/design.ui -o ./modules/Dash/design.py
echo 'Dash done'

pyuic5 ./modules/Processes/design.ui -o ./modules/Processes/design.py
echo 'Processes done'

pyuic5 ./modules/Resource/design.ui -o ./modules/Resource/design.py
echo 'Resource done'

pyuic5 ./modules/Setup/design.ui -o ./modules/Setup/design.py
echo 'Setup done'

pyuic5 ./modules/Startups/design.ui -o ./modules/Startups/design.py
echo 'Startups done'


echo '.......DONE.......'