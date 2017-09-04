#!/bin/sh

#    Copyright (C) 2013 Alexandros Avdis and others. See the AUTHORS file for a full list of copyright holders.
#
#    This file is part of qmesh-cli.
#
#    qmesh-cli is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    qmesh-cli is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with qmesh-cli.  If not, see <http://www.gnu.org/licenses/>.

.PHONY: test unit integration

test: unit integration

integration:
	@echo ">>> Running qmesh-cli integration tests..."
	python -m unittest discover --start-directory=integration --pattern=*.py --verbose

unit:
	@echo ">>> Running qmesh-cli unit tests..."
	python -m unittest discover --start-directory=unit --pattern=*.py --verbose

clean: clean-unit clean-integration

clean-unit:
	#@echo ">>> Cleaning unit tests directory..."
	#for file in unit/*; do \
	#cd $${file};\
	#make clean;\
	#cd ../..;\
	#done ;

clean-integration:
	@echo ">>> Cleaning integration tests directory..."
	for file in integration/*; do \
	cd $${file};\
	make clean;\
	cd ../..;\
	done ;
