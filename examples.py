a = [
	{
		"index": "reinforced iron plate 0",
		"machine": "assembler",
		"inputs": [
			{
				"part": "iron plate",
				"required_per_minute": 30
			},
			{
				"part": "screw",
				"required_per_minute": 60
			}
		],
		"output_per_minute": 15.0,
		"recipe_output_per_minute": 5,
		"machines_required": 3.0,
		"layer": 1
	},
	[
		{
			"index": "iron plate 0",
			"machine": "constructor",
			"inputs": [
				{
					"part": "iron ingot",
					"required_per_minute": 30
				}
			],
			"output_per_minute": 90.0,
			"recipe_output_per_minute": 20,
			"machines_required": 4.5,
			"layer": 2
		},
		[
			{
				"part": "iron ingot",
				"required_per_minute": 135.0,
				"layer": 3
			}
		]
	],
	[
		{
			"index": "screw 0",
			"machine": "constructor",
			"inputs": [
				{
					"part": "iron rod",
					"required_per_minute": 10
				}
			],
			"output_per_minute": 180.0,
			"recipe_output_per_minute": 40,
			"machines_required": 4.5,
			"layer": 2
		},
		[
			{
				"index": "iron rod 0",
				"machine": "constructor",
				"inputs": [
					{
						"part": "iron ingot",
						"required_per_minute": 15
					}
				],
				"output_per_minute": 45.0,
				"recipe_output_per_minute": 15,
				"machines_required": 3.0,
				"layer": 3
			},
			[
				{
					"part": "iron ingot",
					"required_per_minute": 45.0,
					"layer": 4
				}
			]
		]
	]
]