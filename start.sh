if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/BalamuruganDV/LUNA-XTRA-FEATURE.git /LUNA-XTRA-FEATURE
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /LUNA-XTRA-FEATURE
fi
cd /LUNA-XTRA-FEATURE
pip3 install -U -r requirements.txt
echo "πππ°πππΈπ½πΆ α‘α΄[π»ππ½π°]..."
python3 bot.py
