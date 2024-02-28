-- SQL
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);

    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    IF avg_score IS NULL THEN
        SET avg_score = 0;
    END IF;

    INSERT INTO user_average_scores (user_id, average_score)
    VALUES (p_user_id, avg_score)
    ON DUPLICATE KEY UPDATE average_score = avg_score;
END;