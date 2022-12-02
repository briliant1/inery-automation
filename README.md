# inery-automation

**First Install : Install ineryMenu Automation**
	Pastikan VPS bersih, nggak ada folder inery 

1. Jalankan script dibawah

```shell
rm -rf ./inery-automation/; git clone https://github.com/briliant1/inery-automation.git; chmod +x ./inery-automation/command.sh; chmod +x ./inery-automation/ineryMenu.py; source ~/.bashrc; ./inery-automation/command.sh
```

2. Reconnect SSH
3. jalankan command ``ineryMenu.py``
4. Menu Akan Muncul
   
Pilih Step A atau B , sesuai kondisi node kalian di posisi mana.

**A. Step untuk master nodenya belum di install**

1. jalankan ``ineryMenu.py``

2. pilih menu ``Master Node Menu``

3. pilih menu ``Install Node``

4. Ikuti peirntah yang muncul

   

**B. Step untuk master node yang sudah jalan**

1. jalankan ``ineryMenu.py``

2. pilih menu ``Wallet Menu``

3. pilih menu ``Create New Wallet``

4. Ikuti perintah yang muncul

   

## Command Buat Munculin Menu

```
ineryMenu.py
```



## Menu Info

**Master Node Menu**

- Install Node ( untuk install node, install node ini langsung jalan ke Part 1B jg)
- Install Part 1B ( Dijalankan kalau misalkan udah Setup Config duluan )
- Restart Node 
- Add new peer
- Setup Config ( Menu buat setup config master node, dari IP, account name dll )

**Wallet Menu**

- Create New Wallet ( buat bikin wallet baru , pastikan kalau bikin wallet lewat sini)
- Unlock Wallet 

**Check Node** untuk check node 

**Task 1 - 3** Automate Task

