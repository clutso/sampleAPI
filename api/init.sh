echo "init started wairing 1 min"
sleep 40 
echo "starting DB"
python populateDB.py
echo "DB started"
gunicorn -b 0.0.0.0:80 main:app
echo "done"