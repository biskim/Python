"""
날짜 : 2022/01/13
이름 : 김병현
내용 : 파이썬 데이터베이스 프로그램 교재 p295
"""
import pymysql

# 데이터베이스 접속

conn = pymysql.connect(host='54.180.160.240',
                       user='kimbhun123',
                       password='1234',
                       db='kimbhun123',
                       charset='utf8')

# SQL 실행 객체 생성(Corsor)
cur = conn.cursor()


# SQL 실행
sql = "UPDATE `User1` SET `age` = `age` + 1 WHERE `uid` = 'P101';";
cur.execute(sql)
conn.commit()


# 데이터 베이스 종료
conn.close()

print('Update 완료...')
