from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0c8ced55-2ccd-5bce-864c-a1639121cf33',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MSharpedoEX.Name',
    display_name='M Sharpedo-EX',
    searchable_by=['M Sharpedo-EX', 'MEGA', 'EX', 'MSharpedoEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=200,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.SharpedoEX.Name',
    family_id=319,
    abilities=[
        Attack(
            title='Torpedo Dive',
            game_text="This attack does 10 damage to each of your opponent's Benched Pokémon for each Colorless in that Pokémon's Retreat Cost. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
