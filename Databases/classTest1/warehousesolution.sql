-- NEO SAHADEO D00264604
-- SETUP FROM THE FILE

CREATE TABLE warehouse_customers (
  CustomerID varchar(5) NOT NULL,
  CustomerName varchar(40),
  Address varchar(60),
  City varchar(15),
  PRIMARY KEY  (CustomerID)
);

INSERT INTO warehouse_customers (CustomerID, CustomerName, Address, City) VALUES
("ADMUR", "Adam Murphy", "72 Canal Street", "Dublin"),
("BITOM", "Bill Tompson", "21 Quay Street", "Dublin"),
("FRMCG", "Frank McGill", "57 Cherry Lane", "Cork"),
("HACLA", "Harry Clarke", "184 High Street", "Limerick"),
("HEONE", "Helen ONeill", "89 Harbour View", "Galway"),
("JAMAL", "Janet Malone", "44 Castle Close", "Kilkenny"),
("SIPHI", "Simon Phillips", "36 Market Street", "Cork"),
("CAKEN", "Cathy Kenny", "35 Oak Lane", "Dublin"),
("PAWIL", "Paula Wilson", "60 River Drive", "Cork"),
("PESIM", "Peter Simpson", "11 Coach Hill", "Dublin"),
("JUMOR", "Julie Morris", "29 Ashtree Park", "Limerick"),
("SATAY", "Sarah Taylor", "77 Lonsdale Road", "Dublin");

CREATE TABLE warehouse_orders (
  OrderID int NOT NULL,
  CustomerID varchar(5),
  OrderDate date,
  PRIMARY KEY  (OrderID),
  FOREIGN KEY (CustomerID) REFERENCES warehouse_customers(CustomerID));

INSERT INTO warehouse_orders (OrderID, CustomerID, OrderDate) VALUES
(1, "ADMUR", "2012-07-26"),
(2, "BITOM", "2012-04-12"),
(3, "FRMCG", "2012-07-01"),
(4, "JAMAL", "2012-09-20"),
(5, "JUMOR", "2012-08-19"),
(6, "SATAY", "2012-10-17");


CREATE TABLE warehouse_products (
  ProductID int NOT NULL,
  ProductName varchar(40),
  UnitPrice decimal(10,2),
  UnitsInStock int,
  ReorderLevel int,
  PRIMARY KEY  (ProductID));

INSERT INTO warehouse_products (ProductID, ProductName, UnitPrice, UnitsInStock, ReorderLevel) VALUES
(1, "Aniseed Syrup", 5.50, 10, 15),
(2, "Cajun Seasoning", 3.60, 82, 50),
(3, "Organic Dried Pears", 1.90, 25, 30),
(4, "Teatime Chocolate", 9.80, 23, 40),
(5, "Boston Crab Meat", 9.10, 8, 20),
(6, "New England Clam Chowder", 8.70, 18, 20),
(7, "Ravioli Angelo", 6.70, 15, 20),
(8, "Hot Pepper Sauce", 2.30, 12, 10),
(9, "Longbreads", 3.30, 30, 40);

---------------------------------------------------------------

-- NEO SAHADEO D00264604


-- Setting up data
-- Warehouse_Order_Details Table (OrderID, ProductID, Quantity)
create table warehouse_order_details (
  OrderID int,
  ProductID int,
  Quantity int,
  FOREIGN KEY (OrderID) REFERENCES warehouse_orders(OrderID),
  FOREIGN KEY (ProductID) REFERENCES warehouse_products(ProductID)
);

insert into warehouse_order_details
values
(1,	1, 2),
(1,	4, 5),
(1,	8, 3),
(2,	2, 3),
(2,	5, 1),
(3,	1, 1),
(4,	2, 3),
(4,	5, 3),
(4,	8, 2),
(4,	9, 1),
(5,	4, 2),
(5,	5, 1),
(6,	2, 3),
(6,	4, 1),
(6,	7, 2);

-- Queries

-- 1. Customers with an address in Dublin
select CustomerName as customername, Address as address from warehouse_customers where City like "%Dublin%";

-- 2. Customers who have placed orders
select
warehouse_customers.CustomerName as customername,
warehouse_orders.OrderDate as orderdate
from warehouse_orders
join warehouse_customers using (CustomerID)
order by OrderDate;

-- 3. Products that have a unit price between €5 and €10
select
ProductName as productname,
UnitPrice as unitprice
from warehouse_products
where UnitPrice > 5 and UnitPrice < 10
order by UnitPrice desc;

-- 4. The number of different products on each order
select distinct
OrderID as orderid,
count(ProductID) as total_products
from warehouse_order_details
group by warehouse_order_details.OrderID
order by total_products;

-- 5. The average product unit price
select round((sum(UnitPrice) / count(UnitPrice)), 2) as average_unit_price
from warehouse_products;

-- 6. Total stock cost for all products
select
ProductName as productname,
(UnitsInStock * UnitPrice) as total_stock_value
from warehouse_products
order by total_stock_value desc;

-- 7. Total order price for Janet Malones order
select
CustomerName as customername,
OrderID as orderid,
sum(Quantity * UnitPrice) as order_total
from warehouse_order_details
join warehouse_products using (ProductID)
join warehouse_orders using (OrderID)
join warehouse_customers using (CustomerID)
where CustomerName = "Janet Malone"
group by CustomerName;

-- 8. Products that were ordered in July
select
warehouse_products.ProductName as productname,
OrderDate as orderdate
from warehouse_order_details
join warehouse_orders using (OrderID)
join warehouse_products using (ProductID)
where OrderDate like "%2012-07%";

-- 9. Products that are low in stock
select
ProductName as productname,
(ReorderLevel - UnitsInStock) as shortfall
from warehouse_products
where (ReorderLevel - UnitsInStock) > 0
order by shortfall desc;

-- 10.
--     • The store has decided to offer a 20% discount on surplus products (where the number in stock is greater than the reorder level)
--
-- Create a select query to show the discount and new unit price for these products
select
ProductName as productname,
UnitPrice as unitprice,
(0.2 * UnitPrice) as discount,
round(UnitPrice - (0.2 * UnitPrice), 2) as new_unit_price
from warehouse_products
where (ReorderLevel - UnitsInStock) < 0
order by new_unit_price desc;
