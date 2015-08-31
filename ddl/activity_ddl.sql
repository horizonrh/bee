CREATE TABLE activity(
	id int(32),
	publisher int(32),
	group_id int(32),
	gmt_start timestamp,
	gmt_end timestamp,
	gmt_create timestamp,
	status int(8),
	description varchar(1024),
	title varchar(256)
);