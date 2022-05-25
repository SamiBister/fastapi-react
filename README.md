# fastapi-react

## Front-end first time

```bash
sudo su
npx create-react-app frontend
frontend/
npm start
```

## Front end after devcontainer start

```bash
npm install
npm start

```


docker run \
 --rm \
 --volume "$PWD/test-robot":/home/robot/tests \
 --volume "$PWD/results":/home/robot/results \
 robotframework/rfdocker:latest \
 tests

google-chrome-stable  --headless --disable-gpu --remote-debugging-port=4444 https://chromestatus.com
