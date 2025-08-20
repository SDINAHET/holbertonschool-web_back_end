-- 7-average_score.sql
-- Create a stored procedure that computes and stores a user's average score

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
  DECLARE v_avg DECIMAL(10,2);

  -- Compute average (may be decimal); default to 0 if no corrections
  SELECT AVG(score) INTO v_avg
    FROM corrections
   WHERE user_id = p_user_id;

  SET v_avg = IFNULL(v_avg, 0);

  -- Store it on the user row
  UPDATE users
     SET average_score = v_avg
   WHERE id = p_user_id;
END$$

DELIMITER ;
