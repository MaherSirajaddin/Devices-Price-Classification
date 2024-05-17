package com.spring.device.api.entity;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "devices")
public class Device {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private Integer battery_power;

    @Column(nullable = false)
    private Boolean blue;

    @Column(nullable = false)
    private Double clock_speed;

    @Column(nullable = false)
    private Boolean dual_sim;

    @Column(nullable = false)
    private Integer fc;

    @Column(nullable = false)
    private Boolean four_g;

    @Column(nullable = false)
    private Integer int_memory;

    @Column(nullable = false)
    private Integer m_dep;

    @Column(nullable = false)
    private Double mobile_wt;

    @Column(nullable = false)
    private Integer n_cores;

    @Column(nullable = false)
    private Integer pc;

    @Column(nullable = false)
    private Integer px_height;

    @Column(nullable = false)
    private Integer px_width;

    @Column(nullable = false)
    private Integer ram;

    @Column(nullable = false)
    private Double sc_h;

    @Column(nullable = false)
    private Double sc_w;

    @Column(nullable = false)
    private Integer talk_time;

    @Column(nullable = false)
    private Boolean three_g;

    @Column(nullable = false)
    private Boolean touch_screen;

    @Column(nullable = false)
    private Boolean wifi;

    private Integer price_range;

    public void setPriceRange(Integer predicted_price) {
        this.price_range = predicted_price;
    }
}
