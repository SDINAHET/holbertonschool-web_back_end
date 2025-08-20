-- 9-index_name_score.sql
-- Create an index on the first letter of `name` AND on `score`

CREATE INDEX idx_name_first_score ON names (name(1), score);
