import json
import random

class ExamCore:
    def __init__(self, questions_file='114+113questions.json', incorrect_file='incorrect_questions.json'):
        self.questions_file = questions_file
        self.incorrect_file = incorrect_file
        
    def _load_data(self, file_path):
        """通用函式：載入 JSON 檔案資料"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # 如果檔案不存在或格式錯誤，對於 questions_file 返回空字典，對於 incorrect_file 返回空字典
            # 這樣 generate_exam 才能從空字典中嘗試 .get()
            return {}

    def _save_data(self, data, file_path):
        """通用函式：儲存資料到 JSON 檔案"""
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def generate_exam(self, num_questions=3):
        """生成一份模擬考卷，從 JSON 檔案的特定屬性中提取題目列表"""
        full_json_content = self._load_data(self.questions_file) # 載入整個 JSON 物件
        
        # 假設您的題目列表位於 '114(1)' 這個鍵之下
        all_questions = full_json_content.get("114(1)", []) 
        
        if not all_questions:
            print("無法從 JSON 檔案的 '114(1)' 屬性中找到題目列表，請檢查 114questions.json 檔案結構。")
            return []
        
        # 額外檢查確保 all_questions 確實是列表
        if not isinstance(all_questions, list):
            print(f"錯誤: 載入的 '114(1)' 屬性不是一個列表，而是 {type(all_questions)}。")
            return []
            
        # 隨機選取指定數量的題目
        # 確保要選取的題目數量不超過總題目數
        num_to_sample = min(num_questions, len(all_questions))
        if num_to_sample == 0:
            return [] # 如果沒有題目可以選，返回空列表

        exam_questions = random.sample(all_questions, num_to_sample)
        return exam_questions

    def grade_exam(self, user_answers, exam_questions):
        """批改考卷並生成報告"""
        correct_count = 0
        incorrect_questions = []

        for question in exam_questions:
            # 注意這裡的 ID 是 '題號'
            question_id = question['題號'] 
            # 比較答案時，您的題目檔案中的正確答案鍵是 '答案'
            # 並且題目選項是 A, B, C, D
            # 需要將用戶輸入的選項（例如 'A'）與題目檔案中的正確答案進行比較
            
            # 假設 user_answers 的鍵是題號，值是使用者選擇的選項 (例如 'A', 'B', 'C', 'D')
            if user_answers.get(question_id) == question['答案']:
                correct_count += 1
            else:
                incorrect_questions.append(question)
        
        total_questions = len(exam_questions)
        score = (correct_count / total_questions) * 100 if total_questions > 0 else 0
        
        report = {
            "score": round(score, 2),
            "total_questions": total_questions,
            "correct_count": correct_count,
            "incorrect_questions": incorrect_questions
        }
        return report

    def save_incorrect_questions(self, user_id, incorrect_questions):
        """將答錯的題目儲存到錯題庫"""
        if not incorrect_questions:
            return
        
        data = self._load_data(self.incorrect_file)
        # 確保 data 是一個字典，以防 incorrect_questions.json 檔案有誤
        if not isinstance(data, dict):
            data = {}
            
        if user_id not in data:
            data[user_id] = []
        
        # 使用 '題號' 作為判斷題目是否已存在的依據
        existing_ids = {q['題號'] for q in data[user_id]}
        new_items = [q for q in incorrect_questions if q['題號'] not in existing_ids]
        data[user_id].extend(new_items)
        
        self._save_data(data, self.incorrect_file)

    def get_incorrect_questions(self, user_id):
        """取得指定使用者的錯題"""
        data = self._load_data(self.incorrect_file)
        # 確保 data 是一個字典
        if not isinstance(data, dict):
            return []
        return data.get(user_id, [])
