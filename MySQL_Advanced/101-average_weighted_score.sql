-- 101-average_weighted_score.sql
-- Create a procedure that computes and stores the average weighted score for ALL users

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  /* Compute weighted average per user and update in one pass */
  UPDATE users AS u
  LEFT JOIN (
    SELECT
      c.user_id,
      SUM(c.score * p.weight) AS weighted_sum,
      SUM(p.weight)           AS weight_sum
    FROM corrections AS c
    JOIN projects    AS p ON p.id = c.project_id
    GROUP BY c.user_id
  ) AS s ON s.user_id = u.id
  SET u.average_score = IFNULL(s.weighted_sum / NULLIF(s.weight_sum, 0), 0);
END$$

DELIMITER ;
