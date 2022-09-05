CREATE OR REPLACE VIEW stats_report_1h AS
SELECT service_id as 'service_id', country_id as 'country_id', 
(SELECT DISTINCT sc.id FROM service_countries sc, report r WHERE sc.service_id = r.service_id AND sc.country_id = r.country_id) as 'id',
(SELECT count(*) FROM report r WHERE r.submittedAt BETWEEN date_sub(NOW(), INTERVAL 1 hour) AND date_sub(NOW(), INTERVAL 55 minute) AND sc.service_id = r.service_id AND sc.country_id = r.country_id) as 'slice1',
(SELECT count(*) FROM report r WHERE r.submittedAt BETWEEN date_sub(NOW(), INTERVAL 55 minute) AND date_sub(NOW(), INTERVAL 50 minute) AND sc.service_id = r.service_id AND sc.country_id = r.country_id) as 'slice2',
(SELECT count(*) FROM report r WHERE r.submittedAt BETWEEN date_sub(NOW(), INTERVAL 50 minute) AND date_sub(NOW(), INTERVAL 45 minute) AND sc.service_id = r.service_id AND sc.country_id = r.country_id) as 'slice3',
(SELECT count(*) FROM report r WHERE r.submittedAt BETWEEN date_sub(NOW(), INTERVAL 45 minute) AND date_sub(NOW(), INTERVAL 40 minute) AND sc.service_id = r.service_id AND sc.country_id = r.country_id) as 'slice4',
(SELECT count(*) FROM report r WHERE r.submittedAt BETWEEN date_sub(NOW(), INTERVAL 40 minute) AND date_sub(NOW(), INTERVAL 35 minute) AND sc.service_id = r.service_id AND sc.country_id = r.country_id) as 'slice5',
(SELECT count(*) FROM report r WHERE r.submittedAt BETWEEN date_sub(NOW(), INTERVAL 35 minute) AND date_sub(NOW(), INTERVAL 30 minute) AND sc.service_id = r.service_id AND sc.country_id = r.country_id) as 'slice6',
(SELECT count(*) FROM report r WHERE r.submittedAt BETWEEN date_sub(NOW(), INTERVAL 30 minute) AND date_sub(NOW(), INTERVAL 25 minute) AND sc.service_id = r.service_id AND sc.country_id = r.country_id) as 'slice7',
(SELECT count(*) FROM report r WHERE r.submittedAt BETWEEN date_sub(NOW(), INTERVAL 25 minute) AND date_sub(NOW(), INTERVAL 20 minute) AND sc.service_id = r.service_id AND sc.country_id = r.country_id) as 'slice8',
(SELECT count(*) FROM report r WHERE r.submittedAt BETWEEN date_sub(NOW(), INTERVAL 20 minute) AND date_sub(NOW(), INTERVAL 15 minute) AND sc.service_id = r.service_id AND sc.country_id = r.country_id) as 'slice9',
(SELECT count(*) FROM report r WHERE r.submittedAt BETWEEN date_sub(NOW(), INTERVAL 15 minute) AND date_sub(NOW(), INTERVAL 10 minute) AND sc.service_id = r.service_id AND sc.country_id = r.country_id) as 'slice10',
(SELECT count(*) FROM report r WHERE r.submittedAt BETWEEN date_sub(NOW(), INTERVAL 10 minute) AND date_sub(NOW(), INTERVAL 5 minute) AND sc.service_id = r.service_id AND sc.country_id = r.country_id) as 'slice11',
(SELECT count(*) FROM report r WHERE r.submittedAt BETWEEN date_sub(NOW(), INTERVAL 5 minute) AND date_sub(NOW(), INTERVAL 0 minute) AND sc.service_id = r.service_id AND sc.country_id = r.country_id) as 'slice12',
(SELECT count(*) FROM report r WHERE r.submittedAt BETWEEN date_sub(NOW(), INTERVAL 1 hour) AND NOW() AND sc.service_id = r.service_id AND sc.country_id = r.country_id) as 'totalReport'
FROM service_countries sc
WHERE EXISTS (SELECT * FROM report r WHERE sc.service_id = r.service_id AND sc.country_id = r.country_id);