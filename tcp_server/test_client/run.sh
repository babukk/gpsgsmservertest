#! /bin/sh
#--------------------------------------------------------------------------------------------------------------------------------------------

DIR="../.."
HOST=localhost
PORT=15555

if [ ! -d ${DIR}/.venv3 ]; then
    virtualenv -p `which python3` ${DIR}/.venv3/
    . ${DIR}/.venv3/bin/activate
    pip install --upgrade pip
    pip install -r ../requirements.txt
    pip freeze
else
    . ${DIR}/.venv3/bin/activate
fi

export DJANGO_PROJECT_PATH="../"

echo $1

login='tester1'
password='pbkdf2_sha256$150000$bqbwsWYh9xKz$YCLIVkKDE5RqdM9Bx4Ck8Xmhu1ChOcH8JxxlXJIKyyo='
IMEI='24353453452345345234534'
COMMAND='000L;'${login}';'${password}';12134;'${IMEI}';1;222;333333'

CRC16=`./calc_crc16.py ${COMMAND}`
COMMAND='>'${COMMAND}';'${CRC16}'\n'

DATA='00SD;03022020;00:10:23;40.785091;-73.968285;123;120;250;5;111'
CRC16=`./calc_crc16.py ${DATA}`
DATA='>'${DATA}
COMMAND=${COMMAND}${DATA}';'${CRC16}'\n'

DATA='00SD;03022020;00:15:03;40.785098;-73.968286;100;112;250;5;111'
CRC16=`./calc_crc16.py ${DATA}`
DATA='>'${DATA}
COMMAND=${COMMAND}${DATA}';'${CRC16}'\n'

DATA='00SD;03022020;00:19:13;40.785078;-73.968293;112;128;200;4;132'
CRC16=`./calc_crc16.py ${DATA}`
DATA='>'${DATA}
COMMAND=${COMMAND}${DATA}';'${CRC16}'\n'

#echo ${COMMAND}

python ./client.py --command="${COMMAND}" --host=${HOST} --port=${PORT}

deactivate
