from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8b159553-c2bd-5c49-b00a-3fcc70b98d27',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name',
    display_name='Bouffalant',
    searchable_by=['Bouffalant', 'Basic', 'Bouffalant'],
    subtypes=['Basic'],
    collector_number=119,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=626,
    abilities=[
        Ability(
            title='Sap Sipper',
            game_text="This Pokémon's attacks do 40 more damage to your opponent's Grass Pokémon (before applying Weakness and Resistance).",
            passive=standard_passive("This Pokémon's attacks do 40 more damage to your opponent's Grass Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Derail',
            game_text="Discard a Special Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
