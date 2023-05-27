###Simple Queries.

#1.0 Display count of rows in bookings, members and facilities
SELECT COUNT(*) AS row_in_booking FROM cd.bookings;
SELECT COUNT(*) AS rows_in_members FROM cd.members;
SELECT COUNT(*) AS rows_in_facilities FROM cd.facilities;

#2.0 Display bookings in descending sorted order of data
SELECT * FROM cd.bookings ORDER BY bookid DESC;

#3.0 Display distinct facilities
SELECT DISTINCT facilities FROM cd.facilities;

#4.0 Get top 3 facilities with highest member cost
SELECT facilities, membercost
FROM cd.facilities
ORDER BY membercost DESC
LIMIT 3;


#5.0 Get top 1 facilities with least montly maintenance
SELECT name, monthlymaintenance
FROM cd.facilities
ORDER BY monthlymaintenance
LIMIT 1;

#6.0 Get members who share same surname.
SELECT DISTINCT m1.firstname, m1.surname
FROM cd.members m1
JOIN cd.members m2 ON m1.surname = m2.surname AND m1.memid <> m2.memid
ORDER BY m1.surname, m1.firstname;

##7.0 Get members who stay in same City. If they have Boston in Address then they are in same city.
SELECT address_parts.city, array_agg(CONCAT(m.firstname, ' ', m.surname)) AS members
FROM (
  SELECT DISTINCT ON (address) address, split_part(address, ', ', 2) AS city
  FROM cd.members
) AS address_parts
JOIN cd.members m ON address_parts.address = m.address
GROUP BY address_parts.city
ORDER BY address_parts.city;


##8.0 Get members whos surname starts with 'Sm' or 'Tr' or ends with "ll" or "ew"
SELECT firstname, surname
FROM cd.members
WHERE surname LIKE 'Sm%' OR surname LIKE 'Tr%' OR surname LIKE '%ll' OR surname LIKE '%ew'
ORDER BY surname, firstname;



###join Queries###
##1.0 Display members who have booked facilities
SELECT DISTINCT c.firstname, c.surname
FROM cd.members c
JOIN cd.bookings b ON c.memid = b.memid
ORDER BY c.surname, c.firstname;


##2.0 Display facilities that have been booked.
SELECT DISTINCT f.name
FROM cd.facilities f
JOIN cd.bookings b ON f.facid = b.facid
ORDER BY f.name;

##3.0 Display members who have not booked facilities.
SELECT firstname, surname
FROM cd.members
WHERE memid NOT IN (SELECT DISTINCT memid FROM cd.bookings)
ORDER BY surname, firstname;

##4.0 Display facilities that have not been booked by members.
select name as facility
from cd.facilities
where facid not in (select facid from cd.bookings)
order by name;

##5.0 Display bookings with no facilities and members.
SELECT *
FROM cd.bookings
WHERE facid NOT IN (SELECT facid FROM cd.facilities)
   OR memid NOT IN (SELECT memid FROM cd.members);


###Aggregate Queies
##1.0 Display Total facilitiy usage by type
SELECT f.name, SUM(b.slots) AS total_usage
FROM cd.bookings AS b
JOIN cd.facilities AS f ON b.facid = f.facid
GROUP BY f.name
ORDER BY total_usage;

##2.0 Display members with total slots booked for each facility type.

SELECT DISTINCT m.firstname, m.surname,m.memid, f.facid, COUNT(b.slots) AS total_slots
FROM cd.members m
JOIN cd.bookings b ON m.memid = b.memid
JOIN cd.facilities f ON b.facid = f.facid
GROUP BY m.memid, f.facid
ORDER BY m.surname, m.firstname, f.facid;

##3.0 Display top 3 members with maximum faciliy usage (in terms of slots)
SELECT m.firstname, m.surname, SUM(b.slots) AS total_slots
FROM cd.members m
JOIN cd.bookings b ON m.memid = b.memid
GROUP BY m.memid
ORDER BY total_slots DESC
LIMIT 3;


##4.0 Display facilities booked sorted by slots descending
SELECT f.name AS facility_name, SUM(b.slots) AS total_slots
FROM cd.bookings b
JOIN cd.facilities f ON b.facid = f.facid
GROUP BY f.facid
ORDER BY total_slots DESC;

##5.0 Display top 3 booked facilities with maximum earnings.
SELECT f.name AS facility_name, SUM(b.slots) AS total_slots, SUM(b.slots * f.membercost) AS total_earnings
FROM cd.bookings b
JOIN cd.facilities f ON b.facid = f.facid
GROUP BY f.facid
ORDER BY total_earnings DESC
LIMIT 3;

##6.0 Display top 3 referred members based on booking total slots.
SELECT m1.firstname AS member_name, SUM(b1.slots) AS total_slots
FROM cd.members m1
JOIN cd.bookings b1 ON m1.memid = b1.memid
WHERE m1.recommendedby IS NOT NULL
GROUP BY m1.memid
ORDER BY total_slots DESC
LIMIT 3;


##7.0 Display members based on count of usage ot Tennis (could be tennis or table tennis).
SELECT m.memid, m.surname || ', ' || m.firstname AS member_name, COUNT(*) AS usage_count
FROM cd.members m
JOIN cd.bookings b ON m.memid = b.memid
JOIN cd.facilities f ON b.facid = f.facid
WHERE f.name LIKE '%Tennis'
GROUP BY m.memid
ORDER BY usage_count DESC;






