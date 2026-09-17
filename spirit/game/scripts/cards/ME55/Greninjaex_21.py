from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='226b211f-584e-5c33-831c-315c7ca90afd',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Greninjaex.Name',
    display_name='Greninja ex',
    searchable_by=['Greninja ex', 'Stage 2', 'ex', 'Greninjaex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=21,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name',
    family_id=658,
    abilities=[
        Attack(
            title='Stealthy Slash',
            game_text="This attack does 30 damage to 1 of your opponent's Pokémon for each damage counter on that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Aqua Edge',
            cost={PokemonTypes.WATER: 2},
            damage=160,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
