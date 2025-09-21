import json
import random
import os

class QuestionBank:
    def __init__(self, json_dir="random"): # 預設搜尋 'random' 資料夾
        self.json_dir = json_dir
        self.question_data = {}
        self.load_all_chapters()

    def load_all_chapters(self):
        """
        載入指定目錄下所有 .json 檔案的題庫。
        """
        print(f"正在嘗試從目錄: '{os.path.abspath(self.json_dir)}' 載入題庫...")
        found_any_chapters = False
        try:
            if not os.path.exists(self.json_dir):
                print(f"錯誤: 找不到指定的資料夾 '{self.json_dir}'。")
                return

            for filename in os.listdir(self.json_dir):
                if filename.endswith(".json"):
                    filepath = os.path.join(self.json_dir, filename)
                    chapter_name = filename.replace(".json", "")
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            if isinstance(data, list):
                                # 確保每個題目都有必需的欄位
                                for q in data:
                                    # 檢查並設置 '解答' 欄位
                                    if '解答' not in q:
                                        print(f"警告: 檔案 '{filename}' 中的題目缺少 '解答' 欄位，已設為 'N/A'。")
                                        q['解答'] = 'N/A' 
                                    # 檢查並設置選項欄位
                                    for i in range(1, 5):
                                        option_key = str(i) # 您的選項鍵名是字串 "1", "2", "3", "4"
                                        if option_key not in q:
                                            print(f"警告: 檔案 '{filename}' 中的題目缺少 '{option_key}' 選項欄位，已設為 'N/A'。")
                                            q[option_key] = 'N/A'
                                        
                                self.question_data[chapter_name] = data
                                print(f"成功載入章節: {chapter_name}")
                                found_any_chapters = True
                            else:
                                print(f"警告: 檔案 '{filename}' 內容不是一個有效的題目列表。")
                    except json.JSONDecodeError:
                        print(f"錯誤: 無法解析 JSON 檔案 '{filepath}'。請檢查 JSON 格式。")
                    except Exception as e:
                        print(f"載入 '{filepath}' 時發生未知錯誤: {e}")
            
            if not found_any_chapters:
                print(f"警告: 在目錄 '{os.path.abspath(self.json_dir)}' 中沒有找到任何有效的 .json 檔案。")
        except FileNotFoundError:
            print(f"錯誤: 找不到指定的目錄 '{self.json_dir}'。")
        except Exception as e:
            print(f"載入題庫時發生未知錯誤: {e}")

    def get_chapter_list(self):
        """回傳所有可用的章節名稱 (來自載入的 JSON 檔名)"""
        return sorted(list(self.question_data.keys()))

    def get_questions_from_chapters(self, chapter_names):
        """
        根據多個章節名稱，取得所有對應的題目列表。
        """
        selected_questions = []
        for name in chapter_names:
            if name in self.question_data:
                selected_questions.extend(self.question_data[name])
            else:
                print(f"警告: 章節 '{name}' 不存在，已跳過。")
        return selected_questions

    def draw_random_questions(self, question_list, num_questions=40):
        """
        從指定的題目列表中隨機抽取不重複的題目。
        """
        if not question_list:
            print("錯誤: 沒有題目可供抽取。")
            return []

        # 確保抽取的數量不會超過題庫總數
        num_questions = min(num_questions, len(question_list))

        if len(question_list) < num_questions:
            print(f"警告: 總題目數量 ({len(question_list)}) 少於要求的抽題數量 ({num_questions})。將抽取所有題目。")
            
        return random.sample(question_list, num_questions)

    def display_question(self, question_data, question_index):
        """
        在終端機中顯示單一題目資訊。
        """
        print(f"\n--- 題目 {question_index + 1} ---")
        print(f"題號: {question_data.get('題號', 'N/A')}")
        print(f"題目: {question_data.get('題目', '無題目內容')}")
        
        # 處理選項，您的選項鍵名是 "1", "2", "3", "4"
        options = {
            '1': question_data.get('1', 'N/A'),
            '2': question_data.get('2', 'N/A'),
            '3': question_data.get('3', 'N/A'),
            '4': question_data.get('4', 'N/A')
        }
        for key, value in options.items():
            print(f"  {key}. {value}")
        print("--------------------")

    def ask_question_and_get_answer(self, question_data, question_index):
        """
        顯示題目並獲取使用者的答案。
        """
        self.display_question(question_data, question_index)
        
        while True:
            user_input = input("請輸入你的答案 (1-4)，或輸入 'skip' 跳過: ").strip().lower()
            if user_input == 'skip':
                return None # 表示跳過
            elif user_input.isdigit() and 1 <= int(user_input) <= 4:
                return int(user_input) # 返回數字
            else:
                print("輸入無效，請輸入 1-4 的數字或 'skip'。")

    def check_answer(self, question_data, user_answer):
        """
        檢查使用者的答案是否正確。
        """
        if user_answer is None:
            return None, False # 跳過不計分

        # 這裡修改為查找 '解答' 欄位，並將其轉為數字
        correct_answer_str = question_data.get('解答', 'N/A') 
        correct_answer_num = None
        try:
            if correct_answer_str and correct_answer_str.isdigit():
                correct_answer_num = int(correct_answer_str)
            else:
                print(f"警告: 題目 '{question_data.get('題號')}' 的 '解答' 欄位 '{correct_answer_str}' 無效，無法進行對答案。")
        except ValueError:
             print(f"警告: 題目 '{question_data.get('題號')}' 的 '解答' 欄位 '{correct_answer_str}' 無法轉換為數字，無法進行對答案。")
             correct_answer_num = None

        if correct_answer_num is None:
            return None, False # 無法核對

        is_correct = (user_answer == correct_answer_num)
        return correct_answer_num, is_correct

