from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='afa32d4f-ee3a-563e-9ba2-74b8a578eb3a',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Umbreonex.Name',
    display_name='Umbreon ex',
    searchable_by=['Umbreon ex', 'Stage 1', 'ex', 'Umbreonex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=92,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Lunatic Claw',
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 140 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
