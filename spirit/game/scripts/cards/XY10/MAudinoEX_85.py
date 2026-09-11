from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='431dc256-822d-57c5-9316-6c79af339988',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MAudinoEX.Name',
    display_name='M Audino-EX',
    searchable_by=['M Audino-EX', 'MEGA', 'EX', 'MAudinoEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=85,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AudinoEX.Name',
    family_id=531,
    abilities=[
        Attack(
            title='Magical Symphony',
            game_text="If you played a Supporter card from your hand during this turn, this attack does 50 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
