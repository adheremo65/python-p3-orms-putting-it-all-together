import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    all = []
    def __init__(self,name,breed):
        self.id = None
        self.name = name
        self.breed = breed
    sssxxxz
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS dogs(
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT
        )
    """
        CURSOR.execute(sql)
    @classmethod
    def drop_table(cls):
        sql = """
    DROP TABLE IF EXISTS dogs
    """
        CURSOR.execute(sql)
    def save(self):
        sql = """
        INSERT INTO dogs(name,breed)
        values(?,?)
        """
        CURSOR.execute(sql,(self.name,self.breed))
        CONN.commit()
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM dogs").fetchone()[0]
    @classmethod
    def create(cls,name,breed):
        dog = cls(name,breed)
        dog.save()
        return dog
    @classmethod
    def new_from_db(cls,row):
        song = cls(row[1],row[2])
        song.id = row[0]
        return song
    @classmethod
    def get_all(cls):
        sql = """
        SELECT * from dogs
    """
    
        all =  CURSOR.execute(sql).fetchall()
        
    
        cls.all = [cls.new_from_db(row)for row in all]
        return cls.all
    @classmethod
    def find_by_name(cls,name):
        sql = """
        SELECT * FROM dogs
        WHERE name = ?
        LIMIT 1

    """
        all = CURSOR.execute(sql,(name,)).fetchone()

        cls.all = cls.new_from_db(all)
        return cls.all
    @classmethod
    def find_by_id(cls,id):
        sql = """
        SELECT * FROM dogs
        WHERE id = ?
    """
        dog = CURSOR.execute(sql,(id,)).fetchone()
        cls.dog = cls.new_from_db(dog)
        return cls.dog
    @classmethod
    def find_or_create_by(cls,name,breed):
        sql = """
        SELECT * FROM dogs 
        WHERE name = ? 
        AND breed = ? 
        """
        dog = CURSOR.execute(sql,(name,breed)).fetchone()
        
        
        if (dog):
             cls.dog = cls.new_from_db(dog)
             return cls.dog
        else:
            sql =   """
            INSERT INTO dogs (name, breed) VALUES (?, ?)"""
            CURSOR.execute(sql, (name, breed))
            CONN.commit()
            dogid = CURSOR.lastrowid
            cls.id = dogid
           
           
      


        
    
