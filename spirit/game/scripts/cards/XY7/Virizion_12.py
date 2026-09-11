from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3cebc353-5dd1-5d65-84ac-c75fd8705fef',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Virizion.Name',
    display_name='Virizion',
    searchable_by=['Virizion', 'Basic', 'Virizion'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=640,
    abilities=[
        Attack(
            title='Bail Out',
            game_text='Put 2 Pokémon from your discard pile into your hand.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Prize Count',
            game_text='If you have more Prize cards left than your opponent, this attack does 80 more damage.',
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
