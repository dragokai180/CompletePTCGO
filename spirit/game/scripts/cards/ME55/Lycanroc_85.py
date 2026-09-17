from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='62848a0e-af31-5006-96de-da01f93804cd',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lycanroc.Name',
    display_name='Lycanroc',
    searchable_by=['Lycanroc', 'Stage 1', 'Lycanroc'],
    subtypes=['Stage 1'],
    collector_number=85,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name',
    family_id=745,
    abilities=[
        Attack(
            title='Counter',
            game_text="If this Pokémon was damaged by an attack during your opponent's last turn, this attack does that much more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Boulder Crush',
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
