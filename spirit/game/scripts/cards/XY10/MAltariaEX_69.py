from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='405fc0df-12db-5657-ab59-de891d6b5ea4',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MAltariaEX.Name',
    display_name='M Altaria-EX',
    searchable_by=['M Altaria-EX', 'MEGA', 'EX', 'MAltariaEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=69,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AltariaEX.Name',
    family_id=334,
    abilities=[
        Attack(
            title='Mist Purge',
            game_text='If this Pokémon has any Special Energy attached to it, this attack does 30 more damage and heal 30 damage from each of your Pokémon.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
