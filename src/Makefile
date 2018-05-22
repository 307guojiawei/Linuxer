
install : install-dependence build-deb_v2
	@echo "Start dpkg install..."
	@sudo dpkg -i ./dist/Linuxer.deb
	@echo "All done. Check app list and enjoy :)"

install-dependence :
	@echo "Install dependencies ...."
	@sudo pip3 install -r requirements.txt
	@echo "Done."

build : build-ui clean-target
	pyinstaller -F MainFrame.py
	mkdir ./dist/bin
	mv ./dist/MainFrame ./dist/bin/MainFrame
	@cp -r ./assets ./dist/bin
	@cp ./run.sh ./dist/bin/run.sh
	@echo "-------Build Done--------"

build-file : build-ui clean-target
	pyinstaller MainFrame.py
	@cp -r ./assets ./dist/MainFrame 
	@cp ./run.sh ./dist/MainFrame/run.sh
	@echo "-------Build Done--------"

build-ui : show-logo 
	@./parseUI.sh

build-deb : build
	cp -r ./deb ./dist/
	cp -r ./dist/bin/* ./dist/deb/opt/linuxer
	dpkg -b ./dist/deb ./dist/Linuxer.deb

build-deb_v2 : build-file
	cp -r ./deb ./dist/
	cp -r ./dist/MainFrame/* ./dist/deb/opt/linuxer
	dpkg -b ./dist/deb ./dist/Linuxer.deb

clean :
	rm *.spec
	rm -rf ./build
	@echo "Done."

clean-all : clean clean-target
	@echo "-------Clean all Done--------"

clean-target :
	rm -rf ./dist
	@echo "Done."

run : show-logo 
	@echo "Starting APP ....."
	@./dist/bin/run.sh
	@echo "-------APP closed--------"

run-file : show-logo 
	@echo "Starting APP ....."
	@./dist/MainFrame/run.sh
	@echo "-------APP closed--------"

show-logo :
	@clear
	@cat ./logo.txt
