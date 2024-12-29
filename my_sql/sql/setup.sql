CREATE TABLE IF NOT EXISTS `%(schema_name)s`.devices (
  device_id INT NOT NULL,
  device_type_id INT NOT NULL,
  device_name VARCHAR(60) NOT NULL,
  PRIMARY KEY (device_id)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `%(schema_name)s`.events (
  event_id INT NOT NULL,
  event_source_device_id INT NOT NULL,
  event_timestamp VARCHAR(45) NOT NULL,
  PRIMARY KEY (event_id),
  INDEX event_source_device_id_idx (event_source_device_id ASC),
  CONSTRAINT event_source_device_id
    FOREIGN KEY (event_source_device_id)
    REFERENCES %(schema_name)s.devices (device_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `%(schema_name)s`.data (
  data_id INT NOT NULL,
  event_id INT NOT NULL,
  data_name VARCHAR(45) NOT NULL,
  data_value VARCHAR(45) NOT NULL,
  PRIMARY KEY (data_id),
  INDEX event_id_idx (event_id ASC),
  CONSTRAINT event_id
    FOREIGN KEY (event_id)
    REFERENCES %(schema_name)s.events (event_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;