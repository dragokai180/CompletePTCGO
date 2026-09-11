from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e0144fb3-8739-5b2a-b914-eb5d0c1bb964',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Buzzwole.Name',
    display_name='Buzzwole',
    searchable_by=['Buzzwole', 'Basic', 'Ultra Beast', 'Buzzwole'],
    subtypes=['Basic', 'Ultra Beast'],
    collector_number=218,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=794,
    abilities=[
        Ability(
            title='Beast Boost',
            game_text="This Pokémon's attacks do 20 more damage to your opponent's Active Pokémon for each Prize card you have taken (before applying Weakness and Resistance).",
            passive=standard_passive("This Pokémon's attacks do 20 more damage to your opponent's Active Pokémon for each Prize card you have taken (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Touchdown',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
