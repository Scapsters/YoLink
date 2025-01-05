CREATE TABLE IF NOT EXISTS `%(schema_name)s`.devices (
  device_id VARCHAR(16) NOT NULL,
  device_type VARCHAR(45) NOT NULL,
  device_name VARCHAR(60) NOT NULL,
  device_token VARCHAR(60) NOT NULL,
  device_timestamp VARCHAR(45) NOT NULL,

  PRIMARY KEY (device_id)

) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `%(schema_name)s`.events (
  data_id INT NOT NULL AUTO_INCREMENT, -- look into sys_guid and removing column
  
  device_name VARCHAR(60) NOT NULL,
  device_type VARCHAR(45) NOT NULL,
  request_device_id VARCHAR(16) NOT NULL,
  response_device_id VARCHAR(16) NOT NULL,
  response_timestamp VARCHAR(45) NOT NULL,

  event_timestamp VARCHAR(45) NOT NULL,
  field_name VARCHAR(45) NOT NULL,
  field_source VARCHAR(16) NOT NULL,
  field_value VARCHAR(45) NOT NULL,

  PRIMARY KEY (data_id),

  INDEX event_source_device_id_idx (event_source_device_id ASC),
  CONSTRAINT event_source_device_id
    FOREIGN KEY (event_source_device_id)
    REFERENCES %(schema_name)s.devices (device_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    
) ENGINE = InnoDB;