from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='41dd81cd-a20b-5daf-aabc-87d1a0075647',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name',
    display_name='Gligar',
    searchable_by=['Gligar', 'Basic', 'Gligar'],
    subtypes=['Basic'],
    collector_number=98,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=207,
    abilities=[
        Ability(
            title='Free Flight',
            game_text='If this Pokémon has no Energy attached to it, it has no Retreat Cost.',
            passive=standard_passive('If this Pokémon has no Energy attached to it, it has no Retreat Cost.'),
        ),
        Attack(
            title='Shinobi Strike',
            game_text='If you played Janine from your hand during this turn, this attack does 90 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
