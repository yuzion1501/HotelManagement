/****************** Tạo database *********************/
CREATE DATABASE HotelManagement;
go
use HotelManagement
go

/****************** Tạo bảng *********************/
create table Guest (
	name nvarchar(30) ,
	email nvarchar(30),
	phone char(10) primary key,
	id_card char(12),
)

create table Reservation(
	id char(20) primary key,
	phone char(10) ,
	room_id char(5),
	status varchar(20),
	booking_date date,
	date_sent date,
	duration int,
	number_of_guests int,
)



create table Room (
	room_id char(5) primary key,
	room_type char(1),
	price int,
	available char(5),
)


create table Bill(
	id char(20) primary key,
	charge int ,
	addition float,
	foreigner_addition float,
	compensation int,
	total int,
)

insert into Room (room_id,room_type,price,available)
values ('A1','A',150000,'Yes')
insert into Room (room_id,room_type,price,available)
values ('A2','A',150000,'Yes')
insert into Room (room_id,room_type,price,available)
values ('B1','B',170000,'Yes')
insert into Room (room_id,room_type,price,available)
values ('A1','A',200000,'Yes')






