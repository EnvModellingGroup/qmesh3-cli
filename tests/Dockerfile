FROM qmesh/qmesh-containers:ubuntu1604_qgisltr_gmsh304
RUN git clone https://bitbucket.org/qmesh-developers/qmesh.git; cd qmesh; make install; cd ../
RUN git clone https://bitbucket.org/qmesh-developers/qmesh-cli.git; cd qmesh-cli; make install; make test
