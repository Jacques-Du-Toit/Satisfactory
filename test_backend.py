import pytest
from logic import *


def test_all_combinations():
    assert all_combinations([[1, 2, 3]]) == [[1], [2], [3]]
    assert all_combinations([['a', 'b'], [1, 2, 3]]) == [
        ['a', 1], ['a', 2], ['a', 3],
        ['b', 1], ['b', 2], ['b', 3]
    ]


def test_all_trees_from_part():
    assert all_trees_from_part('reinforced iron plate', 15) == [
        [
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
        ],
        [
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
                    "index": "screw 1",
                    "machine": "constructor",
                    "inputs": [
                        {
                            "part": "iron ingot",
                            "required_per_minute": 12.5
                        }
                    ],
                    "output_per_minute": 180.0,
                    "recipe_output_per_minute": 50,
                    "machines_required": 3.6,
                    "layer": 2
                },
                [
                    {
                        "part": "iron ingot",
                        "required_per_minute": 45.0,
                        "layer": 3
                    }
                ]
            ]
        ]
    ]

    assert all_trees_from_part('screw', 145) == [
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
                "output_per_minute": 145.0,
                "recipe_output_per_minute": 40,
                "machines_required": 3.625,
                "layer": 1
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
                    "output_per_minute": 36.25,
                    "recipe_output_per_minute": 15,
                    "machines_required": 2.4166666666666665,
                    "layer": 2
                },
                [
                    {
                        "part": "iron ingot",
                        "required_per_minute": 36.25,
                        "layer": 3
                    }
                ]
            ]
        ],
        [
            {
                "index": "screw 1",
                "machine": "constructor",
                "inputs": [
                    {
                        "part": "iron ingot",
                        "required_per_minute": 12.5
                    }
                ],
                "output_per_minute": 145.0,
                "recipe_output_per_minute": 50,
                "machines_required": 2.9,
                "layer": 1
            },
            [
                {
                    "part": "iron ingot",
                    "required_per_minute": 36.25,
                    "layer": 2
                }
            ]
        ]
    ]