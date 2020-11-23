CREATE INDEX ix_advertisement_startDate_endDate ON advertisement(startDate, endDate);
CREATE INDEX ix_advertisement_endDate_startDate ON advertisement(endDate, startDate);