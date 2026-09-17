from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c5eedd83-78ff-508b-bc0d-154304fe79cb',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name',
    display_name='Umbreon',
    searchable_by=['Umbreon', 'Stage 1', 'Umbreon'],
    subtypes=['Stage 1'],
    collector_number=91,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Retaliate',
            game_text="If any of your Pokémon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 100 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Darkness Fang',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
