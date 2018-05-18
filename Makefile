
install :
	sudo pip3 install -r requirements.txt

build : build-ui clean-target
	pyinstaller -F MainFrame.py
	@cp -r ./assets ./dist/ 
	@cp ./run.sh ./dist/run.sh
	@echo "-------Build Done--------"

build-file : build-ui clean-target
	pyinstaller MainFrame.py
	@cp -r ./assets ./dist/MainFrame 
	@cp ./run.sh ./dist/MainFrame/run.sh
	@echo "-------Build Done--------"

build-ui :
	@./parseUI.sh

clean :
	@rm *.spec
	@rm -rf ./build
	@echo "-------Done--------"

clean-all : clean clean-target
	@echo "-------Clean all Done--------"

clean-target :
	@rm -rf ./dist
	@echo "-------Done--------"

run : 
	@echo "Starting APP ....."
	@./dist/run.sh
	@echo "-------APP closed--------"

run-file :
	@echo "Starting APP ....."
	@./dist/MainFrame/run.sh
	@echo "-------APP closed--------"
