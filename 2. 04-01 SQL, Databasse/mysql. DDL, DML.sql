-- 데이터 베이스 만들기
create table kickborad(
    member_id VARCHAR(16),
    member_name VARCHAR(16),
    kickboard VARCHAR(16),
    kickboard_brand VARCHAR(16),
    rental_location VARCHAR(32),
    rental_date DATETIME,
    distance INT,
    price INT
);

desc kickborad;

-- 데이터 삽입하기
INSERT INTO kickboard
VALUES ('kmax6', '김민준', '7YWC', 'boardkick','서울시 관악구 신림동','2020-05-14 12:01:55',354,4700);


-- PK 설정
-- PK 설정을 안해주면 NOT NULL, UNIQUE를 설정한 컬럼을 자동을로 PK 로 설정
-- 반대로 PK 설정시 자동을로 NOT NULL, UNIQUE 설정됨
CREATE TABLE kickboard(
    member_id       VARCHAR(16)  NOT NULL UNIQUE,
    member_name     VARCHAR(16)  NOT NULL,
    member_birthday DATE,
    id              VARCHAR(16) PRIMARY KEY
    price int);

desc kickboard;

-- 제약조건 추가1
ALTER TABLE kickboard
ADD CONSTRAINT member_id UNIQUE (member_id);
-- 제약조건 추가2
ALTER TABLE kickboard
ALTER price SET DEFAULT 1000;
-- 제약조건 삭제
ALTER TABLE kickboard DROP CONSTRAINT rental_time_check;


-- 외래키 설정하기
CREATE TABLE borrow(
    customer_number VARCHAR(10),
    rental_time DATETIME,
    kickboard_id VARCHAR(10),
    member_id  VARCHAR(16)  NOT NULL UNIQUE,
    CONSTRAINT borrow_pk PRIMARY KEY (customer_number, rental_time),
    FOREIGN KEY (customer_number) REFERENCES customer(customer_number),
    FOREIGN KEY (kickboard_id) REFERENCES kickboard(id)
);
