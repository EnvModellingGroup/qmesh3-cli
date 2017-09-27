FROM qmesh/qmesh-containers:ubuntu1604_qgisltr_gmsh304
RUN git clone --depth 2 https://bitbucket.org/qmesh-developers/qmesh.git && cd qmesh && make install && cd ../ && rm -rf qmesh
RUN git clone --depth 2 https://bitbucket.org/qmesh-developers/qmesh-cli.git && cd qmesh-cli && make install && make test
