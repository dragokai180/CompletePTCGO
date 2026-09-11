from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e1d2f9d6-eb05-5c24-bf4b-6ae18522c02d',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name',
    display_name='Regirock',
    searchable_by=['Regirock', 'Basic', 'Regirock'],
    subtypes=['Basic'],
    collector_number=40,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=377,
    abilities=[
        Attack(
            title='Rock Throw',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title='Unyielding Rock',
            game_text="If your opponent's Active Pokémon is a Pokémon-EX, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
