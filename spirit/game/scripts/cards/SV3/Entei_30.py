from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a9c7f1c7-138c-5101-9639-f4d564b7e2a9',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name',
    display_name='Entei',
    searchable_by=['Entei', 'Basic', 'Entei'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=244,
    abilities=[
        Ability(
            title='Pressure',
            game_text="As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon do 20 less damage (before applying Weakness and Resistance).",
            passive=standard_passive("As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon do 20 less damage (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Blaze Ball',
            game_text='This attack does 20 more damage for each Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
