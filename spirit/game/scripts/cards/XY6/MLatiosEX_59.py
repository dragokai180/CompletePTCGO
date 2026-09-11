from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3285863e-aa65-591a-998a-76dd6d47d247',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MLatiosEX.Name',
    display_name='M Latios-EX',
    searchable_by=['M Latios-EX', 'MEGA', 'EX', 'MLatiosEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=59,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.LatiosEX.Name',
    family_id=381,
    abilities=[
        Attack(
            title='Sonic Ace',
            game_text="Discard 2 Energy attached to this Pokémon. This attack does 120 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
