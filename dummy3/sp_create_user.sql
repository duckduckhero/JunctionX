CREATE PROCEDURE `sp_kill_user`(
IN p_username varchar(45),
)
BEGIN
UPDATE user SET isalive=0 WHERE username= p_username;
END

CREATE PROCEDURE 'sp_login_user'(
IN p_username varchar(45),
IN p_password varchar(45),
OUT p_result varchar(45)
)
BEGIN 
IF(SELECT * FROM user where username=p_username AND password=p_password) THEN 
SET p_result = "true"
ELSE 
SET p_result = "false"
END IF;
END
