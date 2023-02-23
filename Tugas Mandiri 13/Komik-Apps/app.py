# melakukan proses import pymongo
import pymongo

# membuat config koneksi untuk menghubungkan mongodb dengan python
koneksi_url = "mongodb://localhost:27017"

# membuat sebuah function yang bertugas untuk mengecek koneksi ke mongodb
def cekMongoDB() :
    client = pymongo.MongoClient(koneksi_url)
    try:
        cek = client.list_database_names()
        print(cek)
    except:
        print("Database Tidak Terhubung")
# cekMongoDB()

# membuat sebuah function yang bertugas untuk create database
def createDatabase() :
    dbClient = pymongo.MongoClient(koneksi_url)
    namaDatabase = dbClient['Database_komik']
    namaCollection = namaDatabase['Komik']
    nilai_data = namaCollection.insert_one({ 'nama': "Detective Conan", 'pengarang': "Gosho Aoyama", 'harga' : 40000 })

    return nilai_data
# createDatabase()


class MongoCRUD:
    def __init__(self, data, koneksi):
        self.client = pymongo.MongoClient(koneksi)
        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def bacaData(self):
        documents = self.collection.find()
        value = [{
            item: data[item] for item in data if item != '_id'} for data in documents]
        return value


if __name__ == '__main__' :
    data = {
        "database" : "Database_komik",
        "collection" : "Komik"
    }

    mongo_objek = MongoCRUD(data, koneksi_url)
    baca_data = mongo_objek.bacaData()
    print(baca_data)
