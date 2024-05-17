package com.spring.device;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackages = "com.spring.device.api")
public class DeviceApplication {

	public static void main(String[] args) {
		SpringApplication.run(DeviceApplication.class, args);
	}

}
