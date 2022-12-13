# Whisper-GPT
This is a program built to build a closed loop where, user can chat with chatgpt using voice using OpenAI's whisper <br>

## Setup:

1) use requirements.txt file to install dependencies
2) Enter your OpenAI credentials in `testgpt.py` <br>  ``Not Working after the recent cloudflare update``

![image](https://user-images.githubusercontent.com/48201939/206890929-4f77219f-7089-454b-bceb-eb04c3afef42.png)

3) ` Use the below steps `
   * First upgrade the revchat gpt <br> 
   `pip3 install revChatGPT==0.0.a42`
   
   * Then change the config as below  to enter your session token <br>
      - `This requires chrome browser`
      
<br>
![image](https://user-images.githubusercontent.com/48201939/207210877-a177603f-e96f-4645-a026-28e7003d4b89.png)
<br>

## Code Run:
1) Run the code from `speakwithchatGPT.py` <br> <br>
![image](https://user-images.githubusercontent.com/48201939/206890429-a6583e75-8a83-462b-a529-79d76ae48161.png)
2) Choose the option <br> <br>
![image](https://user-images.githubusercontent.com/48201939/206890476-0e8d5671-5139-498b-b9b8-3202792f1eff.png)


## To-Do's
- [ ] Add option for T.T.S. probably pyttsx3
- [ ] Create an executable file, for easy sharing
- [ ] Take yes/no through voice for continued response
- [ ] Clean up the codespace

I would like to thank the brilliant work from OpenAI and also [acheong08](https://github.com/acheong08), without whose work this would have been impossible <br>
1) [Whisper](https://github.com/openai/whisper)
2) [revChatGPT](https://github.com/acheong08/ChatGPT)

