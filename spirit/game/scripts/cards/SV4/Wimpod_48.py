from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='725f8e5e-e8b8-5f5d-a8de-4899cf78a291',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name',
    display_name='Wimpod',
    searchable_by=['Wimpod', 'Basic', 'Wimpod'],
    subtypes=['Basic'],
    collector_number=48,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=767,
    abilities=[
        Attack(
            title='Sneaky Snacking',
            game_text="Flip a coin. If heads, discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
