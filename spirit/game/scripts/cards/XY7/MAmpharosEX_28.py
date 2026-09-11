from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='00cd5d45-f606-5f39-86f3-63c581141172',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MAmpharosEX.Name',
    display_name='M Ampharos-EX',
    searchable_by=['M Ampharos-EX', 'MEGA', 'EX', 'MAmpharosEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=28,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AmpharosEX.Name',
    family_id=181,
    abilities=[
        Attack(
            title='Exavolt',
            game_text="You may do 50 more damage and leave your opponent's Active Pokémon Paralyzed. If you do, this Pokémon does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
