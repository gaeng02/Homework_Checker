import os

# Create / Read / Update / Delete

# file
class User :

    def __init__ (self, name, extension = "csv", base = "../data/") :
        self.name = name
        self.file = base + name + "." + extension
        
    def Create (self) :

        if (os.path.exists(self.file)) :
            print("Already exist")
            return ;
        
        with open (self.file, mode = "w", newline = "", encoding = "utf-8") as f : 
            print("Create")

    def Read (self) :

        if (os.path.exists(self.file)) :
            with open (self.file, mode = "r", encoding = "utf-8") as f :
                content = f.read()
                print(content)
                
        else :
            print("No file")
        
    def Delete (self) :

        try :
            os.remove(self.file)
            print("Delete")
            del self
            
        except FileNotFoundError :
            print(f"{self.file} 파일이 존재하지 않습니다.")
            
        except Exception as e : 
            print(f"파일 삭제 중 오류 발생: {e}")

