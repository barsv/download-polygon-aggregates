# src: https://chatgpt.com/g/g-p-6821226cd0c881918ac57748401da721-poleznoe/c/68c67044-ef94-8333-8b82-f02d2f598c22

sudo chmod +x ~/src/download-polygon-aggregates/viewer/porkbun/porkbun_dns.py
sudo chmod 600 ~/src/download-polygon-aggregates/viewer/porkbun/porkbun.env
sudo chmod +x ~/src/download-polygon-aggregates/viewer/porkbun/run_ddns.sh

# добавим в crontab (от root или нужного пользователя)
( crontab -l 2>/dev/null; echo '*/1 * * * * ~/src/download-polygon-aggregates/viewer/porkbun/run_ddns.sh >> ~/src/download-polygon-aggregates/viewer/porkbun/log/porkbun-ddns.log 2>&1' ) | crontab -
