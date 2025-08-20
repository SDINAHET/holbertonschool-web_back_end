-- 100-average_weighted_score.sql
-- Create a procedure that computes and stores a user's average weighted score

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN p_user_id INT)
BEGIN
  DECLARE v_weighted_sum FLOAT DEFAULT 0;
  DECLARE v_weight_sum   FLOAT DEFAULT 0;
  DECLARE v_avg          FLOAT DEFAULT 0;

  -- Sum of (score * project weight) and sum of weights for this user
  SELECT
      COALESCE(SUM(c.score * p.weight), 0),
      COALESCE(SUM(p.weight), 0)
    INTO v_weighted_sum, v_weight_sum
  FROM corrections c
  JOIN projects   p ON p.id = c.project_id
  WHERE c.user_id = p_user_id;

  -- Compute weighted average (0 if no weights)
  SET v_avg = IF(v_weight_sum = 0, 0, v_weighted_sum / v_weight_sum);

  -- Store result
  UPDATE users
     SET average_score = v_avg
   WHERE id = p_user_id;
END$$

DELIMITER ;
