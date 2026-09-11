from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d8c8e45e-2215-57ba-b6b6-0045aac0a465',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name',
    display_name='Mewtwo',
    searchable_by=['Mewtwo', 'Basic', 'Mewtwo'],
    subtypes=['Basic'],
    collector_number=77,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=150,
    abilities=[
        Ability(
            title='Pressure',
            game_text="As long as this Pokémon is your Active Pokémon, your opponent's Active Pokémon's attack do 20 less damage (before applying Weakness and Resistance).",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, your opponent's Active Pokémon's attack do 20 less damage (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Super Psy Bolt',
            cost={PokemonTypes.PSYCHIC: 3},
            damage=100,
        ),
    ],
)
