Website Link : https://aichat-personas.netlify.app/about
<br>
(Without Backend)
<br>
MULTI PERSONAS AICHAT BOT 
<br>
For Website along with backend, follow these steps :
<hr>
1  Navigate to the project folder<br>
Open your file explorer and go to the folder that contains the project files.<br><br>

2  Open cmd in that folder<br>
Click the location bar, copy the full path, type cmd, and press Enter. A Command Prompt window opens at the project path.<br><br>

3  List currently installed Python packages<br>
bash
Copy
Edit
pip freeze
This command shows all libraries installed in your active Python environment.<br><br>

4  Create a virtual environment<br>
bash
Copy
Edit
python -m venv myenv
If you have multiple Python versions, use the specific interpreter (e.g. python3.11). A new myenv folder appears in the project directory.<br><br>

5  Open a new integrated terminal<br>
In VS Code: Terminal → New Terminal.<br><br>

6  Switch the terminal shell to cmd<br>
Use the shell dropdown (next to the terminal tab), choose Command Prompt (cmd.exe), and close the default PowerShell tab.<br><br>

7  Activate the virtual environment<br>
bash
Copy
Edit
myenv\Scripts\activate
Your prompt now begins with (myenv).<br><br>

8  Change to the sub‑folder that holds the code (if applicable)<br>
bash
Copy
Edit
cd llm-text
<br>
9  Install project dependencies<br>
bash
Copy
Edit
pip install -r requirements.txt
<br>
10  Obtain an API key<br>
Visit https://aistudio.google.com/.<br>

Click Get API key and copy the key.<br><br>

11  Create a .env file to store the key securely<br>
Right‑click inside the llm-text folder → New File → name it .env.<br><br>

12  Add the key to .env<br>
dotenv
Copy
Edit
GOOGLE_API_KEY="YOUR_KEY_HERE"
Save the file.<br><br>

13  Launch NevoxAI<br>
bash
Copy
Edit
streamlit run nevox.py --server.port 7001
Browse to http://localhost:7001, enter your email, and the NevoxAI interface appears.<br><br>

14  Launch VeeVee AI in another terminal<br>
bash
Copy
Edit
streamlit run vv.py --server.port 7002
Open http://localhost:7002 to use VeeVee AI.<br><br>

15  Launch Tillu AI in another terminal<br>
bash
Copy
Edit
streamlit run tillu.py --server.port 7003
Open http://localhost:7003 to use Tillu AI.<br><br>

16  Launch BBG AI in another terminal<br>
bash
Copy
Edit
streamlit run bbg.py --server.port 7004
Open http://localhost:7004 to use BBG AI.<br><br>

17  All set!<br>
All four chatbots are now running concurrently on ports 7001 – 7004. Start chatting and enjoy!<br><br>

Stopping the servers
Press Ctrl +C in each terminal to gracefully shut down any Streamlit instance.

