# Environment

It is recommanded to build a new virtual environment.

```bash
# first install pytorch
conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 cudatoolkit=11.3 -c pytorch

# then clone MRDALane and change directory to it to install requirements
cd ${MRDALane_PATH}
python -m pip install -r requirements.txt

pip install mmcv-full==1.5.0
pip install mmdet==2.24.0
pip install mmdet3d==1.0.0rc3
```