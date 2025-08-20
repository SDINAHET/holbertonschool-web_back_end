-- 11-need_meeting.sql
-- View listing students with score < 80 AND (no last_meeting OR last_meeting > 1 month ago)

DROP VIEW IF EXISTS need_meeting;

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
  AND (last_meeting IS NULL
       OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
