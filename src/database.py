class User_DB :

    def __init__ (self) :
        self.db = "../info.json"

    def _load_data (self) :
        with open(self.db, "r") as f :
            return json.load(f)

    def _save_user (self, user) :
        with open(self.db, "r") as f :
            json.dump(data, f, indent = 4)

    def _generate_pk (self) :
        data = self._load_data()
        users = data.get("users", [])
        if not users : return 0
        return max(user["pk"] for user in users) + 1
  
    def create (self, name, _id, score = 15) :
        data = self._load_data()
        pk = self._generate_pk()

        for user in data["users"] :
            if user["name"] == name : 
                raise ValueError(f"{name} :: already exist")
            
        data["users"].append({
            "pk" : pk, 
            "name": name,
            "id" : _id,
            "score" : score
            })
        self._save_data(data)

    def read (self, name) :
        data = self._load_data ()
        for user in data["users"] :
            if user["name"] == name :
                print(f"{name} :: {user['id']} :: {user['score']}")
        
    def update (self, name, _id = False, score = False) :
        data = self._load_data ()
        for user in data["users"] :
            if user["name"] == name :
                if (_id) : user["id"] == _id
                if (score) : user["score"] == score
            self._save_data(data)
                
    def destroy (self, name) : 
        data = self._load_data ()
        for user in data["users"] :
            if user["name"] == name :
                data["users"].remove(user)
            self._save_data(data)



def save (user_id, data) :

    file = "../info.csv"
    
    with open(file, mode = "r", encoding = "utf-8") as f :
        reader = csv.reader(f)
        rows = list(reader)

    rows.append(data)

    with open(file, mode = "w", encoding = "utf-8", newline = "") as f :
        writer = csv.writer(f)
        writer.writerows(rows)
