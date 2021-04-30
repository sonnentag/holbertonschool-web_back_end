-- 
--

DELIMITER $$ 
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)

BEGIN
  UPDATE users 
    SET average_score = (
       SELECT sum(weight)/sum(x.weights) AS average FROM (
	  SELECT p.weight, (count(p.weight) * p.weight) AS weights 
	    FROM projects p, corrections c 
	    WHERE c.user_id = user_id 
            GROUP BY p.weight) x)
      WHERE id = user_id;
END$$

DELIMITER
;
