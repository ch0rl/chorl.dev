create table access_log (
    id bigserial primary key,
    path varchar,
    ip varchar,
    stamp timestamp,
    user_agent varchar,
    id_got varchar,
    id_set varchar,
    status int,
    forwarded_for varchar,
    referrer varchar
);