<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI 助教</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&display=swap');
        body {
            font-family: 'Noto Sans TC', sans-serif;
            background-color: #F8F9FA;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .chat-container {
            width: 90%;
            max-width: 600px;
            background-color: #FFFFFF;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            height: 80vh;
        }
        .chat-header {
            background-color: #4CAF50;
            color: #FFFFFF;
            padding: 15px;
            text-align: center;
            font-size: 1.2em;
            font-weight: bold;
        }
        .chat-header span {
            margin-right: 10px;
        }
        .chat-messages {
            flex-grow: 1;
            padding: 20px;
            overflow-y: auto;
        }
        .message {
            margin-bottom: 15px;
            display: flex;
        }
        .message.ai {
            justify-content: flex-start;
        }
        .message.user {
            justify-content: flex-end;
        }
        .message .bubble {
            max-width: 70%;
            padding: 12px 18px;
            border-radius: 20px;
            line-height: 1.4;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        }
        .message.ai .bubble {
            background-color: #E8F5E9;
            color: #333;
            border-bottom-left-radius: 5px;
        }
        .message.user .bubble {
            background-color: #B0E0E6;
            color: #333;
            border-bottom-right-radius: 5px;
        }
        .chat-input {
            display: flex;
            padding: 15px;
            border-top: 1px solid #E0E0E0;
        }
        .chat-input input {
            flex-grow: 1;
            padding: 10px 15px;
            border-radius: 20px;
            border: 1px solid #E0E0E0;
            margin-right: 10px;
        }
        .chat-input button {
            background-color: #4CAF50;
            border: none;
            color: #FFFFFF;
            padding: 10px 15px;
            border-radius: 20px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <span>AI 永續助教 🌱</span>
        </div>
        <div class="chat-messages">
            <div class="message ai">
                <div class="bubble">您好！很高興能為您解答永續相關的學習問題。</div>
            </div>
            <div class="message user">
                <div class="bubble">請問什麼是碳足跡？</div>
            </div>
        </div>
        <div class="chat-input">
            <input type="text" placeholder="輸入你的問題...">
            <button>發送</button>
        </div>
    </div>
</body>
</html>
