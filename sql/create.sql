create table vendas (
id serial primary key,
email varchar(255) not null,
data timestamp not null,
valor numeric(10,2) not null check (valor >= 0),
quantidade integer not null check (quantidade >= 0),
produto varchar(255) not null,
categoria varchar(50) not null
);