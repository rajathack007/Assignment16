#1.create table
import pymysql as py

db=py.connect("localhost","root","unknown@123","Book")

book="create table book(book_id int,title char(20),location char(20),genre char(20))"

titles="create table titles(title_id int,title char(20),ISBN char(20),publisher_id int,publication_year int)"

publishers="create table publishers(publisher_id int,name char(20),street_add char(20),suit_number int,zip_code_id int)"

zip_code="create table zip_code(zip_code_id int,city char(20),state char(20),zip_code int)"

auther_titles="create table auther_titles(auther_title_id int,aurther_id int,title_id int)"

authors="create table authors(author_id int,first_name char(20),middle_name char(20),last_name char(20))"

cursor=db.cursor()

cursor.execute("drop table book")

cursor.execute("drop table titles")

cursor.execute("drop table publishers")

cursor.execute("drop table zip_code")

cursor.execute("drop table auther_titles")

cursor.execute("drop table authors")

print(cursor.execute("show tables"))

cursor.execute(book)

cursor.execute(titles)

cursor.execute(publishers)

cursor.execute(zip_code)

cursor.execute(auther_titles)

cursor.execute(authors)

print(cursor.execute("show tables"))

db.close()






#2.insert table
import pymysql as py

db=py.connect("localhost","root","unknown@123","Book")
cursor=db.cursor()

cursor.execute("insert into book values(001,'life of cricket','india','fiction')")
cursor.execute("insert into titles values(001,'life of cicket','1001',101,2005)")
cursor.execute("insert into publishers values(001,'abc','mumabai',10002,11001)")
cursor.execute("insert into zip_code values(001,'ara','bihar',802152)")
cursor.execute("insert into auther_titles values(001,10010,1012012)")
cursor.execute("insert into authors values(001,'rhoit','null','red')")
cursor.execute("select * from book")
result=cursor.fetchall()
print(result)
db.commit()





#3.import pymysql as py

db=py.connect("localhost","root","unknown@123","library")
cursor=db.cursor()
cursor.execute("select * from book")
result=cursor.fetchall()
print(result)
cursor.execute("update book set genre='love story' where book_id=101")
cursor.execute("select * from book")
result=cursor.fetchall()
print(result)
db.commit()
db.close()