# --- 主程式執行區 ---
if __name__ == "__main__":
    # 這裡假設你的 JSON 檔案都在 "random" 資料夾內，且 "隨機練習.py" 與 "random" 資料夾在同一個層級
    # 如果你的檔案結構是 function1/random/ 和 function1/隨機練習.py，則 json_dir="random" 是正確的。
    question_bank = QuestionBank(json_dir="random")  # 指定題庫資料夾為 "random"
    available_chapters = question_bank.get_chapter_list()
    
    if not available_chapters:
        print("錯誤: 未載入任何題庫。請確認 JSON 檔案存在且格式正確，且位於 'random' 資料夾內。")
    else:
        print(f"可用章節: {', '.join(available_chapters)}")

        while True:
            chosen_chapters_input = input(f"\n請輸入想練習的章節名稱 (多個請用逗號隔開, 例如: 3-1,3-2) 或輸入 'quit' 離開: ").strip()

            if chosen_chapters_input.lower() == 'quit':
                break

            # 確保輸入的每個章節名稱都被正確處理
            chosen_chapters = [ch.strip() for ch in chosen_chapters_input.split(',') if ch.strip()]
            
            if not chosen_chapters:
                print("輸入無效，請至少輸入一個有效的章節名稱。")
                continue

            # 驗證每個輸入的章節名稱是否有效
            valid_chapters = [ch for ch in chosen_chapters if ch in available_chapters]
            invalid_chapters = [ch for ch in chosen_chapters if ch not in available_chapters]

            if invalid_chapters:
                print(f"警告: 以下章節名稱不存在，已略過: {', '.join(invalid_chapters)}")
            
            if not valid_chapters:
                print("沒有選擇任何有效的章節。請重新輸入。")
                continue

            # 取得所有選定章節的題目
            all_selected_questions = question_bank.get_questions_from_chapters(valid_chapters)
            
            if not all_selected_questions:
                print("所選章節沒有任何題目。")
                continue
            
            # 隨機抽取題目
            try:
                num_questions_str = input(f"總共有 {len(all_selected_questions)} 題，想練習幾題? (預設 40 題): ").strip()
                if not num_questions_str:
                    num_questions_to_draw = 40
                else:
                    num_questions_to_draw = int(num_questions_str)
                
                if num_questions_to_draw <= 0:
                    print("練習題數必須大於 0。")
                    continue
                
            except ValueError:
                print("輸入無效，請輸入數字。")
                continue

            drawn_questions = question_bank.draw_random_questions(all_selected_questions, num_questions=num_questions_to_draw)

            if drawn_questions:
                # 顯示題目並收集作答
                user_answers_list = question_bank.display_questions_for_practice(drawn_questions)
                
                # 批改答案
                if user_answers_list: # 確保有作答紀錄才進行批改
                    question_bank.check_answers(user_answers_list)
            
            print("\n----------------------------------------") # 分隔每次練習

print("感謝使用，程式結束。")
