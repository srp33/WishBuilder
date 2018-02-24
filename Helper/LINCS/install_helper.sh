#setting up environment for this project
export PATH=$softwareName/bin:$PATH
conda create --name lincs_env -y python=2.7.11 numpy=1.13.0 hdf5=1.10.1 h5py=2.7.1
