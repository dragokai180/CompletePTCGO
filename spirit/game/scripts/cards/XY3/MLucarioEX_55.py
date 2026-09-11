from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='263409b1-6d43-516e-ae53-7897dfe21127',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MLucarioEX.Name',
    display_name='M Lucario-EX',
    searchable_by=['M Lucario-EX', 'MEGA', 'EX', 'MLucarioEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=55,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.LucarioEX.Name',
    family_id=448,
    abilities=[
        Attack(
            title='Rising Fist',
            game_text="Discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
