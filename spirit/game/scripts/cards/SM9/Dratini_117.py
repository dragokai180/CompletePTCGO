from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4a074075-eedf-56a5-bcd1-bf357e5a79e5',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name',
    display_name='Dratini',
    searchable_by=['Dratini', 'Basic', 'Dratini'],
    subtypes=['Basic'],
    collector_number=117,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=147,
    abilities=[
        Ability(
            title='Defensive Scales',
            game_text="Prevent all effects of your opponent's attacks, except damage, done to this Pokémon.",
            passive=standard_passive("Prevent all effects of your opponent's attacks, except damage, done to this Pokémon."),
        ),
        Attack(
            title='Rain Splash',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
