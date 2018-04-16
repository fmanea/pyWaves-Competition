# pyWaves-Competition

## Competition rules:
Steps of the Quest:
1. Please, PROVIDE THE ADDRESS OF YOUR WAVES WALLET IN YOUR REPLY TO THIS MESSAGE and get token ALAN in 2 minutes

2. Connect to Waves Telegram bot @wavesbalancebot to receive another token JOHN

3. Receive the rest of the tokens (VLAD, ZIGM, YURI) via airdrops during 12-16 April (the tokens will be airdroped  to all Waves wallets out there)

4. Send all five tokens simultaneously to a special public address: 3PG3JmVh1czUhvg8stVwFY8zXkqVJBqeeJw

## Installing Pywaves:

```pip install pywaves```

### Running project:

Modify pyWavesWalletCheckSend.py with your private key, in this line:
```myAddress = pw.Address(privateKey='4EQByDHFnC7AmeqYxstC4bh52j9ZkTpkEpxh65YjM5F7')```
Run this scrip to endlessly check the wallet for the required tokens:
```bash +x runLoop.sh```