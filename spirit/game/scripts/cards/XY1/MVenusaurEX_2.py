from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0e0cc3e6-2ad9-5916-9ca7-bfde20e2ce96',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MVenusaurEX.Name',
    display_name='M Venusaur-EX',
    searchable_by=['M Venusaur-EX', 'MEGA', 'EX', 'MVenusaurEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=2,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurEX.Name',
    family_id=3,
    abilities=[
        Attack(
            title='Crisis Vine',
            game_text="Your opponent's Active Pokémon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
