from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='afd5b1be-e4db-5a50-bc6f-c70778a9503a',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name',
    display_name='Lugia',
    searchable_by=['Lugia', 'Basic', 'Lugia'],
    subtypes=['Basic'],
    collector_number=78,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=249,
    abilities=[
        Ability(
            title='Pressure',
            game_text="As long as this Pokémon is your Active Pokémon, any damage done by attacks from your opponent's Active Pokémon is reduced by 20 (before applying Weakness and Resistance).",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, any damage done by attacks from your opponent's Active Pokémon is reduced by 20 (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Intensifying Burn',
            game_text="If your opponent's Active Pokémon is a Pokémon-EX, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
