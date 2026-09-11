from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0c3fca43-47e4-51e2-a9e0-3a806a9481da',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MAlakazamEX.Name',
    display_name='M Alakazam-EX',
    searchable_by=['M Alakazam-EX', 'MEGA', 'EX', 'MAlakazamEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=26,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlakazamEX.Name',
    family_id=65,
    abilities=[
        Attack(
            title='Zen Force',
            game_text="This attack does 30 more damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
