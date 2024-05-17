package com.spring.device.api.service;

import com.spring.device.api.entity.Device;
import com.spring.device.api.repository.DeviceRepository;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class DeviceService {
    private final DeviceRepository deviceRepository;

    public DeviceService(DeviceRepository deviceRepository) {
        this.deviceRepository = deviceRepository;
    }

    public List<Device> getAllDevices() {
        return deviceRepository.findAll();
    }

    public Device getDeviceById(Long id) {
        return deviceRepository.findById(id).orElseThrow(() -> new RuntimeException("Device not found"));
    }

    @Transactional
    public Device addDevice(Device device) {
        return deviceRepository.save(device);
    }

    @Transactional
    public Device updateDevicePriceRange(Long id, Integer priceRange) {
        Device device = getDeviceById(id);
        device.setPriceRange(priceRange);
        return deviceRepository.save(device);
    }
}
