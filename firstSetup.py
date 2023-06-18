import mysql.connector as ms
conn = ms.connect(host="localhost",user="root",passwd="1234",database="users")
cur = conn.cursor()
cur.execute("create table basic_details ( userid char(50),	username char(50),	passwd	char(50) )")
conn.commit()
cur.execute("insert into basic_details values(0,'null','null')")
conn.commit()
cur.execute("create table personal_details ( userid char(50),  firstname char(50),     lastname char(50),     dob char(20),     email char(100),     phno char(20),     gender char(20) )")
conn.commit()
cur.execute("create table address ( userid char(50),	houseno char(50),	street	char(50),	city char(50),	pincode int(6),	state char(50) )")
conn.commit()
cur.execute("create table trains ( trainno int(5),  trainname char(50),     starts char(50),     ends char(50),     firstac int(7),     secondac int(7),     sleeper int(7),	time char(20) )")
conn.commit()
cur.execute("insert into trains values('12681', 'Coimbatore Express', 'Chennai Central', 'Coimbatore Junction', '4000', '2500', '1000', '5 Hours')")
conn.commit()
cur.execute("insert into trains values('19409', 'Gorakhpur Express', 'Ahmedabad Junction', 'Gorakhpur Junction', '5000', '3000', '1500', '1 Day')")
conn.commit()
cur.execute("insert into trains values('12869', 'Howrah Superfast Express', 'Mumbai Cst', 'Howrah Junction', '6000', '3500', '2000', '2 Days')")
conn.commit()
cur.execute("insert into trains values('11125', 'Ind Gwaliar Express', 'Indore Junction Bg', 'Gwalior', '4700', '2700', '900', '10 Hours')")
conn.commit()
cur.execute("insert into trains values('12425', 'Jammu Rajdhani', 'New Delhi', 'Jammu Tawi', '5300', '3000', '950', '10 Hours')")
conn.commit()
conn.close()