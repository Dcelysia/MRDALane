# Data Preparation

## OpenLane

Follow [OpenLane](https://github.com/OpenDriveLab/PersFormer_3DLane#dataset) to download dataset and then link it under `data` directory.

```bash
cd data && makir openlane && cd openlane
ln -s ${OPENLANE_PATH}/images .
ln -s ${OPENLANE_PATH}/lane3d_1000 .
```
## Apollo

Follow [Apollo](https://github.com/yuliangguo/Pytorch_Generalized_3D_Lane_Detection#data-preparation) to download dataset and link it under `data` directory.

```bash
cd data && mkdir apollosyn_gen-lanenet
cd apollosyn_gen-lanenet
ln -s ${Apollo_Sim_3D_Lane_Release} .
ln -s ${data_splits} .
```