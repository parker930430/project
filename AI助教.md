<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>登入 - 永續學習</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&display=swap');
        
        body {
            font-family: 'Noto Sans TC', sans-serif;
            background: linear-gradient(180deg, rgba(76, 175, 80, 0.1) 0%, #FFFFFF 100%);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            color: #333;
        }
        .login-container {
            text-align: center;
            padding: 40px;
            background-color: #FFFFFF;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
            width: 90%;
            max-width: 400px;
        }
        .logo {
            font-size: 3em;
            color: #4CAF50;
            margin-bottom: 20px;
        }
        h1 {
            font-size: 1.8em;
            margin-bottom: 30px;
            color: #2E7D32;
        }
        .input-group {
            margin-bottom: 20px;
        }
        .input-group input {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            font-size: 1em;
            box-sizing: border-box;
        }
        .input-group input::placeholder {
            color: #A0A0A0;
        }
        .login-btn {
            width: 100%;
            padding: 15px;
            border: none;
            border-radius: 8px;
            background-color: #4CAF50;
            color: #FFFFFF;
            font-size: 1.1em;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .login-btn:hover {
            background-color: #2E7D32;
        }
        .slogan {
            margin-top: 40px;
            color: #888;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="logo">📖🌱</div>
        <h1>永續學習平台</h1>
        <div class="input-group">
            <input type="text" placeholder="使用者名稱">
        </div>
        <div class="input-group">
            <input type="password" placeholder="密碼">
        </div>
        <button class="login-btn">登入</button>
    </div>
    <p class="slogan">永續學習，從今天開始 🌱</p>
</body>
</html>
