from exam_core import ExamCore

def start_mock_exam_session():
    """模擬一個完整的考試流程，包含作答與報告"""
    
    # 初始化核心邏輯
    exam_core = ExamCore() # 如果這裡沒有指定檔案名，會使用 ExamCore 預設的 '114questions.json'
    user_id = "user_001"
    
    print("===== 歡迎使用模擬考練習模式！=====")
    
    # 1. 產生考卷
    exam_questions = exam_core.generate_exam(num_questions=3)
    if not exam_questions:
        print("無法產生考卷，請檢查題庫檔案或其內容結構。") # 提示訊息更明確
        return
        
    user_answers = {}
    
    # 2. 顯示題目並收集答案
    for i, q in enumerate(exam_questions, 1):
        print(f"\n--- 第 {i} 題 ---")
        print(f"題目：{q['題目']}") # <-- HERE: 這裡改成 '題目'
        
        # 顯示選項 A, B, C, D
        options_map = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
        print(f"A. {q['A']}")
        print(f"B. {q['B']}")
        print(f"C. {q['C']}")
        print(f"D. {q['D']}")
        
        try:
            user_input_str = input("請輸入你的答案（例如：1代表A, 2代表B, 3代表C, 4代表D）：")
            user_input = int(user_input_str)
            selected_option = options_map.get(user_input) 
            
            if selected_option:
                user_answers[q['題號']] = selected_option # <-- HERE: 使用 '題號' 作為鍵
            else:
                print("無效的輸入，請輸入 1, 2, 3 或 4。本題將視為答錯。")
                user_answers[q['題號']] = "" 
        except ValueError: # 只捕獲 ValueError，因為索引錯誤不會發生
            print("無效的輸入，請輸入一個數字（1-4）。本題將視為答錯。")
            user_answers[q['題號']] = "" 
            
    # 3. 批改考卷與儲存錯題
    print("\n===== 模擬考結束，正在為你評分... =====")
    report = exam_core.grade_exam(user_answers, exam_questions)
    exam_core.save_incorrect_questions(user_id, report['incorrect_questions'])
    
    # 4. 顯示報告
    print("\n===== 你的模擬考報告 =====")
    print(f"總題數：{report['total_questions']}")
    print(f"答對題數：{report['correct_count']}")
    print(f"你的得分：{report['score']} 分")
    
    if report['incorrect_questions']:
        print("\n--- 你的錯題列表 ---")
        for q in report['incorrect_questions']:
            print(f"題號：{q['題號']}") # <-- HERE: 顯示錯題的 '題號'
            print(f"題目：{q['題目']}") # <-- HERE: 顯示錯題的 '題目'
            print(f"正確答案：{q['答案']}") # <-- HERE: 顯示錯題的 '答案'
            print("---")
            
    print("\n===============================")
    
    # 5. 範例：顯示錯題庫題目
    print("\n===== 從錯題庫中提取題目來練習 =====")
    incorrect_list = exam_core.get_incorrect_questions(user_id)
    if incorrect_list:
        print(f"你目前的錯題庫裡共有 {len(incorrect_list)} 題。")
        # 這裡也可以選擇遍歷並顯示錯題庫的題目
        # for q in incorrect_list:
        #     print(f"錯題：{q['題目']} (答案：{q['答案']})")
    else:
        print("恭喜！你目前沒有任何錯題。")


if __name__ == "__main__":
    start_mock_exam_session()
