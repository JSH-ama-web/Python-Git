class PromptManager:
    def __init__(self):
        # 프로그램 실행 중에만 유지되는 메모리 저장소 (딕셔너리 리스트)
        self.prompts = []
        self.next_id = 1

    def display_menu(self):
        print("\n=== 📝 프롬프트 관리 프로그램 ===")
        print("1. 프롬프트 추가")
        print("2. 전체 목록 보기")
        print("3. 카테고리별 조회")
        print("4. 프롬프트 검색 (제목/내용)")
        print("5. 상세 보기 및 즐겨찾기 설정")
        print("6. 즐겨찾기 모아보기")
        print("0. 프로그램 종료")
        print("===============================")

    def add_prompt(self):
        print("\n[1. 프롬프트 추가]")
        title = input("제목을 입력하세요: ")
        category = input("카테고리를 입력하세요: ")
        content = input("프롬프트 내용을 입력하세요: ")
        
        new_prompt = {
            "id": self.next_id,
            "title": title,
            "category": category,
            "content": content,
            "is_favorite": False
        }
        self.prompts.append(new_prompt)
        self.next_id += 1
        print(f"✅ '{title}' 프롬프트가 추가되었습니다.")

    def view_list(self, prompts_to_show=None):
        target_prompts = prompts_to_show if prompts_to_show is not None else self.prompts
        
        if not target_prompts:
            print("\n등록된 프롬프트가 없습니다.")
            return

        print("\n[프롬프트 목록]")
        for p in target_prompts:
            fav_mark = "⭐" if p["is_favorite"] else "☆"
            print(f"ID: {p['id']} | {fav_mark} | [{p['category']}] {p['title']}")

    def view_by_category(self):
        print("\n[3. 카테고리별 조회]")
        category_to_find = input("조회할 카테고리를 입력하세요: ")
        filtered = [p for p in self.prompts if p["category"] == category_to_find]
        self.view_list(filtered)

    def search_prompts(self):
        print("\n[4. 프롬프트 검색]")
        keyword = input("검색어를 입력하세요: ")
        filtered = [p for p in self.prompts if keyword in p["title"] or keyword in p["content"]]
        self.view_list(filtered)

    def view_detail_and_favorite(self):
        print("\n[5. 상세 보기 및 즐겨찾기 설정]")
        try:
            target_id = int(input("상세보기할 프롬프트 ID를 입력하세요: "))
            prompt = next((p for p in self.prompts if p["id"] == target_id), None)
            
            if prompt:
                print("\n--- 프롬프트 상세 ---")
                print(f"제목: {prompt['title']}")
                print(f"카테고리: {prompt['category']}")
                print(f"즐겨찾기: {'⭐ 설정됨' if prompt['is_favorite'] else '☆ 해제됨'}")
                print(f"내용:\n{prompt['content']}")
                print("---------------------")
                
                toggle = input("즐겨찾기 상태를 변경하시겠습니까? (y/n): ")
                if toggle.lower() == 'y':
                    prompt['is_favorite'] = not prompt['is_favorite']
                    print("✅ 즐겨찾기 상태가 변경되었습니다.")
            else:
                print("❌ 해당 ID의 프롬프트를 찾을 수 없습니다.")
        except ValueError:
            print("❌ 올바른 숫자 ID를 입력해주세요.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("원하는 기능의 번호를 입력하세요: ")
            
            if choice == '1':
                self.add_prompt()
            elif choice == '2':
                print("\n[2. 전체 목록 보기]")
                self.view_list()
            elif choice == '3':
                self.view_by_category()
            elif choice == '4':
                self.search_prompts()
            elif choice == '5':
                self.view_detail_and_favorite()
            elif choice == '6':
                print("\n[6. 즐겨찾기 모아보기]")
                filtered = [p for p in self.prompts if p["is_favorite"]]
                self.view_list(filtered)
            elif choice == '0':
                print("프로그램을 종료합니다. (데이터 초기화됨)")
                break
            else:
                print("❌ 잘못된 입력입니다. 메뉴에 있는 번호를 입력해주세요.")

if __name__ == "__main__":
    app = PromptManager()
    app.run()
