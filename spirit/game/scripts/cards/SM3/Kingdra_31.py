from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='acdd92d7-712e-5077-986a-6aadf034cf11',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name',
    display_name='Kingdra',
    searchable_by=['Kingdra', 'Stage 2', 'Kingdra'],
    subtypes=['Stage 2'],
    collector_number=31,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name',
    family_id=116,
    abilities=[
        Attack(
            title='Brine',
            game_text="This attack does 90 damage to 1 of your opponent's Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tornado Shot',
            game_text="Discard a Water Energy from this Pokémon. This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
