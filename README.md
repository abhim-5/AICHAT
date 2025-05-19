Website Link : https://aichat-personas.netlify.app/about
(Without Backend)
<br>
MULTI PERSONAS AICHAT BOT 
<br>
🚀 For Website along with backend, follow these steps :
<hr>
1  📂 Navigate to the project folder<br>
Open your file explorer and browse to the folder that contains the project files. <br><br>

2  🖥️ Open cmd in that folder<br>
Click the location bar, copy the full path, type “cmd”, and press Enter. A Command Prompt window opens at the project path. <br><br>

3  🔍 List currently installed Python packages<br>
Type pip freeze to see all libraries installed in your active Python environment. <br><br>

4  🐍 Create a virtual environment<br>
Type python -m venv myenv (replace python with the desired interpreter if you have multiple versions). A new folder named myenv appears in the project directory. <br><br>

5  🆕 Open a new integrated terminal<br>
In VS Code choose Terminal → New Terminal. <br><br>

6  🔄 Switch the terminal shell to cmd<br>
Use the shell dropdown next to the terminal tab, choose Command Prompt (cmd.exe), and close the default PowerShell tab. <br><br>

7  ⚡ Activate the virtual environment<br>
Type myenv\Scripts\activate. Your prompt now begins with (myenv). <br><br>

8  📁 Change to the code folder (if applicable)<br>
Type cd llm-text to move into the main project folder. <br><br>

9  📦 Install project dependencies<br>
Type pip install -r requirements.txt to install everything listed in requirements.txt. <br><br>

10  🔑 Obtain an API key<br>
Visit https://aistudio.google.com, click Get API key, and copy the key value. <br><br>

11  🗄️ Create a .env file to store the key securely<br>
Inside the llm-text folder, create a new file named .env. <br><br>

12  ✏️ Add the key to .env<br>
Open .env and add this line (replace the placeholder with your key): <br>
GOOGLE_API_KEY="YOUR_KEY_HERE"<br>
Save the file. <br><br>

13  🤖 Launch NevoxAI<br>
Type streamlit run nevox.py --server.port 7001. Then open http://localhost:7001 in your browser and enter your email to access NevoxAI. <br><br>

14  🤖 Launch VeeVee AI in another terminal<br>
Open a second terminal, activate the virtual environment if needed, and type streamlit run vv.py --server.port 7002. Open http://localhost:7002 to use VeeVee AI. <br><br>

15  🤖 Launch Tillu AI in another terminal<br>
Open a third terminal, activate the environment, and type streamlit run tillu.py --server.port 7003. Open http://localhost:7003 to use Tillu AI. <br><br>

16  🤖 Launch BBG AI in another terminal<br>
Open a fourth terminal, activate the environment, and type streamlit run bbg.py --server.port 7004. Open http://localhost:7004 to use BBG AI. <br><br>

17  ✅ All set!<br>
All four chatbots are now running concurrently on ports 7001 – 7004. Start chatting and enjoy! 🎉<br><br>

⏹️ Stopping the servers<br>
Press Ctrl +C in each terminal to gracefully shut down any Streamlit instance. <br>
