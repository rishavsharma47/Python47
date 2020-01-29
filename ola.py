{
    "hotspot_zone": {
        "is_hotpot_zone": true,
        "desc": "Choose from convenient pickup points to board your cab.",
        "default_pickup_point_id": 10881,
        "hotspot_boundary":
            [
                12.9468154,
                77.6472151
            ],
            [
                12.9474219,
                77.6475155
            ],
            [
                12.9478192,
                77.6467001
            ]
        ],
        "pickup_points":
            {
                "lat": 12.9509456,
                "lng": 77.6408958,
                "name": "Sunriver",
                "id": 10880
            },
            {
                "lat": 12.9506006,
                "lng": 77.6417542,
                "name": "Cherry Hills",
                "id": 10881
            }
        ]
  },
	"categories": [{
		"id": "auto",
		"display_name": "Auto",
		"currency": "INR",
		"distance_unit": "kilometre",
		"time_unit": "minute",
		"eta": 1,
		"distance": "0.2",
		"ride_later_enabled": "false",
		"image": "http://d1foexe15giopy.cloudfront.net/auto.png",
        "hotspot_pickup_points": [
                10879,
                10880,
                10881
        ],
		"cancellation_policy": {
			"cancellation_charge": 15,
			"currency": "INR",
			"cancellation_charge_applies_after_time": 5,
			"time_unit": "minute"
		},
		"fare_breakup": [{
				"type": "flat_rate",
				"minimum_distance": 0,
				"minimum_time": 0,
				"base_fare": 50,
				"minimum_fare": 60,
				"cost_per_distance": 8,
				"waiting_cost_per_minute": 0,
				"ride_cost_per_minute": 1,
				"surcharge": [],
				"rates_lower_than_usual": false,
				"rates_higher_than_usual": false,
			}
		],
		"all_cabs": [{
            "lat": 12.9543501,
            "lng": 77.5438193,
            "id":"e0e7ba15f7249207c1d77ec07c1c06",
            "bearing":534,
            "accuracy":15
      },
      {
            "lat": 12.9561008,
            "lng": 77.5464725,
            "id":"15f7249207c1d77e9207c1c0601d6c9c",
            "bearing":135,
            "accuracy":10
      }]
	}],
	"ride_estimate": [{
      "category": "auto",
      "distance": 16.9,
      "travel_time_in_minutes": 93,
      "amount_min": 227,
      "amount_max": 249,
      "booking_fee": 30,
      "booking_fee_breakup":
      [
        {
          "display_text": "Advance Booking Fee",
          "value": 30
        }
      ],
      "taxes":
      {
        "total_tax": 11.87
      },
      "hub_charges":
      {
        "total_hub_fee": 80,
        "pickup_hub_fee": 80,
        "pickup_hub_name": "Ola pick up charge"
      }
      "discounts":
      {
        "discount_type": "custom",
        "discount_code": "BLR29",
        "discount_mode": "AUTO",
        "discount": 0,
        "cashback": 0,
        "pass_savings": 16
      },
      "upfront":
      {
        "fare": 238,
        "fare_id": "1:000008:50002738-7242",
        "select_discount": null
        "is_upfront_applicable": true
      }
	}],
	"previous_cancellation_charges":
      [
        {
          "currency": "INR",
          "booking_id”: "CRN123456789",
          "amount": “25”
        },
        {
          "currency": "INR",
          "booking_id": "OSN123456789",
          "amount": 50
        }
      ]
}