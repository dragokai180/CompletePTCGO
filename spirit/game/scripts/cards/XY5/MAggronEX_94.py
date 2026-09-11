from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0dd7b90b-267b-5998-889c-835209515be0',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MAggronEX.Name',
    display_name='M Aggron-EX',
    searchable_by=['M Aggron-EX', 'MEGA', 'EX', 'MAggronEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=94,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AggronEX.Name',
    family_id=306,
    abilities=[
        Attack(
            title='Megaton Slam',
            game_text="You may flip a coin. If heads, this attack does 120 more damage. If tails, this attack does 20 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
