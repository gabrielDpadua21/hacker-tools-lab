# Hacker Tools Lab

v 0.1.1
---

<div align="center">
    <img src="./image/tool.jpeg" width="100%">
</div>

this project was created to facilitate hacking and pentesting studies

---

## To run kali linux in docker container

Requirements
- Docker
- Docker compose

## Build a kali lab image

```
cd kali && docker build -t kali-lab .
```

## Running kali linux

```
docker-compose up -d && docker-compose exec kali-docker bash
```

The tools path is mapping in the volume inside the container

---

## Alias do running anywhere

bashrc

```
echo "alias kali='docker-compose -f $HOME/hacker-tools/docker-compose.yml up -d kali-docker && docker-compose -f $HOME/hacker-tools/docker-compose.yml exec kali-docker bash'" >> .bashrc && source .bashrc
```

zshrc
```
echo "alias kali='docker-compose -f $HOME/hacker-tools/docker-compose.yml up -d kali-docker && docker-compose -f $HOME/hacker-tools/docker-compose.yml exec kali-docker bash'" >> .zshrc && source .zshrc
```

---

### Send me an E-mail
<a href="mailto:gabriel.d.padua21@gmail.com"><img src="https://slackmojis.com/emojis/870-mail/download" width="33px"></a>

#### License

Copyright © 2021, [Gabriel D. Padua](https://github.com/gabrielDpadua21).
Released under the [MIT license](LICENSE).