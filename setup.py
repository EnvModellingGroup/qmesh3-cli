#!/usr/bin/env python
#
#    Copyright (C) 2013 Alexandros Avdis and others. See the AUTHORS.md file for a full list of copyright holders.
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
#    along with QMesh.  If not, see <http://www.gnu.org/licenses/>.

def main():
    from setuptools import setup
    import os
    import subprocess


    # Put file containing git sha key in the right place for the egg-file.
    try:
        git_sha_key = subprocess.check_output(['git','rev-parse','HEAD'])
    except CalledProcessError:
        git_sha_key = 'Could not obtain git sha key.'
    git_sha_key_file = open('qmesh-cli/GIT_SHA_KEY','w')
    git_sha_key_file.write(git_sha_key)
    git_sha_key_file.close()
    # Put files containing version, license, authors list and
    # README in the right place for the egg-file.
    license_copied = subprocess.call(['cp','LICENSE','qmesh-cli/'])
    authors_copied = subprocess.call(['cp','AUTHORS.md','qmesh-cli/'])
    readme_copied = subprocess.call(['cp','README.md','qmesh-cli/'])
    version_copied = subprocess.call(['cp','VERSION','qmesh-cli/'])
    #Read version from file
    version_file = open('qmesh-cli/VERSION','r')
    qmesh_cli_version_string = version_file.readline().strip()
    version_file.close()

    try:
      destdir = os.environ["DESTDIR"]
    except KeyError:
      destdir = "/usr/share/"
    try:
        set
    except NameError:
        from sets import Set
  
    setup(
          name='qmesh-cli',
          requires=['qmesh (=='+str(qmesh_cli_version_string)+')'],
          install_requires=['qmesh==1.0'],
          version=qmesh_cli_version_string,
          description = "A Command Line Interface to qmesh",
          author = "The QMesh Development Team.",
          #author_email = "devel@qmesh.org",
          url = "https://qmesh.org",
          packages = [ ],
          package_dir = { },
          scripts=["qmesh-cli/qmesh"],
          package_data = {'qmesh-cli':['VERSION','GIT_SHA_KEY','LICENSE','AUTHORS.md','README.md']},
          test_suite = "tests"
         )

    # A little clean-up
    #subprocess.call(['rm','qmesh-cli/VERSION','qmesh-cli/GIT_SHA_KEY','qmesh-cli/LICENSE','qmesh-cli/AUTHORS.md','qmesh-cli/README.md'])

if __name__=='__main__':
    main()
