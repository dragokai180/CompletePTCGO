from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='64ac7ea7-94d7-5d89-a344-c56d1c46a1a5',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name',
    display_name='Golbat',
    searchable_by=['Golbat', 'Stage 1', 'Golbat'],
    subtypes=['Stage 1'],
    collector_number=111,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name',
    family_id=41,
    abilities=[
        Attack(
            title='Leech Life',
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
