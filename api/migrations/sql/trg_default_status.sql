CREATE TRIGGER trg_default_status
AFTER INSERT ON service_countries
FOR EACH ROW
BEGIN
	INSERT INTO `current_status` (country_id, service_id, status_id) VALUES (NEW.country_id, NEW.service_id, 1);
END;
