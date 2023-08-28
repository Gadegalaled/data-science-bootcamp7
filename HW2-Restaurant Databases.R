.open restaurant.db
  
drop table menu;
drop table order;
drop table beverage;
drop table bev_order;

-- table 1 menu;
create table menu (
  id int unique,
  menu_name text,
  price int
);
insert into menu values
  (1, 'salad', 80),
  (2, 'Fish and chips', 160),
  (3, 'steake', 120),
  (4, 'Spaghetti Carbonara', 99),
  (5, 'Fried Rice', 80),
  (6, 'Beef Burger', 150);


-- table 2 order;
create table orders (
  order_id int,
  amount int
);
insert into order values 
  (1, 2),
  (3, 1);

-- table 3 beverages;
create table beverage (
  bev_id int unique,
  bev_name text,
  bev_price int
);
insert into beverage values
  (1, 'water', 25),
  (2, 'coke', 40),
  (3, 'Banana Milkshake', 79),
  (4, 'Beer', 69);

-- table 4 bev_orders;
create table bev_orders (
  bev_or_id int,
  bev_amount int
);
insert into bev_order values
  (2, 3),
  (3, 2),
  (4, 3);

.mode box
.head on 

-- query 
select * from menu;
select * from beverage;
select * from bev_order;

-- subqury
select * from (select * from order);

-- join table
select * from menus
  join orders on menus.id = orders.order_id;

-- WITH (common expressions)
with sub as (select m.id as al_or_id, m.price*o.amount as total
  from menus as m
  join orders as o on m.id = o.order_id)
select al_or_id, total from sub;

-- subquery + aggregate function
select min(total), max(total) from (select m.id as al_or_id, m.price*o.amount as total
  from menus as m
  join orders as o on m.id = o.order_id);

-- where clause
select b.bev_name ,b.bev_price*b_o.bev_amount as bev_bill   from beverage as b, bev_orders as b_o
  where b.bev_id = b_o.bev_or_id;
