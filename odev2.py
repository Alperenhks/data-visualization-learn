import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = "/Users/alperenharmankasi/Desktop/python-scraping/Bird_strikes.csv"
# 1. Veri Yükleme
data = pd.read_csv(dataset)

# verileri korntrole tme 
print("# Veri kontolleri")
print(data.head())
print(data.describe())
print(data.info())
print("\nVeri Türleri:\n", data.dtypes)  
print("#######################")

# 'Cost' sütununu sayısala çevir
data['Cost'] = pd.to_numeric(data['Cost'].str.replace(r'[^\d.]', '', regex=True), errors='coerce')

# Eksik verileri kontrol et
missing_data = data.isnull().sum()
print("Eksik Veri Sayısı:\n", missing_data)

# Çok fazla eksik veri olan sütunları çıkart
data.drop(['Effect', 'Remarks'], axis=1, inplace=True)

# Kalan eksik verileri sil
data.dropna(inplace=True)

# Sadece sayısal sütunları seç
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# 3. Grafikler


# Çubuk Grafiği: En sık rastlanan 10 WildlifeSpecies
plt.figure(figsize=(10, 6))
wildlife_counts = data['WildlifeSpecies'].value_counts().head(10)
wildlife_counts.plot(kind='bar', color='skyblue')
plt.title('En Sık Görülen 10 Kuş Türü')
plt.xlabel('Kuş Türü')
plt.ylabel('Sayısı')
plt.savefig("3a.png")  
plt.show()

# Pasta Grafiği: Hasar Dağılımı
plt.figure(figsize=(8, 8))
damage_counts = data['Damage'].value_counts()
plt.pie(damage_counts, labels=damage_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Hasar Dağılımı')
plt.savefig("pie.png")  
plt.show()

# Dağılım Grafiği: Altitude ve Cost İlişkisi
plt.figure(figsize=(10, 6))
plt.scatter(data['Altitude'], data['Cost'], alpha=0.5, color='green')
plt.xlabel('İrtifa (Altitude)')
plt.ylabel('Maliyet (Cost)')
plt.title('İrtifa ve Maliyet Arasındaki İlişki')
plt.savefig("3b.png")  
plt.show()

# Korelasyon Isı Haritası (Sadece Sayısal Sütunlar)
plt.figure(figsize=(12, 8))
correlation = numeric_data.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Değişkenler Arası Korelasyon')
plt.savefig("korolasyon.png")  
plt.show()

# Histogram: Cost Dağılımı
plt.figure(figsize=(10, 6))
plt.hist(data['Cost'], bins=30, color='purple', alpha=0.7)
plt.xlabel('Maliyet (Cost)')
plt.ylabel('Frekans')
plt.title('Maliyet Dağılımı')
plt.savefig("3f.png")  
plt.show()

# Çizgi Grafiği: Kayıt ID ve Altitude İlişkisi
plt.figure(figsize=(10, 6))
plt.plot(data['RecordID'], data['Altitude'], label='İrtifa')
plt.xlabel('Kayıt ID')
plt.ylabel('İrtifa (Altitude)')
plt.title('Kayıt ID\'ye Göre İrtifa Değişimi')
plt.legend()
plt.savefig("3g.png")  
plt.show()
