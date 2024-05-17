package com.spring.device.api.controller;

import com.spring.device.api.entity.Device;
import com.spring.device.api.service.DeviceService;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.List;

@RestController
@RequestMapping("/api/devices")
public class DeviceController {
    private final DeviceService deviceService;

    public DeviceController(DeviceService deviceService) {
        this.deviceService = deviceService;
    }

    @GetMapping
    public List<Device> getAllDevices() {
        return deviceService.getAllDevices();
    }

    @GetMapping("/{id}")
    public Device getDeviceById(@PathVariable Long id) {
        return deviceService.getDeviceById(id);
    }

    @PostMapping
    public Device addDevice(@RequestBody Device device) {
        return deviceService.addDevice(device);
    }

    @PostMapping("/predict/{deviceId}")
    public Device predictDevicePrice(@PathVariable Long deviceId) {
        Device device = deviceService.getDeviceById(deviceId);

        // Call the Python API to predict the price range
        RestTemplate restTemplate = new RestTemplate();
        String priceRangeApiUrl = "http://localhost:5000/predict/mobile_price"; 
        ResponseEntity<Integer> response = restTemplate.postForEntity(priceRangeApiUrl, device, Integer.class);
        Integer predictedPriceRange = response.getBody();

        // Update the device with the predicted price range
        return deviceService.updateDevicePriceRange(deviceId, predictedPriceRange);
    }
}
