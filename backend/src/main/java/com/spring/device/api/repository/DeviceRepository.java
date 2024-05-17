package com.spring.device.api.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.spring.device.api.entity.Device;

public interface DeviceRepository extends JpaRepository<Device, Long> {
}
